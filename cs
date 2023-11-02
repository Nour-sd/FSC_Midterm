students=[]

def get_student_ID():
    ID=int(input('Enter the student ID you want to search for '))
    result = [n for n in students if ID == n["ID"]]
    print(result)

def get_all_students():
    print ("All Students")
    for i, v in enumerate (students):
        print ('Student',v['ID'],'Name: ',v['name'],' Age: ',v['age'],' Magor: ',v
               ['magor'],' GPA: ',v['GPA'])
        
def get_student_by_magor():
    magor = input("Enter the major of the student you are looking for ")
    result = [s for s in students if magor == s['magor']]
    print("\nStudents with this major")
    for r in result :
        print(r)

def add_student():
    student = {}
    student["name"] = input("Enter Student Name ")
    student["age"] = int(input("Enter Student Age "))
    student["magor"] = input("Enter Student Major ")
    student["GPA"] = float(input("Enter Student GPA "))
    student["ID"] = len(students)+1
    students.append(student)

def find_common_magor():
    b=0

    
       
def delete_student():
    del_ID = int(input("Enter the ID of the student you want to delete"))
    global students
    students=[x for x in students if x['ID']!=del_ID]

def calculate_avarage_GPA():
    total_sum = 0
    count = len(students)
    for student in students:
        total_sum += student['GPA']
    avg = total_sum /count
    print("Average GPA is ",avg)

def get_top_performance():
     top_performance = max(students['GPA'])
     result = [z for z in students if top_performance == z['GPA']]
     print("\ntop performance")
     for m in result :
        print(m)
    

while True:
    print("\nMenu")
    print("1.Get all students")
    print("2.Search by student ID")
    print("3.Add a student")
    print("4.Delete a student")
    print("5.Find common magor")
    print("6.Calculate average GPA")
    print("7.find student by magor")
    print("8.get top performers")
    print("9.Exit")
    choice = int(input('\nEnter your choice :'))
    if choice == 1:
        get_all_students()
    elif choice == 2:
        get_student_ID()
    elif choice == 3:
        add_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        find_common_magor()
    elif choice == 6:
        calculate_avarage_GPA()
    elif choice == 7:
        get_student_by_magor()
    elif choice == 8:
        get_top_performance()
    elif choice == 9:
        break
else:
    print("InvalID Choice! Please enter again.")
        
