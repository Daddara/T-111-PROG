
choice = (input("Input f|a|b (fibonacci, abundant or both): "))

if choice == ("f") or choice == ("b"):
    
    '''prints out fibonacci sequence based on input'''

    length_sequence = int(input("Input the length of the sequence: "))

    print("Fibonacci Sequence:")
    print ("-------------------")
    
    first_num = 0
    second_num = 1
    print(first_num)
    print(second_num)

    for i in range(2,length_sequence):
        new_num = (first_num+second_num)
        print(new_num)
        first_num = second_num
        second_num = new_num
        
if choice == ("a") or choice == ("b"):
    
    '''prints out abundant based on input'''

    max_number = int(input("Input the max number to check: "))
    
    print("Abundant numbers:")
    print ("-----------------")
    
    total = 0
    
    for i in range(1, max_number+1):
        for j in range(1, i):
            if (i%j==0):
                total+=j
        if (total > i):
            print(i)
        total = 0
                   
else:
    quit()

        

