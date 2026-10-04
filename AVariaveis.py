# Atribuindo valor nas variaveis
nome = "Gabriel"
idade = 19
peso = 87.3

# Pedindo para o usuario colocar valor nas variaveis
nome1 = str(input("Type your name: "))
idade2 = int(input("Type your age: "))
peso2 = float(input("Type your weight: "))
print(f"Name: {nome1}, Age: {idade2}, Weight: {peso2}")


nome3 = str(input("Type your name: "))
print(f"Hello, {nome3}! Welcome to our program.")

# Data of birth
dia = int(input("Type the day of your birth: "))
mes = int(input("Type the month of your birth: "))
ano = int(input("Type the year of your birth: "))
print(f"You were born on {dia}/{mes}/{ano}.")

# Soma
numero1 = int(input("Type the first number: "))
numero2 = int(input("Type the second number: "))
soma = numero1 + numero2
print(f"The sum of {numero1} and {numero2} is equal to {soma}.")


n = input("Type something: ")
print(n.isnumeric())  # Verifies if it is a number
print(n.isalpha())  # Verifies if it is a letter
print(n.isalnum())  # Verifies if it is alphanumeric
print(n.isupper())  # Verifies if it is uppercase
print(n.islower())  # Verifies if it is lowercase


number1 = int(input("Type a number: "))

print(
    f"The number entered was {number1} and its predecessor is {number1 - 1} and its successor is {number1 + 1}."
)

# Multiplication Table

number2 = int(input("Type another number: "))
print(f"The multiplication table of {number2} is:")
for i in range(1, 11):
    print(f"{number2} x {i} = {number2 * i}")

# Converter em dollar
number3 = float(input("Type a value in reais: "))
if number3 < 0:
    print("Invalid value. Please enter a positive value.")
else:
    dollar = number3 / 5.25
    print(f"The value of R${number3:.2f} converted to dollars is: ${dollar:.2f}")

#  Calcula area de uma parede e quantidade de tinta necessária para pintar a parede
largura = float(input("Type the width of the wall in meters: "))
comprimento = float(input("Type the length of the wall in meters: "))
area = largura * comprimento
# Quantidade de tinta necessária (1 litro pinta 2m²)
tinta_necessaria = area / 2
print(
    f"The area of the wall is {area:.2f} m² and the quantity of paint needed to paint the wall is {tinta_necessaria:.2f} liters."
)
