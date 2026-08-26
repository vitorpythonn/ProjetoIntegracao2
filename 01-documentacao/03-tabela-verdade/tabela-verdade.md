# Tabela Verdade

## Variáveis

As variáveis booleanas utilizadas para representar os requisitos do Sistema de Gerenciamento de Estoque são:

- **P** = Cadastro de Produtos
- **E** = Atualização de Estoque
- **L** = Rastreamento de Localização
- **R** = Relatórios

A solução será considerada completa somente quando todos os requisitos forem atendidos simultaneamente.

## Expressão lógica

**P ∧ E ∧ L ∧ R**

A expressão será verdadeira somente quando P, E, L e R forem verdadeiras.

## Tabela Verdade

| P | E | L | R | P ∧ E ∧ L ∧ R |
|---|---|---|---|----------------|
| V | V | V | V | V |
| V | V | V | F | F |
| V | V | F | V | F |
| V | V | F | F | F |
| V | F | V | V | F |
| V | F | V | F | F |
| V | F | F | V | F |
| V | F | F | F | F |
| F | V | V | V | F |
| F | V | V | F | F |
| F | V | F | V | F |
| F | V | F | F | F |
| F | F | V | V | F |
| F | F | V | F | F |
| F | F | F | V | F |
| F | F | F | F | F |

## Interpretação

A tabela possui 16 combinações possíveis para as quatro variáveis booleanas.

A expressão **P ∧ E ∧ L ∧ R** apresenta resultado verdadeiro somente na primeira combinação, quando todos os requisitos do sistema são atendidos simultaneamente.

Nas demais combinações, pelo menos um dos requisitos não é atendido e, portanto, o resultado da expressão é falso.

Dessa forma, a tabela demonstra logicamente que a solução completa do Sistema de Gerenciamento de Estoque depende da implementação conjunta das quatro funcionalidades principais: cadastro de produtos, atualização de estoque, rastreamento de localização e geração de relatórios.