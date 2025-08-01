data =  []

def add_employee():
    name = input("enter employee name: ")
    mail = input("enter employee mail: ")
    role = input("enter employee role: ")

    employee = {"emp_name":name,
                "emp_mail":mail,
                "emp_role":role}
    return employee


def data_display(data):
    for i, employee in enumerate(data):
        print(i+1,":", employee["emp_name"], "---", employee["emp_role"])

    
def delete_employee(data):
    data_display(data)

    number = input("enter employee who's data is to be deleted: ")
    while True:
        try:
            number = int(number)
            if number <= 0 or number > len(data):
                print("Invalid number i.e. out of range")
            else:
                break
        except:
            print("invalid number")

    data.pop(number-1)


def search_employee(data):
    results = []
    search = input("search employee name: ")


    for employee in data:
        name = employee["emp_name"]

        if search in name.lower():
            results.append(employee)
        else:
            pass

    data_display(results)


print("\nwelcome to employee database management system!!")

while True:
    task = input("you'd like 'search', 'add', 'delete' or 'quit'? ").lower()
    if task == "add":
        employee = add_employee()
        data.append(employee)
        print("Employee data added!")
        

    elif task == "search":
        search_employee(data)

    elif task == "delete":
        delete_employee(data)

    elif task == "quit":
        break
    else:
        print("invalid operation!")
