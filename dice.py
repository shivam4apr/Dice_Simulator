import random
a="y"
while a=="y":
    x = random.randint(1, 6)
    if x == 1:
        print("--------")
        print("|      |")
        print("|  O   |")
        print("|      |")
        print("--------")
    elif x == 2:
        print("--------")
        print("|      |")
        print("|  O O |")
        print("|      |")
        print("--------")
    elif x == 3:
        print("---------")
        print("|       |")
        print("| O O O |")
        print("|       |")
        print("---------")
    elif x == 4:
        print("--------")
        print("| O  O |")
        print("|      |")
        print("| O  O |")
        print("--------")
    elif x == 5:
        print("--------")
        print("|O    O|")
        print("|   O  |")
        print("|O    O|")
        print("--------")
    else:
        print("---------")
        print("| O O O |")
        print("|       |")
        print("| O O O |")
        print("---------")
    a=input("Press Y to roll again")
