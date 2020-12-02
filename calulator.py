def calculate ():
    operation = input("Please enter the desired operation"
                      "\n1. Add"
                      "\n2. Subtract"
                      "\n3. Multiply"
                      "\n4. Divide"
                      "\n")
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))

    if operation == '1':
        print('{} + {} ='.format(num1, num2))
        print(num1 + num2)
        again()
    elif operation == '2':
        print('{} - {} ='.format(num1, num2))
        print(num1 - num2)
        again()
    elif operation == '3':
        print('{} * {} ='.format(num1, num2))
        print(num1 * num2)
        again()
    elif operation == '4':
        print('{} / {} ='.format(num1, num2))
        print(num1 / num2)
        again()
    else:
        print("Syntax Error")
        #Add again() function to calculate
        again()

def again():
    calc_again = input("\nDo you want to calculate again? Please type Y for Yes N for No.")
    if calc_again == 'Y':
        calculate()
    elif calc_again == 'N':
        print("Thank you for using this calculator see you later!")
    else:
        again()
calculate()

def welcome():
    print("Welcome to calcualtor")

    welcome()
    calculate()
