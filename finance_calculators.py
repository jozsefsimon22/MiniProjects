
import math

# Asks the user to choose a calculator and converts input to lower case so the program can recognize input even if it's capitalized 
calculator = input("Choose either 'investment' or 'bond' from the menu below to proceed: \n \n investment \t - to calculate the amount of interest you'll earn on interest \n bond \t \t - to calculate the amount you'll have to pay on a home loan \n").lower()

# If user selects the 'investment' calculator, it asks to enter details and choose between 'simple' or 'compound' interest rate
if (calculator == "investment"):
    deposit = float(input("Please enter the deposit amount: "))
    interest_rate = float(input("Please enter the interest rate: "))/100                                            # Input divided by 100 to get the decimal percentage 
    no_of_years = int(input("Please enter the number of years the investment is for: "))
    interest_type = input("Please select the interest type from the below options: \n simple \n compound \n")

    # Calculates the total amount based on the 'simple' interest rate type and rounds it to 2 decimal places
    if (interest_type == "simple"):
        total_amount = round(deposit * (1 + interest_rate * no_of_years), 2)

    #Calculates the total amount based on the 'compound' interest rate and rounds it to 2 decimal places
    elif (interest_type == "compound"):
        total_amount = round(deposit * math.pow((1 + interest_rate), no_of_years), 2)

    #Displays the below text along with the total amount
    print(f"The total amount including interest earned at the end of the investment period is: R{total_amount} ")
    
#If the user selects 'bond' calculator it asks to enter the details 
elif (calculator == "bond"):
    present_value = float(input("Please enter the present value of the house: "))
    annual_interest_rate = float(input("Please enter the interest rate: "))/100                                      # Input divided by 100 to get the decimal percentage 
    monthly_interest_rate = annual_interest_rate /12                                                                 # Calculates the monthly interest rate 
    no_of_months = int(input("Please enter the number of months to repay: "))

    #Calculates the monthly repayment amount based on the details entered above and rounds it to 2 decimal places 
    monthly_repayment = round((monthly_interest_rate * present_value) / (1 - math.pow((1 + monthly_interest_rate), no_of_months * -1)),2)

    # Prints out the below text along with the monthly repayment amount
    print(f"The monthly repayment amount of this bond is R{monthly_repayment}")

#If the user doesn't type in a valid input, it shows the below error message 
else:
     print("Error, input not recognized. Please enter either 'Investment' or 'Bond'.")

