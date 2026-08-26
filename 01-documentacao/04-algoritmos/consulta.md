# Algoritmo de Consulta

## Objetivo

Definir o procedimento utilizado para consultar as informações dos produtos cadastrados no Sistema de Gerenciamento de Estoque.

## Dados utilizados

A consulta pode utilizar as seguintes informações:

- identificador do produto;
- nome do produto;
- categoria;
- localização.

## Algoritmo

INÍCIO

1. Solicitar o critério de consulta.
2. Receber o valor informado pelo usuário.
3. Percorrer os produtos cadastrados.
4. Comparar o valor informado com os dados dos produtos.
5. Identificar os produtos que correspondem ao critério.
6. Exibir as informações dos produtos encontrados.
7. Caso nenhum produto seja encontrado, informar que não existem resultados para a consulta.

FIM

## Informações apresentadas

Para cada produto encontrado, devem ser apresentadas:

- id;
- nome;
- categoria;
- quantidade em estoque;
- preço;
- localização.

## Consulta por localização

Para consultar os produtos armazenados em determinado local, o sistema deve comparar a localização informada com a localização cadastrada para cada produto.

Somente os produtos que estiverem na localização correspondente devem ser apresentados.

## Resultado

O algoritmo permite localizar produtos cadastrados e consultar suas principais informações, incluindo quantidade em estoque e localização no depósito.