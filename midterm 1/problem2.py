dog_age = int(input("Input dog's age: ")) # Do not change this line

if dog_age > 0 and dog_age <= 16:
    '''calculates human age'''
    human_age = 0
    if dog_age == 1:
        human_age += 15
    else:
        human_age = (dog_age+4)*4
    print ("Human age: ", human_age) 
else:
    print ("Invalid age")