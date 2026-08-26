# Estruturas de Dados

## Objetivo

Definir como as informações utilizadas pelo Sistema de Gerenciamento de Estoque serão organizadas e armazenadas.

## Produto

A estrutura Produto representa os itens armazenados no estoque.

Produto
- id
- nome
- categoria
- quantidade
- preço
- localização

O campo id identifica unicamente o produto. Os demais campos armazenam as informações necessárias para seu controle no estoque.

## Categoria

A estrutura Categoria representa a classificação dos produtos.

Categoria
- id
- nome

Cada categoria possui um identificador e um nome.

## Movimentação

A estrutura Movimentação registra as alterações realizadas no estoque.

Movimentação
- id
- produto
- tipo
- quantidade
- data
- responsável

O campo tipo identifica se a movimentação corresponde a uma entrada ou saída de produtos.

## Localização

A estrutura Localização permite identificar onde o produto está armazenado.

Localização
- id
- depósito
- setor
- posição

A localização é composta pelo depósito, setor e posição física do produto.

## Compra

A estrutura Compra representa as solicitações de aquisição de produtos.

Compra
- id
- produto
- quantidade
- status
- solicitante
- data

O campo status permite acompanhar a situação da solicitação de compra.

## Nota Fiscal

A estrutura NotaFiscal representa a nota fiscal relacionada à entrada de produtos.

NotaFiscal
- id
- número
- data
- validada

O campo validada indica se a nota fiscal foi validada antes do registro da entrada.

## Organização dos dados

As estruturas foram definidas de acordo com as necessidades apresentadas no enunciado. Produto, Categoria, Movimentação, Localização, Compra e NotaFiscal representam os principais conjuntos de informações utilizados pelo sistema.

Essa organização permite realizar operações de cadastro, consulta, movimentação de estoque e geração de relatórios sem adicionar funcionalidades que não sejam necessárias ao projeto.