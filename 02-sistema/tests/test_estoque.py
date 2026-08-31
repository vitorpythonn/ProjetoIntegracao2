import unittest


class TestEstoque(unittest.TestCase):

    def test_cadastro_produto(self):
        produto = {
            "id": 1,
            "nome": "Produto Teste",
            "categoria": "Eletrônicos",
            "quantidade": 10,
            "preco": 100.00,
            "localizacao": "Deposito A"
        }

        self.assertEqual(produto["nome"], "Produto Teste")
        self.assertEqual(produto["quantidade"], 10)

    def test_entrada_estoque(self):
        quantidade_atual = 10
        entrada = 5

        nova_quantidade = quantidade_atual + entrada

        self.assertEqual(nova_quantidade, 15)

    def test_saida_estoque(self):
        quantidade_atual = 10
        saida = 3

        nova_quantidade = quantidade_atual - saida

        self.assertEqual(nova_quantidade, 7)

    def test_saida_maior_que_estoque(self):
        quantidade_atual = 10
        saida = 15

        self.assertGreater(saida, quantidade_atual)

    def test_relatorio_estoque_baixo(self):
        quantidade = 3
        limite = 5

        estoque_baixo = quantidade < limite

        self.assertTrue(estoque_baixo)


if __name__ == "__main__":
    unittest.main()