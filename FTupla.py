from tokenize import PseudoExtras


lanche = (
    "hambúrguer",
    "juice",
    "pizza",
    "pudding",
)  #  one tupla called "lanche" with some elements
print(lanche[1])  # Acesses the element at index 1 of the tuple
# lanche[1] = "refrigerante"  # This would cause an error, as tuples are immutable
# print(lanche[1])  # Acesses the element at index 1 of the tuple after the modification
# lanche.append("batata frita")  # Adds an element to the end of the tuple
# print(lanche)  # Displays the complete tuple
print(lanche[-1])  # Acesses the last element of the tuple

for c in lanche:
    print(
        f"I am eating {c}"
    )  # Iterates over each element of the tuple and prints a message

# Show the first 4 elements of the tuple
tupla = ("Gabriel", "João", "Maria", "Ana", "Pedro")
print(tupla[:4])  # Accesses the elements from index 0 to index 3 (exclusive)

for pos, comida in enumerate(lanche):
    print(
        f"I am cooking {comida} in position {pos}"
    )  # Iterates over the tuple with index and value

print(
    sorted(lanche)
)  # Displays the tuple in alphabetical order without changing the original tuple
