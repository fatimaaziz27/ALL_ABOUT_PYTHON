employees = []  # list to store employee dictionaries
# Function to add a new employee
def add_employee():
    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    salary = float(input("Enter employee salary: "))
    emp = {"name": name, "age": age, "salary": salary}
    employees.append(emp)
    print("Employee added successfully!\n")

# Function to display all employees
def show_employees():
    if not employees:
        print("No employees to display.\n")
    else:
        print("\n--- Employee List ---")
        for i, emp in enumerate(employees, 1):
            print(f"{i}. Name: {emp['name']}, Age: {emp['age']}, Salary: {emp['salary']}")
        print()

# Function to calculate total salary expense
def total_salary():
    total = 0
    for emp in employees:
        total += emp['salary']  # Using operators
    print(f"Total Salary Expense: {total}\n")

# Main loop
while True:
    print("1. Add Employee")
    print("2. Show Employees")
    print("3. Total Salary Expense")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        show_employees()
    elif choice == "3":
        total_salary()
    elif choice == "4":
        print("Exiting Employee Management System...")
        break
    else:
        print("Invalid choice, try again.\n")
