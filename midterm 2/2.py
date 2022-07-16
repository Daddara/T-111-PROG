def open_read_file(filename):
    '''opens the file and sorts each line to seperate lists'''
    try:
        file_object = open(filename, "r")
        word_list = []
        for line in file_object:
            babies = line.strip().split()
            word_list.append(babies)
        return word_list
    except FileNotFoundError:
        return None
    
def get_male(male_list):
    '''arranges all men into seperate lists with single names and frequency'''
    new_male_list = []
    for item in male_list:
        new_male_list.append(item[1:3])
    return new_male_list

def get_female(female_list):
    '''arranges all men into seperate lists with single names and frequency'''
    new_female_list = []
    for item in female_list:
        new_female_list.append(item[3:5])
        
    return new_female_list
    
def frequency_counter(counter):
    '''supposed to find the number of every single name in list but doesn't work'''
    total_men = 0
    total_female = 0
    
    for num in counter:
        total_men+=num
        
    for num in counter:
        total_men+=num
    
    print(f"Total frequency of boy names: {total_men}")
    print(f"Total frequency of girl names: {total_femail}")
    
def main():
    '''opens and prints the file. If file is not found an message is sent out'''
    filename = input("Enter file name: ")
    baby_names = open_read_file(filename)
    if baby_names:
        print(baby_names[:2])
        male_list = get_male(baby_names)
        print(male_list[:5])
        female_list = get_female(baby_names)
        print(female_list[:5])
        #frequency_counter(baby_names) #this function doesn't work :(
        
    else:
        print(f"File {filename} not found")
main()
