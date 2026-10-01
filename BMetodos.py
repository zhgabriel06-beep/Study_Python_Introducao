# Importa todas as funções do módulo math
#   import math 

# Importa apenas a função sqrt do módulo math
from math import sqrt
import random
import emoji




num = int(input('Digite um número: '))
raiz_quadrada = sqrt(num)
print(f'A raiz quadrada de {num} é {raiz_quadrada:.2f}.')
num = random.randint(1, 10)
print(num)

print(emoji_module.emojize('hello world :earth_americas:', use_aliases=True))

