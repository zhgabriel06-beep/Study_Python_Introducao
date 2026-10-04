# Create a list called "lanche" with some elements
lanche = ["hambúrguer", "suco", "pizza", "pudim"]
print(lanche[1])  # Access the element at position 1 of the list
lanche[1] = "refrigerante"  # Change the element at position 1 of the list
print(lanche[1])  # Access the element at position 1 of the list after the change
lanche.append("batata frita")  # Add an element to the end of the list
print(lanche)  # Display the complete list
print(lanche[-1])  # Access the last element of the list
lanche.insert(0, "cachorro-quente")  # Insert an element at position 0 of the list
print(lanche)  # Display the complete list after the insertion
lanche.pop()  # Remove the last element of the list
lanche.remove("pizza")  # Remove the element "pizza" from the list
print(lanche)  # Display the complete list after the removals
valores = list(range(4, 11))
print(valores)

num = [2, 5, 9, 1]
num[2] = 3  # Change the element at position 2 of the list
num.append(7)  # Add the element 7 to the end of the list
num.sort()  # Sort the list in ascending order
num.sort(reverse=True)  # Sort the list in descending order
print(num)  # Display the complete list after the changes


valores = []
valores.append(5)  # Add the element 5 to the list
valores.append(9)  # Add the element 9 to the list
valores.append(4)  # Add the element 4 to the list
for c, v in enumerate(valores):  # Iterate over the list with index and value
    print(f"At position {c} I found the value {v}!")  # Display the position and value
print(
    f"I reached the end of the list."
)  # Display message indicating the end of the list

a = [2, 3, 4, 7]
b = a  # Assign the list 'a' to the variable 'b'
b[2] = 8  # Change the element at position 2 of the list
print(f"List A: {a}")  # Display the list 'a' after the change
print(f"List B: {b}")  # Display the list 'b' after the change

a = [2, 3, 4, 7]
b = a[:]  # Create a copy of the list 'a' and assign it to the variable 'b'
b[2] = 8  # Change the element at position 2 of the list 'b'
print(f"List A: {a}")  # Display the list 'a' after the change
print(f"List B: {b}")  # Display the list 'b' after the change
