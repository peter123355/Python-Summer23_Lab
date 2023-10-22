# **************************************************************************************
# Statement: Loops and Repetition - Bank Account
# Input:     initial bank balance
#            annual interest rate
#            PIN number
# Output:    monthly balance for each month during 12 months

# local variable declarations

initial_bank_balance = 0.0
annual_interest_rate = 0.0
monthly_bal = 0.0
total_interest = 0.0

# Validates that PIN number meets security conditions
required_pin = "1234Ax"
attempt = 1

while attempt <= 3:
    pin_number = input("Enter PIN: ")
    if pin_number == required_pin:
        print(">>>")
        initial_bank_balance = float(input("Enter an initial bank balance: "))
        print("")
        annual_interest_rate = float(input("Include annual interest rate (as a decimal): "))
        print("\n")
        monthly_bal = initial_bank_balance

        print("{:<8s}{:<15s}{:<10s}".format("Month #", "Interest Amt", "Balance"))
        print("-----------------------------------")

        for month in range(1, 13):
            interest = (annual_interest_rate / 12) * monthly_bal
            monthly_bal = monthly_bal + interest
            total_interest += interest
            print("{:<8d}{:<15.2f}{:<10.2f}".format(month, interest, monthly_bal))

        print("-----------------------------------")
        print("Total\t\t", format(total_interest, '.2f'), "\t\t", format(monthly_bal, '.2f'))
        print(">>>")
        break
    else:
        if len(pin_number) < 4:
            print("\nPIN is too short. PIN must be at least 4 digits in length.\n")
        print("Attempts left =", 3 - attempt, ", PIN is incorrect\n")
        attempt += 1
