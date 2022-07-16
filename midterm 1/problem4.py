max_integer = int(input("Input max integer: "))

for i in range(0, max_integer):
    for j in range(0, i+1):
        print(j+1, end=" ")
    print()