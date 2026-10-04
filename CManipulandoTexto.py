# Manipulando texto em Python

frase = "Python is a programming language incredible!"
print(frase.upper())  # Converte para maiúsculas
print(frase.lower())  # Converte para minúsculas
print(frase.title())  # Converte para título (primeira letra maiúscula)
print(frase.capitalize())  # Converte a primeira letra da frase para maiúscula
print(frase.strip())  # Remove espaços em branco no início e no final da frase
print(frase.lstrip())  # Remove espaços em branco à esquerda da frase
print(frase.rstrip())  # Remove espaços em branco à direita da frase
print(frase.replace("incredible", "fantastic"))  # Substitui uma palavra
print(frase.split())  # Divide a frase em uma lista de palavras
print(frase[0:6])  # Acessa uma parte da frase (fatiamento)
print(len(frase))  # Retorna o tamanho da frase
print(frase[15:20])  # Acessa a partir do índice 15 até o índice 20
print(
    frase[0::2]
)  # Acessa a cada 2 caracteres da frase e corrige o erro de sintaxe no final da linha.
print(
    frase.count("a", 0, 20)
)  # Conta quantas vezes a letra 'a' aparece na frase, entre os índices 0 e 20
print("Python" in frase)  # Verifica se a palavra "Python" está na frase
print("-".join(frase))  # Junta a frase com o caractere "-" entre cada letra
