# Laços de repetição em Python



for i in range(1, 11):
    print(f'{i} x 2 = {i * 2}')

# Contagem regressiva
for i in range(6, 0, -1):
    print(i)

i = int(input('Digite um número para o começo: '))
f = int(input('Digite um número para o fim: '))
p = int(input('Digite o passo: '))
for c in range(i, f + 1, p):
    print(c)

# Soma
for c in range(1, 6):
    soma +=c
print (f'A soma dos números digitados é {soma}.')

# Matriz de 3x3
for i in range(1, 4):
    for j in range(1, 4):
        print(f'[{i}, {j}]', end=' ')


# While

c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')
