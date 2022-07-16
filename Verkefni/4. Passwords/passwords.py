
PASS_MAX_LENGTH = 20
PASS_MIN_LENGTH = 6

count_valid = 0
count_invalid = 0
sum_int = 0

new_pass = (input("Enter a new password: "))

while new_pass != "q":
    
    if PASS_MIN_LENGTH <= len(new_pass) <= PASS_MAX_LENGTH:
    
        '''varibles set to False by default'''
        uppercase = False
        lowercase = False
        digits = False
      
        for item in new_pass:
            '''if item found in string it will return True'''
            if item.isupper():
                uppercase = True
            if item.isdigit():
                digits = True
            if item.islower():
                lowercase = True
    
        '''if every task is set to True'''
        if uppercase and lowercase and digits:
            count_valid += 1
            sum_int += 1
            print(f"Valid password of length {len(new_pass)}")
        else:
            count_invalid += 1
            sum_int += 1

        if lowercase == False:
            print("At least one lower case letter needed")
        if uppercase == False:
            print("At least one upper case letter needed")
        if digits == False:
            print("At least one number needed")  
            
    else:                
        print("Invalid length")
        count_invalid += 1
        sum_int += 1
        
    new_pass = (input("Enter a new password: "))

if new_pass == "q":
    print(f"You tried {sum_int} passwords, {count_valid} valid, {count_invalid} invalid")

        

        

    

    


