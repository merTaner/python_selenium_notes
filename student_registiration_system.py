student_list = []

def add_student():
    student_name_surname = input('student name - surname : ').lower()
    student_list.append(student_name_surname)

    print(f'{student_list[-1]} added student to list. \n')

def delete_student():
    deleted_student = input('Name and surname of the student you want to delete : ').lower()
    print(f'{deleted_student} removed from list.')
    student_list.remove(deleted_student)

def show_student_list():
    print('Student List'.center(20, '-'))

    for student in student_list:
        print(student)

def show_student_number():
    global student_list

    student = input('Name and surname of the student whose number you want to know : ').lower()
    student_list_lenght = len(student_list)

    for student_no in range(student_list_lenght):
        if student == student_list[student_no]:
            print(f"{student} student's number : {int(student_list.index(student)) + 1}")                
        else:
            print("That item does not exist")
            

def menu():
    print(' Welcome Student Register System '.center(50, '*') + '\n')
    
    option = None
    while option != 5:
        print(' What want to do? '.center(50, '-'))    
        print(
        ''' 
            1 - Add Student
            2 - Delete Student
            3 - Show Student List
            4 - Learn Student Number
            5 - Quit
        ''')
        option = int(input())

        match option:
            case 1:
                add_student()
            case 2:
                delete_student()
            case 3:
                show_student_list()
            case 4:
                show_student_number()
            case 5:
                print('Please select a valid transaction !')


if __name__ == '__main__':
    menu()