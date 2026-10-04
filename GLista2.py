# Lista dentro de Lista
pessoas = [["João", 25], ["Maria", 30], ["Pedro", 20]]
# Acessing elements of the list
print(pessoas[0][0])  # Acesses the name of the first person
print(pessoas[1][1])  # Acesses the age of the second person
print(pessoas[1])  # Acesses the list of the second person

teste = list()
teste.append("Gustavo")
teste.append(40)
galera = list()
galera.append(teste[:])  # to add a copy of the 'teste' list to the 'galera' list
teste[0] = "Maria"
teste[1] = 22
galera.append(teste[:])  # Adds a copy of the 'teste' list to the 'galera' list
print(galera)  # Displays the 'galera' list with the information of the people
galera = [["João", 25], ["Maria", 30], ["Pedro", 20]]
print(galera)  # Displays the 'galera' list with the information of the people
galera = list()
dado = list()
for c in range(0, 4):
    dado.append(str(input("Nome: ")))  # Solicits the name of the person
    dado.append(int(input("Idade: ")))  # Solicits the age of the person
    galera.append(dado[:])  # Adds a copy of the 'dado' list to the 'galera' list
    dado.clear()  # Clears the 'dado' list for the next iteration
print(galera)  # Displays the 'galera' list with the information of the people
