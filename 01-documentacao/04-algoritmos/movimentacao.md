# Algoritmo de Movimentação

## Objetivo

Definir o procedimento utilizado para registrar entradas e saídas de produtos e atualizar a quantidade disponível em estoque.

## Tipos de movimentação

O sistema considera dois tipos de movimentação:

- Entrada: representa o recebimento de novos produtos.
- Saída: representa a retirada de produtos do estoque devido à venda.

## Algoritmo

INÍCIO

1. Solicitar o produto.
2. Solicitar o tipo de movimentação.
3. Solicitar a quantidade.
4. Solicitar o responsável pela movimentação.
5. Verificar se o produto está cadastrado.
6. Verificar se a quantidade informada é válida.
7. Se o tipo for ENTRADA, adicionar a quantidade ao estoque.
8. Se o tipo for SAÍDA, verificar se existe quantidade suficiente em estoque.
9. Se houver quantidade suficiente, retirar a quantidade do estoque.
10. Registrar a movimentação com produto, tipo, quantidade, data e responsável.
11. Atualizar a quantidade do produto.
12. Informar que a movimentação foi registrada.

FIM

## Validações

Antes de registrar uma movimentação, devem ser realizadas as seguintes verificações:

- O produto deve estar cadastrado.
- A quantidade deve ser maior que zero.
- O tipo de movimentação deve ser ENTRADA ou SAÍDA.
- Em uma saída, a quantidade solicitada não pode ser maior que a quantidade disponível em estoque.

Caso alguma validação não seja atendida, a movimentação não deve ser registrada.

## Registro de entrada

Quando o tipo de movimentação for ENTRADA, a quantidade recebida deve ser adicionada à quantidade atual do produto.

Exemplo:

Quantidade atual = 20

Entrada = 10

Nova quantidade = 30

## Registro de saída

Quando o tipo de movimentação for SAÍDA, a quantidade vendida deve ser retirada da quantidade atual do produto.

Exemplo:

Quantidade atual = 30

Saída = 5

Nova quantidade = 25

Caso a quantidade disponível seja insuficiente, a saída não deve ser realizada.

## Resultado

Após uma movimentação válida, a quantidade do produto é atualizada e a operação fica registrada no histórico de movimentações.