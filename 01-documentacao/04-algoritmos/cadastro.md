# Algoritmo de Cadastro

## Objetivo

Definir o procedimento utilizado para cadastrar um novo produto no Sistema de Gerenciamento de Estoque.

## Dados necessários

Para realizar o cadastro, devem ser informados:

- nome do produto;
- categoria;
- quantidade inicial em estoque;
- preço;
- localização no depósito.

O sistema também atribui um identificador único ao produto.

## Algoritmo

INÍCIO

1. Solicitar o nome do produto.
2. Solicitar a categoria do produto.
3. Solicitar a quantidade inicial em estoque.
4. Solicitar o preço do produto.
5. Solicitar a localização no depósito.
6. Gerar um identificador para o produto.
7. Criar o registro do produto com os dados informados.
8. Armazenar o produto.
9. Informar que o cadastro foi realizado.

FIM

## Validações

Antes de armazenar o produto, devem ser verificadas as informações obrigatórias.

- O nome deve ser informado.
- A categoria deve ser informada.
- A quantidade deve ser válida.
- O preço deve ser válido.
- A localização deve ser informada.

Caso alguma informação obrigatória seja inválida ou não seja informada, o cadastro não deve ser concluído até que o dado seja corrigido.

## Resultado

Após a conclusão do cadastro, o produto passa a fazer parte do estoque e suas informações podem ser utilizadas nas consultas, movimentações e relatórios do sistema.