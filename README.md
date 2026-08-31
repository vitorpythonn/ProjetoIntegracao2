# Projeto Integrado Inovação — Sistema de Gerenciamento de Estoque

Sistema de Gerenciamento de Estoque desenvolvido para o Projeto Integrado Inovação — ADS.

## Objetivo

Desenvolver uma solução para auxiliar uma empresa de comércio eletrônico no controle de produtos, quantidades, localizações e movimentações de estoque.

## Funcionalidades

* Cadastro de produtos.
* Consulta de produtos.
* Atualização de estoque.
* Registro de entradas.
* Registro de saídas.
* Validação de quantidade disponível.
* Rastreamento da localização dos produtos.
* Relatório de estoque baixo.
* Relatório de excesso de estoque.
* Relatório da posição geral do estoque.
* Consulta do histórico de movimentações.

## Tecnologias utilizadas

* Python 3
* Flask 3.1.3
* SQLite
* HTML5
* CSS3
* JavaScript
* unittest
* Git e GitHub

## Estrutura do projeto

```text
ProjetoIntegracao2/
│
├── 01-documentacao/
│   ├── 01-situacao-problema/
│   ├── 02-scrum/
│   ├── 03-tabela-verdade/
│   ├── 04-algoritmos/
│   ├── 05-casos-de-uso/
│   └── 06-evidencias/
│
├── 02-sistema/
│   ├── database/
│   │   └── schema.sql
│   ├── static/
│   │   └── css/
│   ├── templates/
│   ├── tests/
│   ├── database.py
│   ├── main.py
│   └── requirements.txt
│
├── 03-relatorio-final/
│   └── relatorio-final.md
│
├── .gitignore
└── README.md
```

## Banco de dados

O sistema utiliza SQLite.

O esquema do banco está disponível em:

```text
02-sistema/database/schema.sql
```

O banco de dados é criado automaticamente durante a inicialização da aplicação.

O arquivo `.db` local não é versionado no Git, pois é um arquivo gerado pela aplicação.

## Instalação

Clone o repositório:

```bash
git clone https://github.com/vitorpythonn/ProjetoIntegracao2.git
```

Entre no diretório:

```bash
cd ProjetoIntegracao2
```

Instale as dependências:

```bash
python -m pip install -r 02-sistema/requirements.txt
```

## Execução

Execute:

```bash
python 02-sistema/main.py
```

Depois acesse:

```text
http://127.0.0.1:5000
```

## Testes

Para executar os testes automatizados:

```bash
python -m unittest discover -s "02-sistema/tests" -v
```

Resultado esperado:

```text
Ran 5 tests

OK
```

Os testes validam:

* cadastro de produto;
* entrada de estoque;
* saída de estoque;
* relatório de estoque baixo;
* impedimento de saída superior ao estoque disponível.

## Documentação acadêmica

A documentação do projeto está organizada no diretório `01-documentacao`, contendo:

* situação-problema;
* objetivos;
* planejamento Scrum;
* tabela verdade;
* estruturas de dados;
* algoritmos;
* casos de uso;
* evidências.

O relatório final está disponível em:

```text
03-relatorio-final/relatorio-final.md
```

## Projeto

Repositório:

https://github.com/vitorpythonn/ProjetoIntegracao2
