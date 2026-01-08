#LM 2nd Financial Calculator

#Create function savings
def savings():
    #get (valid) user intputs for GOAL and DEPOSIT
    goal=input('What is your savings goal?')
    deposit=input('How much money are you adding to savings every month?')
    #display GOAL divided by DEPOSIT, rounded up, months to acheive this savings goal
    print(int(goal/deposit+1),'months to achieve this savings goal.')

#create fuction interest
def interest():
    #get (valid) user intputs for RATE, AMOUNT, TIME
    #create function interest
        #add RATE times AMOUNT to AMOUNT
    #repeat TIME times
        #call function interest
    #display after the duration, the account will include AMOUNT dollars

#create function budget
    #set RATES to dictionary of percentages for categories
    #get (valid) user input for INCOME
    #loop through catregories in RATES as CAT
        #display you have INCOME times RATES at CAT for the CAT category

#create function sales
    #get (valid) user inputs for DISCOUNT and PRICE
    #print the reduced price is PRICE times DISCOUNT

#create function tip
    #get (valid) user inputs for AMOUNT and TIP
    #display the tip amount is AMOUNT plus AMOUNT times TIP

#create function main
    #display options
    #ask user for (valid) input for CHOICE
    #run correct function for CHOICE