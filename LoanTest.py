from Loan import Loan

def main():
	annualInterestRate=eval(input("Enter Yearly interest rate\n"))
	numberOfYears=eval(input("Enter the number of years as integers\n"))
	loanAmount=eval(input("Enter Loan Amount\n"))
	borrower=input("Enter the borrowers name:\n")
	
	#create an object
	loan=Loan(annualInterestRate,numberOfYears,loanAmount,borrower)
	
	print("The loan is for",loan.getBorrower())
	print("The monthly payment is ",loan.getMonthlyPayment())
	print("The total payment is",loan.getTotalPayment())

main()
