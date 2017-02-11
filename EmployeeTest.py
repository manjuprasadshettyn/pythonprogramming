from Employee import Employee

def main():
	name=input("Enter the Emplyoee name:\n")
	design=input("Enter the designation:\n")
	salary=eval(input("Enter the salary\n"))
	DA=eval(input("Enter the DA\n"))
	HRA=eval(input("Enter HRA\n"))
	
	#create an object
	emp=Employee(name,design,salary,DA,HRA)
	
	print("The gross salary is",emp.grosssalary())

main()
