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
