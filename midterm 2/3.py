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
    
def main():
    '''opens and prints the file. If file is not found an message is sent out'''
    filename = input("Enter file name: ")
    baby_names = open_read_file(filename)
    if baby_names:
        print(baby_names[:2])
    else:
        print(f"File {filename} not found")
main()