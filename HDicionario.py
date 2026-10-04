# Dicionario em python
dados = dict()  # Create a call for an empty dictionary
dados["name"] = str(
    input("type your name: ")
)  # adding the "name" key with the value entered by the user
dados["age"] = int(
    input("type your age: "))
# adding the "age" key with the value entered by the user
print(dados)  # Displays the complete dictionary
print(
    f"O {dados['name']} tem {dados['age']} anos."
)  # Access the values of the "name" and "age" keys in the dictionary
dados["gender"] = str(
    input("type your gender (M/F): ")
)  # Add the "gender" key with the value entered by the user
print(dados)  # Display the complete dictionary after adding the key

filme = {
    "title": "Star Wars",
    "year": 1977,
    "director": "George Lucas",
}  # Create a dictionary called "filme" with some keys and values
print(filme)  # Display the complete dictionary
print(filme.values())  # Display the values of the dictionary
print(filme.keys())  # Display the keys of the dictionary
print(filme.items())  # Display the items (key-value pairs) of the dictionary

for k, v in filme.items():
    print(f"O {k} é {v}")  # Iterates over the dictionary items and prints a message.

pessoas = {"Name": "Gabriel", "Gender": "M", "Age": 19}
print(pessoas)
del pessoas["Gender"]  # Remove a keys "gender" do dicionário
print(pessoas)
estado = dict()
brasil = list()

for c in range(4):
    estado["UF"] = input("Unidade Federativa")
    estado["Sigla"] = input("Sigla do Estado")
    brasil.append(estado.copy())
print(brasil)
