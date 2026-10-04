# Condicionais em Python
n1 = float(input("Type the first grade: "))
n2 = float(input("Type the second grade: "))
media = (n1 + n2) / 2
if media >= 7:
    print(f"Your average was {media:.2f}. Congratulations, you were approved!")
else:
    print(f"Your average was {media:.2f}. Unfortunately, you were failed.")
