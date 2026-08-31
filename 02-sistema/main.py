from datetime import datetime

from flask import Flask, flash, redirect, render_template, request, url_for

from database import get_connection, init_database


app = Flask(__name__)
app.secret_key = "projeto-integrado-estoque"


@app.route("/")
def index():
    connection = get_connection()

    total_produtos = connection.execute(
        "SELECT COUNT(*) AS total FROM produto"
    ).fetchone()["total"]

    total_estoque = connection.execute(
        "SELECT COALESCE(SUM(quantidade), 0) AS total FROM produto"
    ).fetchone()["total"]

    total_movimentacoes = connection.execute(
        "SELECT COUNT(*) AS total FROM movimentacao"
    ).fetchone()["total"]

    connection.close()

    return render_template(
        "index.html",
        total_produtos=total_produtos,
        total_estoque=total_estoque,
        total_movimentacoes=total_movimentacoes,
    )


@app.route("/produtos")
def produtos():
    connection = get_connection()

    produtos = connection.execute(
        """
        SELECT
            produto.id,
            produto.nome,
            categoria.nome AS categoria,
            produto.quantidade,
            produto.preco,
            localizacao.deposito,
            localizacao.setor,
            localizacao.posicao
        FROM produto
        INNER JOIN categoria
            ON produto.categoria_id = categoria.id
        INNER JOIN localizacao
            ON produto.localizacao_id = localizacao.id
        ORDER BY produto.nome
        """
    ).fetchall()

    categorias = connection.execute(
        "SELECT id, nome FROM categoria ORDER BY nome"
    ).fetchall()

    localizacoes = connection.execute(
        """
        SELECT id, deposito, setor, posicao
        FROM localizacao
        ORDER BY deposito, setor, posicao
        """
    ).fetchall()

    connection.close()

    return render_template(
        "produtos.html",
        produtos=produtos,
        categorias=categorias,
        localizacoes=localizacoes,
    )


@app.route("/produtos/cadastrar", methods=["POST"])
def cadastrar_produto():
    nome = request.form.get("nome", "").strip()
    categoria_id = request.form.get("categoria_id", "").strip()
    quantidade = request.form.get("quantidade", "").strip()
    preco = request.form.get("preco", "").strip().replace(",", ".")
    localizacao_id = request.form.get("localizacao_id", "").strip()

    if not nome or not categoria_id or not quantidade or not preco or not localizacao_id:
        flash("Todos os campos são obrigatórios.", "error")
        return redirect(url_for("produtos"))

    try:
        quantidade = int(quantidade)
        preco = float(preco)
        categoria_id = int(categoria_id)
        localizacao_id = int(localizacao_id)
    except ValueError:
        flash("Quantidade, preço, categoria e localização devem possuir valores válidos.", "error")
        return redirect(url_for("produtos"))

    if quantidade < 0:
        flash("A quantidade não pode ser negativa.", "error")
        return redirect(url_for("produtos"))

    if preco < 0:
        flash("O preço não pode ser negativo.", "error")
        return redirect(url_for("produtos"))

    connection = get_connection()

    try:
        connection.execute(
            """
            INSERT INTO produto
                (nome, categoria_id, quantidade, preco, localizacao_id)
            VALUES (?, ?, ?, ?, ?)
            """,
            (nome, categoria_id, quantidade, preco, localizacao_id),
        )

        connection.commit()
        flash("Produto cadastrado com sucesso.", "success")

    except Exception as error:
        connection.rollback()
        flash(f"Não foi possível cadastrar o produto: {error}", "error")

    finally:
        connection.close()

    return redirect(url_for("produtos"))

@app.route("/movimentacoes/registrar", methods=["POST"])
def registrar_movimentacao():
    produto_id = request.form.get("produto_id", "").strip()
    tipo = request.form.get("tipo", "").strip().upper()
    quantidade = request.form.get("quantidade", "").strip()
    responsavel = request.form.get("responsavel", "").strip()

    if not produto_id or not tipo or not quantidade or not responsavel:
        flash("Todos os campos são obrigatórios.", "error")
        return redirect(url_for("movimentacoes"))

    if tipo not in ("ENTRADA", "SAIDA"):
        flash("Tipo de movimentação inválido.", "error")
        return redirect(url_for("movimentacoes"))

    try:
        produto_id = int(produto_id)
        quantidade = int(quantidade)
    except ValueError:
        flash("Produto e quantidade devem possuir valores válidos.", "error")
        return redirect(url_for("movimentacoes"))

    if quantidade <= 0:
        flash("A quantidade deve ser maior que zero.", "error")
        return redirect(url_for("movimentacoes"))

    connection = get_connection()

    try:
        produto = connection.execute(
            "SELECT id, nome, quantidade FROM produto WHERE id = ?",
            (produto_id,),
        ).fetchone()

        if produto is None:
            flash("Produto não encontrado.", "error")
            return redirect(url_for("movimentacoes"))

        estoque_atual = produto["quantidade"]

        if tipo == "SAIDA" and quantidade > estoque_atual:
            flash(
                f"Estoque insuficiente. Disponível: {estoque_atual}.",
                "error",
            )
            return redirect(url_for("movimentacoes"))

        if tipo == "ENTRADA":
            novo_estoque = estoque_atual + quantidade
        else:
            novo_estoque = estoque_atual - quantidade

        connection.execute(
            """
            UPDATE produto
            SET quantidade = ?
            WHERE id = ?
            """,
            (novo_estoque, produto_id),
        )

        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        connection.execute(
            """
            INSERT INTO movimentacao
                (produto_id, tipo, quantidade, data, responsavel)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                produto_id,
                tipo,
                quantidade,
                data,
                responsavel,
            ),
        )

        connection.commit()

        flash(
            f"Movimentação registrada. Novo estoque de "
            f"{produto['nome']}: {novo_estoque}.",
            "success",
        )

    except Exception as error:
        connection.rollback()
        flash(
            f"Não foi possível registrar a movimentação: {error}",
            "error",
        )

    finally:
        connection.close()

    return redirect(url_for("movimentacoes"))

@app.route("/movimentacoes")
def movimentacoes():
    connection = get_connection()

    movimentacoes = connection.execute(
        """
        SELECT
            movimentacao.id,
            produto.nome AS produto,
            movimentacao.tipo,
            movimentacao.quantidade,
            movimentacao.data,
            movimentacao.responsavel
        FROM movimentacao
        INNER JOIN produto
            ON movimentacao.produto_id = produto.id
        ORDER BY movimentacao.id DESC
        """
    ).fetchall()

    produtos = connection.execute(
        "SELECT id, nome, quantidade FROM produto ORDER BY nome"
    ).fetchall()

    connection.close()

    return render_template(
        "movimentacoes.html",
        movimentacoes=movimentacoes,
        produtos=produtos,
    )


@app.route("/relatorios")
def relatorios():
    connection = get_connection()

    produtos = connection.execute(
        """
        SELECT
            produto.id,
            produto.nome,
            produto.quantidade,
            produto.preco,
            categoria.nome AS categoria,
            localizacao.deposito,
            localizacao.setor,
            localizacao.posicao
        FROM produto
        INNER JOIN categoria
            ON produto.categoria_id = categoria.id
        INNER JOIN localizacao
            ON produto.localizacao_id = localizacao.id
        ORDER BY produto.quantidade
        """
    ).fetchall()

    connection.close()

    estoque_baixo = [produto for produto in produtos if produto["quantidade"] < 5]
    excesso_estoque = [produto for produto in produtos if produto["quantidade"] > 50]

    return render_template(
        "relatorios.html",
        estoque_baixo=estoque_baixo,
        excesso_estoque=excesso_estoque,
        produtos=produtos,
    )


if __name__ == "__main__":
    init_database()
    app.run(debug=True)