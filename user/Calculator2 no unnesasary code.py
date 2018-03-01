# while loop is used so that the user can easilly restart program and print multiple operations
restart = 'yes'
while restart != 'no':
    if restart.strip() == 'no':
        break

    # Defining operations
    def add(x, y):
        return x + y
    def subtract(x, y):
        return x - y
    def multiply(x, y):
        return x * y
    def divide(x, y):
        return x / y
    def power(x, y):
        return x ** y

    # prints information for user    
    print('Select Operation:')
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')
    print('5. Raise to a power')

    # takes information from user
    choice=input('Enter 1, 2, 3, 4 or 5: ')

    num1=float(input('Enter first number: '))
    num2=float(input('Enter second number: '))

    # completes user defined operation
    if choice == '1':
        answer=add(num1, num2)
        print(num1,' + ',num2,' = ',answer)
    elif choice == '2':
        answer=subtract(num1, num2)
        print(num1,' - ',num2,' = ',answer)
    elif choice == '3':
        answer=mulitply(num1, num2)
        print(num1,' * ',num2,' = ',answer)
    elif choice == '4':
        answer=divide(num1, num2)
        print(num1,' / ',num2,' = ',answer)
    elif choice == '5':
        answer=power(num1, num2)
        print(num1,' ^ ',num2,' = ',answer)
    else:
        print('Invalid Input')

        # ends/restarts while loop depending on user input
        restart=input('Another operation? If not enter no: ')
        if restart != 'no':
            print('I am not sure, but I will take that as a yes')

    
