## Resposta do Teste Técnico do Programa de Formação em Elixir da Stone
Autor: Souza, Gustavo.

Enunciado do teste: [README.md](https://gist.github.com/programa-elixir/1bd50a6d97909f2daa5809c7bb5b9a8a)

Minha outra solução, dessa vez utilizando Elixir: [Repositório](https://github.com/gdssouza/aprendendo_Elixir/blob/main/desafioStone.exs)

### Explicando o código

O repositório possui um módulo chamado pagamentos, dentro há uma função nomeada desafio que requer dois argumentos:

* Lista de compras: Uma matriz 3xN com os itens (string), quantidade de cada item (inteiro) e preço por unidade item (float ou inteiro).
* Lista de emails: onde cada email é uma string

A função faz uso de outras 3 funções auxiliares:

* Uma para validação, composta por condicionais que garatem a estrutura dos dados.
* Uma para encontrar o valor total, para isso, foi utilizado um laço de repetição que percorre todos os dados.
* Uma para realizar a divisão, essa é o cerne do problema. Para isso, é obtido o inteiro da divisão e o resto da divisão, que por definição matemática também SEMPRE é um inteiro e NUNCA maior ou igual que o quociente. Sendo assim, o programa percorre os emails distribuindo os valores de pagamento somados com o resto de divisão limitado a 1 centavo. Esse limite é necessário para garantir a distribuição mais próxima possível do igualitário. Não há prejuízo.

A função desafio retorna um dicionário que é a resposta do teste técnico.

### Teste

Para testar o programa é necessário dois datasets:

* Lista de compras. Colunas na seguinte ordem: item, quantidade e preço
* Lista de emails. Uma única coluna com os emails.

```python

python teste.py <caminho lista de compras> <caminho lista de emails>
```

Para simplificar a sua vida, há na pasta dados um exemplo bem simples. Para testar utilize:

```python
python teste.py dados/datasetCompras_exemplo dados/datasetEmails_exemplo
```

### Agradecimentos


Agradeço à Stone pela oportunidade de participar deste desafio. Acesse [Jornada Stone](https://jornada.stone.com.br/).
