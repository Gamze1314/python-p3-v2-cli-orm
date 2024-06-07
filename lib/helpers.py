from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
# this function will get all departments stored in the database, then print each department on a new line. 
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    #should prompt for a name , fid the Department instance that matches, and print the matching object's data or en error message.
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')



def create_department():
    #should prompt for a name, and location
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    ##create and persist new department instance, handle exception
    try:
        department = Department.create(name, location)
        print(f'Success : {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    pass


def find_employee_by_name():
    pass


def find_employee_by_id():
    pass


def create_employee():
    pass


def update_employee():
    pass


def delete_employee():
    pass


def list_department_employees():
    pass