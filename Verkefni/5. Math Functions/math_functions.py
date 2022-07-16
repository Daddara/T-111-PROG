import math

def sum_natural(n_str):
    '''returns the sum of the first n numbers'''
    sum_of_num = 0
    if n_str >= 2:
        for number in range(0, n_str+1):
            sum_of_num += number
        print(f"Natural number sum: {sum_of_num}")  
    else:
        return None

def sum_fibonacci(n_str):
    '''returns the sum of the first n fibonacci numbers'''
    if n_str >= 2:
        
        fibo_num_1 = 0
        fibo_num_2 = 1
        counter = 0
        
        while counter < n_str:
            sum_of_num = 0
            next_num = fibo_num_1+fibo_num_2
            fibo_num_1 = fibo_num_2
            fibo_num_2 = next_num
            counter+=1
            sum_of_num+=next_num-1
            
        print(f"Fibonacci sum: {sum_of_num}")
    else:
        return None

def sum_approximate_euler(n_str):
    '''returns Euler approximation with five floating numbers'''
    sum_of_num=0
    if n_str >= 2:
        for number in range(0,n_str):
            sum_of_num += (1/math.factorial(number)) 
        if str(sum_of_num)[2::] == '0':
            print(f"Euler approximation: {sum_of_num:.1f}")
        else:
            print(f"Euler approximation: {sum_of_num:.5f}")
    else:
        return None
  
def display_instructions():
    '''instructions for the program'''
    print("Please choose one of the options below:")
    print("a. Display the sum of the first N natural numbers.")
    print("b. Display the sum of the first N Fibonacci numbers.")
    print("c. Display the approximate value of e using N terms.")
    print("x. Exit from the program.")
    
def calculations(category_choice, number_choice):
    '''inputs N number into right calculation category'''
    if category_choice == "a":
        sum_natural(number_choice)
    elif category_choice == "b":
        sum_fibonacci(number_choice)
    elif category_choice == "c":
        sum_approximate_euler(number_choice)
        
def read_category_choice():
    category_choice = input("\nEnter option: ")
    
    return category_choice

def main():

    valid_char = "a","b","c"
    display_instructions()
    category_choice = read_category_choice()
    
    while category_choice in valid_char:
        number_choice_str = input("Enter N: ")   
        '''Raise error if choice is not a number or is a string'''
        if not number_choice_str.isnumeric() or int(number_choice_str) < 2:
            print(f"Error: {number_choice_str} was not a valid number.")
        else:
            number_choice = int(number_choice_str)
            calculations(category_choice, number_choice)
        
        category_choice = read_category_choice()

    if category_choice == "x":
        quit()
    else:
        print (f"Unrecognized option {category_choice}")
        main()
        
main()