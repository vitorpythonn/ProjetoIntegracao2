# Algoritmos de Relatórios

## Objetivo

Definir os procedimentos utilizados para gerar relatórios sobre a situação e a movimentação do estoque.

## Relatório de Estoque Baixo

O relatório de estoque baixo identifica produtos cuja quantidade disponível está abaixo do limite definido para controle.

INÍCIO

1. Percorrer os produtos cadastrados.
2. Verificar a quantidade disponível de cada produto.
3. Comparar a quantidade com o limite de estoque baixo.
4. Selecionar os produtos abaixo do limite.
5. Exibir os produtos encontrados.

FIM

## Relatório de Excesso de Estoque

O relatório de excesso de estoque identifica produtos cuja quantidade disponível está acima do limite definido para controle.

INÍCIO

1. Percorrer os produtos cadastrados.
2. Verificar a quantidade disponível de cada produto.
3. Comparar a quantidade com o limite de excesso de estoque.
4. Selecionar os produtos acima do limite.
5. Exibir os produtos encontrados.

FIM

## Relatório de Movimentação

O relatório de movimentação apresenta as entradas e saídas registradas para os produtos.

INÍCIO

1. Consultar o histórico de movimentações.
2. Percorrer as movimentações registradas.
3. Identificar o produto, tipo, quantidade, data e responsável.
4. Organizar as informações.
5. Exibir o histórico de movimentações.

FIM

## Consulta do Histórico

Para consultar o histórico de movimentações, o sistema deve recuperar os registros armazenados e permitir sua visualização.

As informações apresentadas devem incluir:

- produto;
- tipo de movimentação;
- quantidade;
- data;
- responsável.

## Resultado

Os algoritmos permitem identificar produtos com estoque baixo, produtos em excesso e consultar a movimentação dos produtos, fornecendo informações para acompanhamento do estoque.