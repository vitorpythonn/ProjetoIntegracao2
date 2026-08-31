# Descrição dos Casos de Uso

## UC01 — Registrar Entrada de Produto

**Ator principal:** Estoquista

**Objetivo:** Registrar a entrada de novos produtos no estoque.

**Pré-condição:** O estoquista possui os dados do produto e a nota fiscal de entrada.

**Fluxo principal:**

1. O estoquista inicia o registro de entrada.
2. O sistema solicita os dados do produto.
3. O sistema solicita os dados da nota fiscal.
4. O sistema realiza a validação da nota fiscal.
5. O sistema registra a entrada do produto.
6. O sistema atualiza a quantidade disponível em estoque.
7. O sistema confirma o registro da entrada.

**Fluxo alternativo:**

- Caso a nota fiscal não seja válida, a entrada não deve ser registrada.

**Resultado:** A entrada do produto é registrada e a quantidade em estoque é atualizada.

---

## UC02 — Validar Nota Fiscal

**Ator principal:** Estoquista

**Objetivo:** Validar a nota fiscal antes do registro da entrada do produto.

**Pré-condição:** Uma nota fiscal foi informada durante o processo de entrada.

**Fluxo principal:**

1. O sistema recebe os dados da nota fiscal.
2. O sistema realiza a validação.
3. O sistema identifica a nota como válida.
4. O processo de entrada pode continuar.

**Fluxo alternativo:**

- Caso a nota fiscal seja inválida, o sistema informa a inconsistência e impede o registro da entrada.

**Resultado:** A nota fiscal é validada para permitir ou impedir o registro da entrada.

---

## UC03 — Emitir Relatório de Posição Semanal

**Ator principal:** Usuário

**Objetivo:** Emitir um relatório com a posição do estoque no período semanal.

**Pré-condição:** Existem informações de estoque disponíveis para consulta.

**Fluxo principal:**

1. O usuário solicita o relatório de posição semanal.
2. O sistema realiza a consolidação das compras.
3. O sistema reúne as informações necessárias.
4. O sistema gera o relatório.
5. O sistema apresenta o relatório ao usuário.

**Resultado:** O relatório de posição semanal é disponibilizado.

---

## UC04 — Solicitar Compra de Produtos

**Ator principal:** Usuário

**Objetivo:** Solicitar a compra de produtos necessários para o estoque.

**Pré-condição:** O usuário identificou a necessidade de reposição de produtos.

**Fluxo principal:**

1. O usuário solicita a compra de produtos.
2. O sistema realiza a consolidação das compras.
3. O sistema registra a solicitação de compra.
4. A solicitação fica disponível para autorização do gerente de setor.

**Resultado:** A solicitação de compra é registrada para posterior autorização.

---

## UC05 — Consolidar Compras

**Ator principal:** Usuário

**Objetivo:** Consolidar as informações necessárias relacionadas às compras.

**Pré-condição:** O processo de emissão de relatório ou solicitação de compra foi iniciado.

**Fluxo principal:**

1. O sistema recebe as informações relacionadas às compras.
2. O sistema organiza as informações.
3. O sistema consolida os dados.
4. O processo que solicitou a consolidação continua.

**Resultado:** As informações de compras são consolidadas.

---

## UC06 — Autorizar Compra de Produtos

**Ator principal:** Gerente de Setor

**Objetivo:** Autorizar a compra de produtos solicitada pelo usuário.

**Pré-condição:** Existe uma solicitação de compra registrada.

**Fluxo principal:**

1. O gerente de setor consulta a solicitação.
2. O gerente analisa as informações da compra.
3. O gerente autoriza a compra.
4. O sistema registra a autorização.

**Resultado:** A solicitação de compra fica autorizada.

---

## Relacionamentos entre os Casos de Uso

Os seguintes casos de uso possuem relacionamento `<<include>>`:

- **Registrar Entrada de Produto** inclui **Validar Nota Fiscal**.
- **Emitir Relatório de Posição Semanal** inclui **Consolidar Compras**.
- **Solicitar Compra de Produtos** inclui **Consolidar Compras**.

Esses relacionamentos representam funcionalidades que obrigatoriamente fazem parte dos respectivos processos.