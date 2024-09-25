monthly_salary = float(input("Enter your monthly salary: "))
loan_amount = float(input("Enter the loan amount you are requesting: "))

if monthly_salary >= 30000 and loan_amount <= 10 * monthly_salary:
   months_pay= int(input("How many months would you plan to pay the loan?:"))
   total= loan_amount *1.10 
   print(f"You are eligible for the loan. The total amount to be paid with 10% interest is: ${total:.2f}")
   print(f"You will pay ${total/months_pay:.2f} per month for {months_pay} months")
else:
    if loan_amount > 10 * monthly_salary:
      print("You are not eligible for the loan because the requested loan amount is too high to meet the requirements.")
    if monthly_salary < 30000:
      print("You are not eligible to loan because your salary is too low to meet the requirements")





