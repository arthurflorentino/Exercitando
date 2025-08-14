# 1. Determinar se um ano fornecido pelo usuário é bissexto ou não
# Um ano é bissexto se for divisível por 4 e, se for divisível por 100, deve ser também divisível por 400.
ano = int(input("Ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("1) Ano Bissexto.\n")
else:
    print("1) Não Bissexto\n")


# 2. Calcular o fatorial de um número usando loop do-while (ou equivalente em Python)
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)
n = int(input('Digite um número: '))
result_fat = fatorial(n)
print(result_fat)



# 3. Determinar se um número fornecido pelo usuário é primo
def primo(n, divisor = 2):
    if n < 2:
        return 'Não é primo'
    if divisor > int(n ** 0.5):
        return 'É primo'
    if n % divisor == 0:
        return 'Não é primo'
    return primo(n, divisor + 1)

while True:
    try:
        numerico = int(input('Digite um número inteiro: '))
        print(primo(numerico))
        break
    except ValueError:
        print('Entrada inválida. Por favor, digite um número inteiro.')



# 4. Gerar a sequência de Fibonacci até um número fornecido pelo usuário
def fibonacci(fib):
    if fib == 1:
        return 0
    elif fib == 2:
        return 1
    else:
        return fibonacci(fib - 1) + fibonacci(fib - 2)
numero = int(input('Digite: '))
print(fibonacci(numero))