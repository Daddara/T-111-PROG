def process_all_files(files):
    for file in files:
        file_name = check_files(file)
        if file_name != None: 
            new_list = make_list(file_name)
            seq = file_sequence(new_list)
            c_sum = cumulative_sum(new_list)
            sort = sorted_sequence(new_list)
            med = median(new_list)
            print_data(seq,c_sum,sort,med,file)

def check_files(file_name):
    '''try to open file otherwise throws an error'''
    try:
        data_file = open(file_name, "r")
        return data_file
    except FileNotFoundError:
        print()
        print("File",file_name, "not found")
        return None


def make_list(file_name):
    '''creates the lists from open files'''
    new_str = ''
    temp_list = []
    for i in file_name:
        no_newline = i.replace('\n','')
        no_newline = ''.join(no_newline.split())
        if no_newline.replace('.', '').replace('-','').isdigit():

            new_str = (str(round(float(no_newline),1))+ ' ') 
            temp_list.append(float(new_str))
    
    return temp_list

def file_sequence(file_list):
    '''sequence funciton that returns new_str of numbers'''
    new_str = ''
    for i in file_list:
        new_str += (str(i)+ ' ')
    
    return new_str

def cumulative_sum(file_list):
    '''calculates the cumulative sum of opened file'''
    new_str = ''
    c_sum = 0
    for i in file_list:
        c_sum += i
        new_str += (str(round(float(c_sum),1))+ ' ')
    return new_str

def sorted_sequence(file_list):
    '''sorst the numbers in openeded files'''
    new_str = ''
    file_list.sort()
    for i in file_list:
        new_str += (str(i)+' ')
    return new_str

def median(file_list):
    '''calculates the median number of number list'''
    file_count = len(file_list)
    if file_count == 0:
        return 
    
    if file_count % 2 == 0:
        median1 = file_list[file_count//2]
        median2 = file_list[file_count//2 - 1]
        median = (median1 + median2)/2
    else:
        median = file_list[file_count//2]
    return median

def print_data(seq,c_sum,sort,med,file):
    print()
    print("File",file)
    print("\tSequence:")
    print('\t\t{:<1}'.format(seq))
    print('\tCumulative sum:')
    print('\t\t{:<1}'.format(c_sum))
    print('\tSorted sequence:')
    print('\t\t{:<1}'.format(sort))
    print('\tMedian:')
    '''prints out correct number of floating points'''
    if med != None: # med returns the len of list, if len is 0 it returns none
        if str(med) == str(med).rstrip('0'):
            if len(str(med).split('.')[1]) > 2:
                print('\t\t{:.2f}'.format(med))
            else:
                print('\t\t{}'.format(med))
        else:
            new_med = float(str(med).rstrip('0'))
            print('\t\t{:.1f}'.format(new_med))

# Main program starts here
filename_list = input("Enter filenames: ").split()
process_all_files(filename_list)