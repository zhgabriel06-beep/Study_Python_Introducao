# Atribuindo valor nas variaveis 
nome ='Gabriel'
idade = 19
peso = 87.3

# Pedindo para o usuario colocar valor nas variaveis 
nome1 = str(input('Digite seu nome: '))
idade2 = int(input('Digite sua idade: '))
peso2 = float(input('Digite seu peso: '))
print(f"Nome: {nome1}, Idade: {idade2}, Peso: {peso2}")


nome3 = str(input('Digite seu nome: '))
print(f'Olá, {nome3}! Seja bem-vindo(a) ao nosso programa.')

# Data de nascimento
dia = int(input('Digite o dia do seu nascimento: '))
mes = int(input('Digite o mês do seu nascimento: '))
ano = int(input('Digite o ano do seu nascimento: '))
print(f'Você nasceu em {dia}/{mes}/{ano}.')

# Soma
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
soma = numero1 + numero2
print(f'A soma de {numero1} e {numero2} é igual a {soma}.')


n = input('Digite algo: ')
print(n.isnumeric()) # Verifica se é um número
print(n.isalpha()) # Verifica se é uma letra
print(n.isalnum()) # Verifica se é alfanumérico
print(n.isupper()) # Verifica se é maiúsculo
print(n.islower()) # Verifica se é minúsculo


number1 = int(input('Digite um numero: '))

print(f'O número digitado foi {number1} e o seu antecessor é {number1 - 1} e o seu sucessor é {number1 + 1}.')

#Tabuada

number2 = int(input('Digite outro número: '))
print(f'A tabuada de {number2} é:')
for i in range(1, 11):
    print(f'{number2} x {i} = {number2 * i}')
    
# Converter em dollar
number3 = float(input('Digite um valor em reais: '))
if number3 < 0:
    print('Valor inválido. Por favor, digite um valor positivo.')
else: 
    dollar = number3 / 5.25
    print(f'O valor de R${number3:.2f} convertido em dólar é: ${dollar:.2f}')
    
#  Calcula area de uma parede e quantidade de tinta necessária para pintar a parede
largura = float(input('Digite a largura da parede em metros: '))
comprimento = float(input('Digite o comprimento da parede em metros: '))
area = largura * comprimento
# Quantidade de tinta necessária (1 litro pinta 2m²)
tinta_necessaria = area / 2
print(f'A área da parede é de {area:.2f} m² e a quantidade de tinta necessária para pintar a parede é de {tinta_necessaria:.2f} litros.')







