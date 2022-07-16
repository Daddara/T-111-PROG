def calculate_sum():
    
    try:
        value = int(input("Enter value for n: "))
        result = 1
        for i in range(1, value+1):
            result=result+i
        print("The result is:", result-1)
    except ValueError:
        None
        
def calculate_product():
    
    try:
        value = int(input("Enter value for n: "))
        result = 1
        for i in range(1, value+1):
            result=result*i
        print("The result is:", result)
    except ValueError:
        None

def instructions():
    print("1: Compute the sum of 1..n")
    print("2: Compute the product of 1..n")
    print("9: Quit")

    try:
        choice = int(input("Choice: "))
        return choice
    except ValueError:
        None

def main():
    
    while True: 
        answer = instructions()
        if answer == int(1):
            calculate_sum()
        elif answer == int(2):
            calculate_product()
        elif answer==int(9):
            quit()

main()