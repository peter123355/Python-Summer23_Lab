import os

TEMP_FILE = "C:/Users/peter/OneDrive/Desktop/Labs/New folder/la 5/temp.txt"

def printEmp(employee):
    if len(employee) >= 4:
        first_name = employee[0]
        last_name = employee[1]
        try:
            rate = float(employee[2])
            hours = float(employee[3])
            overtime_pay = calculate_overtime(rate, hours)
            gross_pay = rate * hours + overtime_pay
            print(f"{first_name} {last_name} - Gross Pay: {gross_pay:.2f}")
        except ValueError:
            print(f"Invalid data for employee: {' '.join(employee)}")
    elif len(employee) > 0:
        print(f"Invalid employee record format: {' '.join(employee)}")
    else:
        print("Invalid employee record format.")




def calculate_overtime(rate, hours):
    regular_hours = 40.0
    if hours > regular_hours:
        overtime_hours = hours - regular_hours
        overtime_pay = overtime_hours * rate * 0.5
        return overtime_pay
    else:
        return 0.0


def addEmp(file_path, employees):
    with open(file_path, 'a') as file:
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        rate_of_pay = input("Enter rate of pay: ")
        hours_worked = input("Enter hours worked: ")
        record = f"{first_name} {last_name} {rate_of_pay} {hours_worked}\n"

        found = False
        for employee in employees:
            if isinstance(employee, str):  # Check if the employee is a string
                employee_data = employee.split()  # Split the employee record into individual elements
                if len(employee_data) >= 2 and employee_data[0] == first_name and employee_data[1] == last_name:
                    found = True
                    break

        if found:
            print("Employee record already exists.")
        else:
            file.write(record)
            employees.append(record.strip().split())  # Split the record and append individual elements
            print("Employee record added.")

def findEmployeeByName(employees, name):
    for employee in employees:
        if name == f"{employee[0]} {employee[1]}":
            return employee
    return None


def writeEmployees(file_path, employees):
    with open(file_path, "w") as empFile:
        for employee in employees:
            empFile.write(" ".join(employee) + "\n")

def exitApp():
    print("Exiting the program.")
    exit()

def deleteEmp(file_path, employees):
    name = input("Enter a name to delete employee: ")
    found_employee = None
    deleted = False

    with open(file_path, "r") as file, open(TEMP_FILE, "w") as temp_file:
        while True:
            line = file.readline()
            if not line:
                break

            employee = line.strip().split()
            if f"{employee[0]} {employee[1]}" != name:
                temp_file.write(" ".join(employee) + "\n")
            else:
                found_employee = employee
                deleted = True

    if found_employee is not None:
        os.remove(file_path)
        os.rename(TEMP_FILE, file_path)
        employees.remove(found_employee)
        print("Employee record deleted successfully.")
    elif deleted:
        print("Employee not found.")
    else:
        print("No employees found.")
def printAll(employees, calculate_gross_pay):
    if employees:
        for employee in employees:
            printEmp(employee)
    else:
        print("No employees found.")

        
def modifyEmp(file_path, employees):
    name = input("Enter a name to modify employee: ")
    found = False

    with open(file_path, "r") as file, open(TEMP_FILE, "w") as temp_file:
        for line in file:
            employee = line.strip().split()
            if f"{employee[0]} {employee[1]}" == name:
                print("Employee found. Modifying details...")
                first_name = input("Enter new first name: ")
                last_name = input("Enter new last name: ")
                rate = float(input("Enter new rate of pay: "))
                hours = float(input("Enter new hours worked: "))
                employee[0] = first_name
                employee[1] = last_name
                employee[2] = str(rate)
                employee[3] = str(hours)
                found = True
            temp_file.write(" ".join(employee) + "\n")

    if found:
        os.remove(file_path)
        os.rename(TEMP_FILE, file_path)
        print("Employee details modified.")
        # Update the employees list with the modified employee data
        employees.clear()
        employees.extend(readEmployees(file_path))
    else:
        print("Employee not found.")

def readEmployees(file_path):
    employees = []
    if os.path.exists(file_path):
        with open(file_path, "r") as empFile:
            for line in empFile:
                employee_data = line.strip().split()
                if len(employee_data) >= 4:
                    employees.append(employee_data)
                else:
                    print(f"Invalid employee record format: {line}")
    else:
        print("Error: Payroll file not found.")
    return employees

def printGrossPRByEmployeeName(employees, name, calculate_gross_pay):
    found = False
    for employee in employees:
        if name.lower() == f"{employee[0]} {employee[1]}".lower():
            found = True
            rate = float(employee[2])
            hours = float(employee[3])
            overtime_pay = calculate_overtime(rate, hours)
            gross_pay = rate * hours + overtime_pay
            print(f"{employee[0]} {employee[1]} - Gross Pay: {gross_pay:.2f}")
            break
    if not found:
        print("Employee not found.")









