# Importa todas as funções do módulo math
#   import math

# Importa apenas a função sqrt do módulo math
from math import sqrt
import random

num = int(input("Type a number: "))
raiz_quadrada = sqrt(num)
print(f"The square root of {num} is {raiz_quadrada:.2f}.")
num = random.randint(1, 10)
print(num)

# Metodos do módulo math
max(1, 2, 3, 4, 5)  # Retorna o maior valor
min(1, 2, 3, 4, 5)  # Retorna o menor valor
abs(-5)  # Retorna o valor absoluto

# Metodos do módulo random
random.randint(1, 10)  # Retorna um número inteiro aleatório entre 1 e 10
random.choice([1, 2, 3, 4, 5])  # Retorna um elemento aleatório da lista
random.shuffle([1, 2, 3, 4, 5])  # Embaralha a lista


print(emoji.emojize("hello world :earth_americas:", use_aliases=True))
