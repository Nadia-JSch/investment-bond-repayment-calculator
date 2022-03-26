# GOAL: the user has access to INVESTMENT and HOME LOAN REPAYMENT calculators

# import math for the power function
import math

# print greeting to welcome user 
print("Welcome to the Investment & Home Loan Repayment Calculator!\n")

# First, the user chooses the investment or bond calculator
calc_type = input("""Choose either 'investment' or 'bond' from the menu below to proceed:
\ninvestment \t- to calculate the amount of interest you'll earn on interest
bond \t\t- to calculate the amount you'll have to pay on a home loan\n""")

# user input.txt shouldn't be case senstive, so have some common otptions of user input.txt
if calc_type == "investment" or calc_type == "INVESTMENT" or calc_type =="INVESTMENT" or calc_type =="iNVESTMENT" or calc_type =="invest":
    amount_dep = float(input("Please enter the exact deposit amount only (enter numbers only): "))
    int_rate = float(input("Now, enter the interest rate percentage (numbers only): "))
    years_invest = int(input("How many years will you invest for? (numbers only): "))
    
    # if 'investment', ask the user if they want to calculate "simple" or "compound" interest 
    interest = input("Is it 'simple' or 'compound' interest? ")
   
    # nested if/elif/else statement for the simple, compound, and error options 
    # simple interest formula: x = deposit * (1 + (interest/100)) * years
    if interest == "simple":
        tot_simp_interest = amount_dep * (1 + (int_rate / 100) * (years_invest)) 
        print(f"""You will have R{tot_simp_interest:.2f} after {years_invest} years.\nThis includes the principal amount of R{amount_dep:.2f}.""")

    # compound interest formula: x = deposit * (1 + interest/100)^ years
    elif interest == "compound": 
            tot_comp_interest = amount_dep * (math.pow((1 + int_rate/100), years_invest))
            print(f"""You will have R{tot_comp_interest:.2f} after {years_invest} years.\nThis includes the principal amount of R{amount_dep:.2f}.""")

    # print an error message if input.txt is not 'simple' or 'investment'
    else:
        print("Please try again")   

# if bond repayment calculator is selected ask for proverty value, interest & months   
elif calc_type == "bond" or calc_type == "Bond" or calc_type == "BOND" or calc_type =="bOND":
    house_value = float(input("What is the property's present value? (numbers only): "))
    house_interest = float(input("What is the interest rate? (numbers only): "))
    house_time = float(input("How many months will you take to repay the bond? (numbers only): "))
    
    # bond repayment calculations: x = (int/12) / (1 - (1+ int)^ -repayment months)
    # where int = interest rate / 100
    bond_repay = (house_interest/100/12 * house_value) / (1 - math.pow(1 + house_interest/100/12,-house_time))
    
    # display result (rounding off the answer to two decimal points as above)
    print(f"You'll need to pay R{bond_repay:.2f} every month for {house_time:.0f} months.")

# print an error message if initial input.txt is not related to 'investment' or 'bond'
else:
    print(f"Sorry! I don't recognize '{calc_type}'.\nPlease enter 'investment' or 'bond'.")

# print a goodbye greeting
print("Thank you for using the Investment and Home Loan Repayment Calculator.\nMay you achieve wealth!")

#---END---