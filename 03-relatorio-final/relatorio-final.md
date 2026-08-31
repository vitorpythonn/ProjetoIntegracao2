# Projeto Integrado Inovação — Sistema de Gerenciamento de Estoque

## 1. Introdução

Este projeto apresenta o desenvolvimento de um Sistema de Gerenciamento de Estoque para uma empresa de comércio eletrônico.

A solução foi desenvolvida para auxiliar no controle dos produtos armazenados, suas quantidades, localizações e movimentações, disponibilizando uma interface web para utilização do sistema.

## 2. Situação-Problema

A empresa enfrenta dificuldades relacionadas à falta de produtos, excesso de estoque, localização dos itens nos depósitos e acompanhamento das movimentações.

Diante desse cenário, foi definida e implementada uma solução capaz de organizar as informações do estoque, registrar movimentações e disponibilizar relatórios para acompanhamento.

## 3. Objetivos

O objetivo geral é desenvolver um Sistema de Gerenciamento de Estoque capaz de auxiliar no controle dos produtos armazenados, suas quantidades, localizações e movimentações.

Entre os objetivos específicos estão:

* cadastro de produtos;
* atualização do estoque;
* rastreamento da localização;
* registro de movimentações de entrada e saída;
* consulta de produtos;
* geração de relatórios;
* consulta do histórico de movimentações.

## 4. Metodologia Scrum

O desenvolvimento foi organizado utilizando a metodologia Scrum, com três sprints:

* Sprint 01 — Análise e Planejamento.
* Sprint 02 — Estruturas de Dados e Algoritmos.
* Sprint 03 — Casos de Uso e Finalização.

O acompanhamento das atividades foi realizado por meio do quadro Scrum no Trello.

As atividades foram organizadas conforme o fluxo:

**Backlog → Sprint Atual → Em Progresso → Concluído**

## 5. Tabela Verdade

Foram utilizadas as seguintes variáveis:

* P — Cadastro de Produtos.
* E — Atualização de Estoque.
* L — Rastreamento de Localização.
* R — Relatórios.

A expressão lógica utilizada foi:

**P ∧ E ∧ L ∧ R**

A solução completa é considerada verdadeira somente quando os quatro requisitos são atendidos simultaneamente.

A tabela verdade completa, contendo as 16 combinações possíveis, encontra-se no documento específico da atividade.

## 6. Estruturas de Dados

Foram definidas as seguintes estruturas:

* Produto.
* Categoria.
* Movimentação.
* Localização.
* Compra.
* NotaFiscal.

Essas estruturas representam os principais conjuntos de informações necessários ao funcionamento da solução.

No sistema implementado, essas informações são armazenadas em um banco de dados SQLite.

O esquema do banco está definido no arquivo:

`02-sistema/database/schema.sql`

## 7. Algoritmos

Foram definidos algoritmos para:

* cadastro de produtos;
* consulta de produtos;
* movimentação de estoque;
* registro de entradas;
* registro de saídas;
* atualização do estoque;
* geração de relatórios;
* consulta do histórico de movimentações.

Os algoritmos foram utilizados como base para a implementação das funcionalidades do sistema.

## 8. Casos de Uso

O sistema possui três atores principais:

* Estoquista.
* Usuário.
* Gerente de Setor.

Os casos de uso definidos são:

* Registrar Entrada de Produto.
* Validar Nota Fiscal.
* Emitir Relatório de Posição Semanal.
* Solicitar Compra de Produtos.
* Consolidar Compras.
* Autorizar Compra de Produtos.

Os relacionamentos `<<include>>` foram definidos de acordo com as dependências obrigatórias entre as funcionalidades.

O Diagrama de Casos de Uso está disponível em:

`01-documentacao/05-casos-de-uso/diagrama-casos-uso.png`

## 9. Implementação do Sistema

O sistema foi implementado utilizando Python e Flask, com banco de dados SQLite.

As principais tecnologias utilizadas foram:

* Python 3;
* Flask 3.1.3;
* SQLite;
* HTML5;
* CSS3;
* unittest;
* Git e GitHub.

A aplicação possui uma interface web composta pelas seguintes áreas:

* página inicial;
* cadastro e consulta de produtos;
* movimentações de estoque;
* relatórios.

Entre as funcionalidades implementadas estão:

* cadastro de produtos;
* consulta de produtos;
* registro de entradas;
* registro de saídas;
* validação de quantidade disponível;
* atualização automática do estoque;
* identificação da localização dos produtos;
* relatório de estoque baixo;
* relatório de excesso de estoque;
* relatório da posição geral do estoque.

## 10. Banco de Dados

O sistema utiliza SQLite para armazenamento das informações.

O banco possui estruturas relacionadas a:

* categorias;
* localizações;
* produtos;
* movimentações;
* compras;
* notas fiscais.

O arquivo `schema.sql` contém a definição das tabelas, relacionamentos, restrições e dados iniciais utilizados pela aplicação.

O banco de dados local gerado durante a execução não é versionado no Git. Dessa forma, o esquema necessário para recriação do banco permanece disponível no repositório.

## 11. Testes

Foram desenvolvidos testes automatizados utilizando o módulo `unittest` do Python.

Foram executados cinco testes:

* `test_cadastro_produto`;
* `test_entrada_estoque`;
* `test_relatorio_estoque_baixo`;
* `test_saida_estoque`;
* `test_saida_maior_que_estoque`.

Resultado da execução:

```text
Ran 5 tests in 0.001s

OK
```

Todos os cinco testes foram aprovados.

Os testes verificam operações fundamentais do sistema, incluindo cadastro, entrada, saída, geração de relatório e bloqueio de saída superior à quantidade disponível.

## 12. Versionamento

O projeto foi versionado utilizando Git e disponibilizado no GitHub.

O repositório contém:

* documentação acadêmica;
* código-fonte;
* banco de dados e schema;
* interface web;
* testes automatizados;
* diagrama de casos de uso;
* evidências;
* relatório final;
* README com instruções de execução.

O arquivo `.gitignore` impede o versionamento de arquivos temporários e do banco SQLite gerado localmente.

## 13. Evidências

As evidências do desenvolvimento incluem:

* registros do quadro Scrum no Trello;
* documentos produzidos durante as sprints;
* Diagrama de Casos de Uso;
* validação da aplicação;
* execução dos testes automatizados.

As evidências disponíveis no projeto estão organizadas no diretório:

`01-documentacao/06-evidencias/`

## 14. Conclusão

O projeto resultou na implementação de um Sistema de Gerenciamento de Estoque funcional, desenvolvido a partir dos requisitos definidos durante a análise do problema.

A solução contempla cadastro e consulta de produtos, controle de entradas e saídas, atualização do estoque, rastreamento de localização e geração de relatórios.

Além da implementação do sistema, foram desenvolvidos os artefatos acadêmicos relacionados à situação-problema, objetivos, Scrum, tabela verdade, estruturas de dados, algoritmos, casos de uso, evidências e documentação final.

A aplicação foi validada por meio de testes automatizados, nos quais os cinco testes desenvolvidos foram executados com sucesso.

O projeto completo está versionado no GitHub, contendo a documentação e os arquivos necessários para execução e avaliação da solução.
