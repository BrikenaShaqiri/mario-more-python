from cs50 import get_int

while True:
    n = get_int("Height: ")
    if n >= 1 and n <= 8:
        break


for i in range(n):
    # Printimi i hapeisrave ne anen e majte
    for j in range(n - i - 1):
        print(" ", end="")

    # Printimi i hashave ne anen e majte
    for k in range(i + 1):
        print("#", end="")

    # Shtimi i hapesira mes dy piramidave
    print("  ", end="")

    # Printimi i hasheve ne anen e djathte
    for l in range(i + 1):
        print("#", end="")

    # Dalja ne rresht te ri
    print()
