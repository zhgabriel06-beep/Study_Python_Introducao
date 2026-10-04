# Laços de repetição em Python


for i in range(1, 11):
    print(f"{i} x 2 = {i * 2}")

# Contagem regressiva
for i in range(6, 0, -1):
    print(i)

i = int(input("Type a number for the start: "))
f = int(input("Type a number for the end: "))
p = int(input("Type the step: "))
for c in range(i, f + 1, p):
    print(c)

# Soma
soma = 0
for c in range(1, 6):
    soma += c
print(f"The sum of the entered numbers is {soma}.")

# Matriz de 3x3
for i in range(1, 4):
    for j in range(1, 4):
        print(f"[{i}, {j}]", end=" ")


# While

c = 1
while c < 10:
    print(c)
    c += 1
print("End of the loop.")
