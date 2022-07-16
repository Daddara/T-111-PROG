#les skjal 1
#les skjal 2
#reiknar lokaeinkunn miðað við vægi
#prentar skjöl

def open_file(filename):
    try:
        file_stream = open(filename, "r")
        return file_stream
    except FileNotFoundError:
        return None
    
def process_file(file):
    
    print ([item.strip() for item in file])
    
def process_course_info(value):
    pass
    
    #grade_list = []
    #student_list = []
    
    #for item in value:
    #    student_list.append(value[0],item)
    #    grade_list.append(value[1])
        
        #print (item)
        #if item == float:
        #    grade_list.append(item)
        #else:
        #    student_list.append(item)
    
    #print (student_list)
    #print (grade_list)
    #print (values)
    
    
        
def process_student_info(student):
    pass

def print_info():
    pass
        

# Main program starts here
file_name = input("Enter filename for parts: ")
file_object = open_file(file_name)
if file_object:
    file_items = process_file(file_object)
    course_info = process_course_info(file_items)
    #student_items = process_file(file_items)
    #print_info(course_items, student_items)
else:
    print(f"File {file_name} not found")