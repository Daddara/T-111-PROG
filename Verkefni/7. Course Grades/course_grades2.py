def main():
    try:
        filename_parts = input('Enter filename for parts: ')
        fileobj_parts = open(filename_parts)
        parts_list = make_parts_list(fileobj_parts)
        print(parts_list)
    except FileNotFoundError:
        print ("File {} not found".format(filename_parts))

    try:
        filename_grades = input('Enter filename for grades: ')
        fileobj_grades = open(filename_grades)
        grades_list = make_grade_list(fileobj_grades)
        print(grades_list)
    except FileNotFoundError:
        print ("File {} not found".format(filename_grades))

    print_result(parts_list,grades_list)

def make_parts_list(partsobj):
    list_a = []
    counter = 0 
    final_list = []
    temp = []

#Create a list
    for line in partsobj:
        list_a.append(line.strip().split())
#Split list into names and number
    names = list_a[0]
    number = list_a[1]
#Make sure that numbers are not string
    for n in number:
        temp.append(float(n))
#Create a tuple and add to an empty list(final_list)
    for word in names:
        bla = tuple((word,temp[counter]))
        final_list.append(bla)
        counter += 1
    return (final_list)

def make_grade_list(gradesobj):
    list_a = []
    students = []
    grades = []
    final_list = []
#Make a list
    for line in gradesobj:
        list_a.append(line.strip().split())
#Create a new list and split to students and grades, Make sure that grades are numbers and not string
#Create a tuple with students and grades and add to a list
    counter = 0
    for i in list_a:
        new_list = list_a[counter]
        students = new_list.pop(0)
        grades = []
        for i in new_list:
            grades.append(float(i))
        grades_tupe = (students,grades)
        final_list.append(grades_tupe)

        counter+=1

    return final_list

def calculate_grade():
    pass

def print_result(parts,grades):
    print()
    student_ID = ("Student ID",0.0)
    course_grade = ("Course grade",0.0)
    parts.insert(0,student_ID)
    parts.append(course_grade)
    for i in parts:
        print ((i[0])+' ',end='')
    print()
    for i in grades:
        print(i)
    
    


main()