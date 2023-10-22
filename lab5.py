# Name : Peter Geevarghese Alex
# Lab 5
# Course number : ITMD 513-01
# Description :
import time
print("ITMD 513-01")
print("Lab 5")
print("Programmer: Peter Geevarghese Alex")

x = 12
print("-" * 25)
## dd/mm/yyyy format
print (time.strftime("%d/%m/%Y"))



#military time
print ("Current time:",time.strftime("%X"))
import os
import methods

def menu():
    pstr = "Choose from the following payroll choices\n"
    pstr += "(1) A gross PR payroll report for all employees\n"
    pstr += "(2) A gross PR payroll report for a single employee by name\n"
    pstr += "(3) Add Employee data followed by the rate of pay and hours worked\n"
    pstr += "(4) Delete the employee data\n"
    pstr += "(5) Modify the employee data\n"
    pstr += "(6) Quit Program"
    print(pstr)


def main():
    file_path = input("Enter the payroll file name: ")
    employees = methods.readEmployees(file_path)
    answer = ""
    while answer != "6":
        if answer == "1":
            methods.printAll(employees, methods.calculate_overtime)
        elif answer == "2":
            name = input("Enter a name to search employee: ")
            methods.printGrossPRByEmployeeName(employees, name, methods.calculate_overtime)
           
        elif answer == "3":
            methods.addEmp(file_path, employees)
        elif answer == "4":
            methods.deleteEmp(file_path, employees)
        elif answer == "5":
            methods.modifyEmp(file_path, employees)  # Modify employee data
        elif answer == "6":
            methods.exitApp()
        else:
            menu()  # Show the menu only when an invalid choice is entered

        methods.writeEmployees(file_path, employees)  # Write updated employee data to file
        answer = input("Enter Menu Choice Now! ")



if __name__ == "__main__":
    main()
