import random
from re import S
import time

# Verifica se o número digitado pelo usuário é igual ao número gerado aleatoriamente
num = int(random.randint(1, 5))

escolha = int(input("Digite uma numero de 1 a 5: "))

if escolha == num:
    print("Parabéns! Você acertou o número!")
else:
    print(f"Que pena! Você errou o número. O número correto era {num}.")


# Velocidade do carro
velocidade = float(input("Digite a velocidade do carro em km/h: "))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f"Você foi multado! A multa é de R${multa:.2f}.")
else:
    print("Você está dentro do limite de velocidade. Dirija com segurança!")

    # Verifica se o ano digitado pelo usuário é bissexto
ano = int(input("Digite um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")

    # Aumento de salário
salario = float(input("Digite o salário do funcionário: "))
if salario <= 1250:
    aumento = salario * 0.15
else:
    aumento = salario * 0.10
novo_salario = salario + aumento
print(f"O novo salário do funcionário é R${novo_salario:.2f}.")


# Verificar se consegue formar um triângulo com os lados informados pelo usuário
lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    if lado1 == lado2 == lado3:
        print("O triângulo formado é equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("O triângulo formado é isósceles.")
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print("O triângulo formado é escaleno.")
else:
    print("Não é possível formar um triângulo com os lados informados.")

genero = input("Digite o gênero da pessoa (M/F): ").upper()
peso = float(input("Digite o peso da pessoa em kg: "))
altura = float(input("Digite a altura da pessoa em metros: "))

imc = peso / (altura**2)

if genero == "M":
    if imc < 20.7:
        classificacao = "Abaixo do peso"
    elif imc < 26.4:
        classificacao = "Peso ideal"
    else:
        classificacao = "Acima do peso"

elif genero == "F":
    if imc < 19.1:
        classificacao = "Abaixo do peso"
    elif imc < 25.8:
        classificacao = "Peso ideal"
    else:
        classificacao = "Acima do peso"

else:
    classificacao = "Gênero inválido"

print(f"IMC: {imc:.2f}")
print(f"Classificação: {classificacao}")

# Pedra, papel e tesoura

opcoes = ["pedra", "papel", "tesoura"]

jogador = input("Escolha pedra, papel ou tesoura: ").lower()

if jogador not in opcoes:
    print("Opção inválida!")
else:
    computador = random.choice(opcoes)

if jogador == computador:
    print(f"Empate! Ambos escolheram {jogador}.")
elif (
    (jogador == "pedra" and computador == "tesoura")
    or (jogador == "papel" and computador == "pedra")
    or (jogador == "tesoura" and computador == "papel")
):
    print(f"Você venceu! {jogador} vence {computador}.")
else:
    print(f"Você perdeu! {computador} vence {jogador}.")

    # Contagem regressiva para o ano novo
print("Contagem regressiva para o ano novo:")
for i in range(10, 0, -1):
    print(f"segundo {i}")
    time.sleep(1)
print("Feliz Ano Novo!")

# divider de todos os numeros impares multiplo de 3 entre 0 a 500
divider = 0
for i in range(501):
    if i % 3 == 0 and i % 2 != 0:
        divider += i
print(divider)

num = int(input("Escreva um valor :"))
num = num**3

print(num, "\n")

# The formula to calculate the area of a circumference is defined as A = π . R2. Considering to this problem that π = 3.14159:

n = 3.14159
r = float(input())
a = n * r**2
print(f"A={a:.4f}")

# divider de numeros
a = int(input())
b = int(input())
print(f"X = {a + b}")

# Read four integer values named A, B, C and D. Calculate and print the difference of product A and B by the product of C and D (A * B - C * D).

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(f"DIFERENCA = {a * b - c * d}")

# The input is composed of several test cases. The first line has an integer C, representing the number of test cases. The following C lines contain two integers N and M (1 <= N, M <= 100).

c = int(input())

for _ in range(c):
    n, m = map(int, input().split())
    print(len(str(n**m)))

    # Numero primo
divider = 0
number = int(input("Digite um numero :\n"))
for i in range(1, number + 1):
    if number % i == 0:
        divider += 1
if divider < 3:
    print(f"O numero {number} é primo")
else:
    print(f"O numero {number} não é primo")

# Maior peso e menor peso
maior = 0
menor = 101
for i in range(5):
    peso = random.randint(40, 100)
    maior = max(peso, maior)
    menor = min(peso, menor)


print(peso)

print(f"Menor peso: {menor}")
print(f"Maior peso: {maior}")

# Solicitar o sexo da pessoa

n = input("Digite seu gênero (M/F): ").upper()
while n not in ("M", "F"):
    n = input("Favor digitar seu gênero corretamente (M/F): ").upper()

print(f"Seu genero é {n}")

# Adivinhar um numero
numero = random.randint(0, 10)
escolha = int(input("Escolha um numero de 0 a 10 :"))
while escolha != numero:
    escolha = int(
        input(f"Você errou! O numero {escolha} não é o correto. Escolha outro")
    )

print(f"Parabêns você acertou e era o numero {numero} ")

number1 = float(input("Input one number"))
number2 = float(input("Other"))
opetion = -1
while opetion != 0:
    """
    1 SOMA
    2 MENOS
    3 MULTIPLICATION
    4 DIVISAO
    0 SAIR
    """
    opetion = input()
    match opetion:
        case "1":
            print(number1 + number2)
        case "2":
            print(number1 - number2)
        case "3":
            print(number1 * number2)
        case "4":
            print(number1 / number2)
        case "0":
            print("Leaving...")
        case _:
            print("Invalid option")

# Break and continue
for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(10):
    if i == 5:
        continue
    print(i)

# Contador de erros
counter = 0
n = 0
while n != 10:
    n = int(input("Digite um numero: "))
    if n != 10:
        counter += 1
    if counter == 10:
        print("Você digitou 10 números. O programa será encerrado.")
        break
print(f"Você digitou {counter} números antes de digitar 10.")


numbers = [10]
for i in range(1, 11):
    numbers.append(int(input()))
    if numbers[i] <= 0:
        numbers[i] = 1
    print(f"X[{i - 1}] = {numbers[i]}")

# Menu

opcoes = ["Soma", "Subtração", "Multiplicação", "Divisão", "Sair"]
n = 0
while n != 5:
    print("Escolha uma opção:")
    for i, opcao in enumerate(opcoes):
        print(f"{i + 1}. {opcao}")
    n = int(input())
    if n == 1:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        print(f"A soma é: {a + b}")
    elif n == 2:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        print(f"A subtração é: {a - b}")
    elif n == 3:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        print(f"A multiplicação é: {a * b}")
    elif n == 4:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        if b != 0:
            print(f"A divisão é: {a / b}")
        else:
            print("Não é possível dividir por zero.")
    elif n == 5:
        print("Saindo do programa...")
    else:
        print("Opção inválida. Tente novamente.")

# Contador de dias por idade

idade = int(input("Digite sua idade: "))
dias = idade * 365
print(f"Você já viveu aproximadamente {dias} dias.")

# Lista de filmes

filmes = []
n = 0
while n != 4:
    print("Escolha uma opção:")
    print("1. Adicionar filme")
    print("2. Listar filmes")
    print("3. Remover filme")
    print("4. Sair")
    n = int(input())
    if n == 1:
        filme = input("Digite o nome do filme: ")
        filmes.append(filme)
        print(f"Filme '{filme}' adicionado à lista.")
    elif n == 2:
        if len(filmes) == 0:
            print("Nenhum filme na lista.")
        else:
            print("Lista de filmes:")
            for i, filme in enumerate(filmes):
                print(f"{i + 1}. {filme}")
    elif n == 3:
        if len(filmes) == 0:
            print("Nenhum filme na lista para remover.")
        else:
            print("Lista de filmes:")
            for i, filme in enumerate(filmes):
                print(f"{i + 1}. {filme}")
            indice = int(input("Digite o número do filme que deseja remover: ")) - 1
            if 0 <= indice < len(filmes):
                removido = filmes.pop(indice)
                print(f"Filme '{removido}' removido da lista.")
            else:
                print("Número inválido.")
    elif n == 4:
        print("Saindo do programa...")
    else:
        print("Opção inválida. Tente novamente.")

# tuplas

pessoa1 = ("João", 25, "Masculino")
pessoa2 = ("Maria", 30, "Feminino")
print(f"Nome: {pessoa1[0]}")
print(f"Nome: {pessoa2[0]}")

# Mostrar quem tem a maior idade

if pessoa1[1] > pessoa2[1]:
    print(f"{pessoa1[0]} é mais velho(a) que {pessoa2[0]}.")
elif pessoa1[1] < pessoa2[1]:
    print(f"{pessoa2[0]} é mais velho(a) que {pessoa1[0]}.")
else:
    print(f"{pessoa1[0]} e {pessoa2[0]} têm a mesma idade.")

# Mostrar o numero por extenso
numeros = {
    0: "zero",
    1: "um",
    2: "dois",
    3: "três",
    4: "quatro",
    5: "cinco",
    6: "seis",
    7: "sete",
    8: "oito",
    9: "nove",
    10: "dez",
}
num = int(input("Digite um número de 0 a 10: "))
while num < 0 or num > 10:
    num = int(input("Número inválido. Digite um número de 0 a 10: "))
print(f"O número {num} por extenso é '{numeros[num]}'.")

# Gerar numeros aleatórios e armazenar em uma lista
numeros_aleatorios = []
for i in range(10):
    numeros_aleatorios.append(random.randint(1, 100))
print(f"Números aleatórios gerados: {numeros_aleatorios}")
print(f"Números aleatórios em ordem crescente: {sorted(numeros_aleatorios)}")

# Mostrar as vogais de uma tupla
tupla = {"Gabriel", "João", "Maria", "Ana", "Pedro"}
vogais = {"a", "e", "i", "o", "u"}
print(
    f"Vogais encontradas na tupla: {', '.join(vogais & {char for item in tupla for char in item.lower()})}"
)
for item in tupla:
    for char in item.lower():
        if char in vogais:
            print(char)

# Maior e menor valor em uma lista
# Index é usado para mostrar a posição do maior e menor valor na lista
valores = []
for i in range(5):
    valores.append(int(input(f"Digite o {i + 1}º valor: ")))
print(f"Você digitou os valores: {valores}")
print(
    f"O maior valor digitado foi {max(valores)} na posição {valores.index(max(valores))}."
)  # Exibe o maior valor e sua posição
print(
    f"O menor valor digitado foi {min(valores)} na posição {valores.index(min(valores))}."
)  # Exibe o menor valor e sua posição

# Verifica se o numero já foi digitado e se não foi, adiciona na lista
valores = []
for i in range(5):
    num = int(input(f"Digite o {i + 1}º valor: "))
    if num not in valores:
        valores.append(num)
print(f"Você digitou os valores: {valores}")

# Colocar os valores em ordem crescente sem usar sort() e sorted()
valores = []
for i in range(5):
    num = int(input(f"Digite o {i + 1}º valor: "))
    if i == 0 or num > valores[-1]:
        valores.append(num)
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                break
            pos += 1
print(f"Você digitou os valores: {valores}")

# Cadastrar pessoas com nome e idade em uma lista de listas
galera = []
escolha = "S"
while escolha == "S":
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    galera.append([nome, idade])
    escolha = input("Deseja continuar? [S/N] ").upper()

print(f"Você cadastrou {len(galera)} pessoas.")
# Verificar a pessoa mais pessada
if galera:
    maior_idade = max(galera, key=lambda x: x[1])[1]
    mais_velho = [p[0] for p in galera if p[1] == maior_idade]
    print(f"A pessoa mais velha tem {maior_idade} anos e é: {', '.join(mais_velho)}.")
# Matriz de 3x3 com numeros aleatorios
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(random.randint(1, 10))
    matriz.append(linha)
print("Matriz 3x3:")
for linha in matriz:
    print(linha)
# Soma de todos os valores pares da matriz
soma_pares = sum(num for linha in matriz for num in linha if num % 2 == 0)
print(f"A soma de todos os valores pares da matriz é: {soma_pares}")

# Soma de todos os valores da terceira coluna da matriz
soma_terceira_coluna = sum(linha[2] for linha in matriz)
print(
    f"A soma de todos os valores da terceira coluna da matriz é: {soma_terceira_coluna}"
)

# 4 Jogadores jogam um dado e tem resultados aleatórios.
# Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
jogadores = {}
for i in range(1, 5):
    jogadores[f"Jogador {i}"] = random.randint(1, 6)
print("Resultados dos jogadores:")
for jogador, resultado in jogadores.items():
    print(f"{jogador}: {resultado}")
jogadores_ordenados = sorted(jogadores.items(), key=lambda x: x[1], reverse=True)
