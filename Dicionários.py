'''
Preencha um dicionário com as informações de 5 produtos fornecidos pelo usuário.
- Solicite os dados ao usuário
- Utilize o nome do produto como chave e o preço como valor.
- Percorra o dicionário e exiba o nome dos produtos com preço
superior a R$ 50,00.
Exemplo:
Veja um exemplo da estrutura do dicionário.
{'caneta': 3.0, 'Pen drive': 100.0,'Teclado': 30.0, 'Lápis': 1.5}
'''
produtos = {}

for _ in range(5):
    nome = str(input('Digite um produto: '))
    preco = float(input('Digite o valor do produto: '))
    produtos[nome] = preco

print('\n\n\nProdutos com valor maior que 50 reais:')
for nome, preco in produtos.items():
    if preco > 50:
        print(f'Nome do produto: {nome}\nValor do produto: R${preco:.2f}\n')



'''
Preencha um dicionário com os dados de 5 alunos fornecidos pelo usuário.
- Solicite os dados do usuário
- Utilize o ra do aluno como chave e uma lista de três notas como valor.
- Percorra o dicionário e exiba a média de cada aluno.
Exemplo:
Veja um exemplo da estrutura do dicionário.
{19230490: [10, 8.0, 7.5], 2002441: [6, 5, 7.5], 2001332: [5,8,9.5]}
'''


'''
Escreva uma função que conta a quantidade de vogais em um texto e armazena tal
quantidade em um dicionário, onde a chave é a vogal considerada e o valor é a quantidade
de vezes que essa vogal aparece no texto.
A função deve receber o texto como entrada e retornar o dicionário.
Exemplo:
Para o texto abaixo:
texto = ' faculdade impacta de tecnologia'
A função deve devolver o seguinte dicionário:
{'a': 5, 'u': 1, 'e': 3, 'o' : 2, 'i': 2 }
'''

