# Condicionais em Python
n1 = flot(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media >= 7:
    print(f'Sua média foi {media:.2f}. Parabéns, você foi aprovado!')
else:
    print(f'Sua média foi {media:.2f}. Infelizmente, você foi reprovado.')
    