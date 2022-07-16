number_to_multiply = int(input("Input number to multiply: ")) # Do not change this line
how_often = int(input("Input how often to multiply: ")) # Do not change this line

sum_num = 0 

for i in range(1, how_often+1):
    sum_num += number_to_multiply
    
    print(sum_num)
