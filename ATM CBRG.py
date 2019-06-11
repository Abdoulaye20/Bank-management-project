print('===================Welcome to BCRG============')
restart=('Y')
chances = 3
balance = 1000
while chances >= 0:
    pin = int(input('Please Enter You 4 Digit Pin: '))
    if pin == (1234):
        print('You entered you pin Correctly\n')
        while restart not in ('n','NO','no','N'):
            print("===================================================\n")
            print('========= Press 1 For Your Balance=================\n')
            print('========= Press 2 To Make a Withdrawl==============\n')
            print('========= Press 3 Fo Deposit=======================\n')
            print("========= press 4 To transfer =====================\n")
            print('========= Press 5 To Return Card===================\n')
            option = int(input('What Would you like to choose?'))
            if option == 1:
                print('Your Balance is ',balance,'$ \n')
                restart = input('Would You you like to go back? ')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break
            elif option == 2:
                option2 = ('y')
                amount = float(input('How Much Would you like to withdraw?: '))
                if amount > balance:
                    print("suffiscient amount !")
                    print(" your balance is %d", balance ," $ \n")
                else:
                    balance=balance - amount
                    print("successful! \n")
                    print("your new balance is %d", balance, "$ \n")
                    restart = input('Would You you like to go back? ')
                    if restart in ('n','NO','no','N'):
                        print('Thank You')
                        break   
            elif option == 3:
                amount = float(input('How Much you want to depose? '))
                balance = balance + amount
                print ('\nYour Balance is now  ',balance, "$")
                restart = input('Would You you like to go back? ')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break
            elif option == 4:
                print(" Please give the information bellow:\n")
                account=int(input("Enter the account you want to recive the money?"))
                amount=int(input("Enter the amount?"))
                if amount > balance:
                    print("amount sufficient!")
                    break
                else:
                    balance= balance- amount
                    print("transfer successfull \n")
                    print("Your new balance is :",balance ," $ \n")
                    restart = input('Would You you like to go back? ')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break
            elif option == 5:
                print('Please wait whilst your card is Returned...\n')
                print('Thank you for you service')
                break
            else:
                print('Please Enter a correct number. \n')
                restart = ('y')
    elif pin != ('1234'):
        print('Incorrect Password')
        chances = chances - 1
        if chances == 0:
            print('\nNo more tries')
            break
