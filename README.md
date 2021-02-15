## Resposta do Teste Técnico do Programa de Formação em Elixir da Stone
Autor: Souza, Gustavo.

Enunciado do teste: [README.md](https://gist.github.com/programa-elixir/1bd50a6d97909f2daa5809c7bb5b9a8a)

### Explicando o código

O repositório possui uma classe nomeada Desafio que requer dois argumentos:

* Lista de compras: Uma matriz 3xN com os itens (string), quantidade de cada item (inteiro) e preço por unidade item (float ou inteiro).
* Lista de emails: onde cada email é uma string

A classe faz uso de 3 funções auxiliares:

* Uma para validação, composta por condicionais que garatem a estrutura dos dados.
* Uma para encontrar o valor total, para isso, foi utilizado um laço de repetição que percorre todos os dados.
* Uma para realizar a divisão, essa é o cerne do problema. Para isso, é obtido o inteiro da divisão e o resto da divisão, que por definição matemática também SEMPRE é um inteiro e NUNCA maior ou igual que o quociente. Sendo assim, o programa percorre os emails distribuindo os valores de pagamento somados com o resto de divisão limitado a 1 centavo. Esse limite é necessário para garantir a distribuição mais próxima possível do igualitário.

A classe possui uma função chamada retornaMapa que retorna um dicionário onde a chave será o e-mail e o valor será quanto ele deve pagar nessa conta, ou seja, é a função que responde o teste técnico.

### Arquivos

O código está no arquivo \_\_init\_\_.py. O arquivo teste.py é a forma que eu encontrei para testar o código, para isso, é necessário um dataset com as compras e um dataset com os emails. \
Para facilitar o teste, criei um exemplo na pasta dados. O caminho do exemplo já está no teste.py, ou seja, é só rodar o programa :)
