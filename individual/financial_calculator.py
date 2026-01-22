#LM 1st Financial Calculator

#Create function savings
def savings():
    #get (valid) user intputs for GOAL and DEPOSIT
    goal=input('What is your savings goal? ')
    while True:
        try:
            goal=float(goal)
            break
        except:
            goal=input('What is your savings goal? ')
    deposit=input('How much money are you adding to savings every month? $')
    while True:
        try:
            deposit=float(deposit)
            break
        except:
            deposit=input('How much money are you adding to savings every month? $')
    #display GOAL divided by DEPOSIT, rounded up, months to acheive this savings goal
    print(int(goal/deposit+1),'months to achieve this savings goal. ')

#create function interest
def interest():
    #get (valid) user intputs for RATE, AMOUNT, TIME
    rate=input('What is your interest rate in percent? ')
    while True:
        try:
            rate=float(rate)/100
            break
        except:
            rate=input('What is your interest rate in percent? ')
    amount=input('What is your current balance? $')
    while True:
        try:
            amount=float(amount)
            break
        except:
            amount=input('What is your current balance? $')
    time=input('How long will this investment last in months? ')
    while True:
        try:
            time=int(time)
            break
        except:
            time=input('How long will this investment last in months? ')
    #create function interest2 to add interest
    def interesterest(): #the inner function adds the interest to the total value
        #add RATE times AMOUNT to AMOUNT
        nonlocal amount, rate
        amount += rate*amount
    #repeat TIME times
    for i in range(time):
        #call function interest
        interesterest()
    #display after the duration, the account will include AMOUNT dollars
    print(f'After the duration, the account will include ${amount}')

#create function budget
def budget():
    #set RATES to dictionary of percentages for categories
    rates={'housing':.30,'transportation':.10,'food':.10,'utilities':.05,'insurance':.20,'medical':.05,'savings':.20}
    #get (valid) user input for INCOME
    income=input('What is your income? $')
    while True:
        try:
            income=float(income)
            break
        except:
            income=input('What is your income? $')
    #loop through catregories in RATES as CAT
    for cat in rates.keys():
        #display you have INCOME times RATES at CAT for the CAT category
        print(f'${income*rates[cat]} for the {cat} category.')

#create function sales
def sales():
    #get (valid) user inputs for DISCOUNT and PRICE
    price=input('What is the price? $')
    while True:
        try:
            price=float(price)
            break
        except:
            price=input('What is the price? $')
    discount=input('What is the discount in percent? ')
    while True:
        try:
            discount=float(discount)/100
            break
        except:
            discount=input('What is the discount in percent? ')
    #display the reduced price is PRICE minus PRICE times DISCOUNT
    print(f'The reduced price is ${price-price*discount}')

#create function tip
def tip():
    #get (valid) user inputs for AMOUNT and TIP
    amount=input('What is the amount due? $')
    while True:
        try:
            amount=float(amount)
            break
        except:
            amount=input('What is the amount due? $')
    tip=input('What is the tip percentage? ')
    while True:
        try:
            tip=float(tip)/100
            break
        except:
            tip=input('What is the tip percentage? ')
    #display the tip amount is AMOUNT times TIP
    print(f'The tip amount is ${amount*tip}')

#create function main
def main():
    #display options
    print('Welcome to the Financial Calculator. Choose from: Savings Goal, Compound Interest, Budget, Sale, Tip.')
    #ask user for (valid) input for CHOICE
    choice=input('Which option would you like to use? ').lower()
    while choice.lower() not in ['savings goal', 'compound interest', 'budget', 'sale', 'tip']:
        choice=input('Which option would you like to use? ').lower()
    #run correct function for CHOICE
    if choice=='savings goal':
        savings()
    elif choice=='compound interest':
        interest()
    elif choice=='budget':
        budget()
    elif choice=='sale':
        sales()
    else:
        tip()

main()