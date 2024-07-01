"""
Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and emp_department and methods like calculate_emp_salary, emp_assign_department, and print_employee_details.
Sample Employee Data:
"ADAMS", "E7876", 50000, "ACCOUNTING"
"JONES", "E7499", 45000, "RESEARCH"
"MARTIN", "E7900", 50000, "SALES"
"SMITH", "E7698", 55000, "OPERATIONS"
Use 'assign_department' method to change the department of an employee.
Use 'print_employee_details' method to print the details of an employee.
Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked, which is the number of hours worked by the employee. If the number of hours worked is more than 50, the method computes overtime and adds it to the salary. Overtime is calculated as following formula:
overtime = hours_worked - 50
Overtime amount = (overtime * (salary / 50))
"""

class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department) -> None:
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department
        
    def calculate_emp_salary(self, emp_salary, hours_worked):
        if hours_worked > 50:
            # overtime and adds it to the salary
            overtime = hours_worked - 50
            overtime_amount = (overtime * (emp_salary / 50))
            self.emp_salary += overtime_amount
        print(f'The total employee salary is {self.emp_salary}.')
            
    
    def emp_assign_department(self, new_department):
        self.emp_department = new_department
        print(f'Employment department is {self.emp_department}.')
    
    def print_employee_details(self):
        print('Employee Details')
        print(f'Name: {self.emp_name}')
        print(f'ID: {self.emp_id}')
        print(f'Salary: {self.emp_salary}')
        print(f'Department: {self.emp_department}')
        
    
employee1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
employee2 = Employee("JONES", "E7499", 45000, "RESEARCH")
employee3 = Employee("MARTIN", "E7900", 50000, "SALES")
employee4 = Employee("SMITH", "E7698", 55000, "OPERATIONS")

# Change the departments of employee1 and employee4
employee1.emp_assign_department("OPERATIONS")
employee4.emp_assign_department("SALES")

# Now calculate the overtime of the employees who are eligible:
employee2.calculate_emp_salary(45000, 52)
employee4.calculate_emp_salary(45000, 60)

print("Updated Employee Details:")
employee1.print_employee_details()
employee2.print_employee_details()
employee3.print_employee_details()
employee4.print_employee_details()