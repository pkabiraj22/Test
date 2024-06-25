def addition():                                             ##testing
    print('Addition')
    cont_cal = 'y'
    inputs = 2

    num1 = float(input('Enter a number: '))
    num2 = float(input('Enter another number: '))

    ans = num1 + num2
    print('Current Result: ', ans)

    while cont_cal.lower() == 'y':
        cont_cal = input('Continue Calculation.. (y/n): ')

        while cont_cal not in ['y','n']:
            print('Enter a valid input....(y/n)')
            cont_cal = input('Continue Calculation..(y/n): ')
            continue
    

        if cont_cal.lower() == 'n':
            break

        print('Enter \'a\' for Addition')
        print('Enter \'s\' for Substruction')
        print('Enter \'m\' for Multiplication')
        print('Enter \'d\' for Division')
        print('Enter \'q\' to stop')


        userinput = input('Selection: ')
        
        if userinput == 'a':
            num = float(input('Enter number: '))
            print('Addition')
            ans += num
        elif userinput == 's':
            num = float(input('Enter number: '))
            print('Substruction')
            ans -= num
        elif userinput == 'm':
            num = float(input('Enter number: '))
            print('Multiplication')
            ans *= num
        elif userinput == 'd':
            num = float(input('Enter number: '))
            print('Division')
            ans /= num
        elif userinput == 'q':
            print('No more Calculation')
            break
        else:
            print('Please enter valid input....')
            continue

        print('Current Result: ', round(ans,3))
        inputs += 1
        
    return [round(ans,3),inputs]
        


def substruction():
    print('Substruction')

    cont_cal = 'y'
    input1 = 2

    num1 = float(input('Enter a number: '))
    num2 = float(input('Enter another number: '))

    ans = num1 - num2
    print(f'Current Result: {ans}')


    while cont_cal.lower() == 'y':
        cont_cal = input('Continue Calculation.. (y/n): ')
        

        while cont_cal not in ['y','n']:
            print('Enter a valid input....(y/n)')
            cont_cal = input('Continue Calculation..(y/n): ')
            continue
    

        if cont_cal.lower() == 'n':
            break

        print('Enter \'a\' for Addition')
        print('Enter \'s\' for Substruction')
        print('Enter \'m\' for Multiplication')
        print('Enter \'d\' for Division')
        print('Enter \'q\' to stop')


        userinput = input('Selection: ')

        if userinput == 'a':
            num = float(input('Enter number: '))
            print('Addition')
            ans += num
        elif userinput == 's':
            num = float(input('Enter number: '))
            print('Substruction')
            ans -= num
        elif userinput == 'm':
            num = float(input('Enter number: '))
            print('Multiplication')
            ans *= num
        elif userinput == 'd':
            num = float(input('Enter number: '))
            print('Division')
            ans /= num
        elif userinput == 'q':
            print('No more Calculation')
            break
        else:
            print('Please enter valid input....')
            continue

        print('Current Result: ', round(ans,3))
        inputs += 1
        
    return [round(ans,3),inputs]
         
        

def Multiplication():
    print('Multiplication')

    inputs = 2
    cont_cal = 'y'

    num1 = float(input('Enter a number: '))
    num2 = float(input('Enter another number: '))

    ans = num1*num2

    print('Current Result: ',ans)

    while cont_cal.lower() == 'y':
        cont_cal = input('Continue Calculation.. (y/n): ')

        while cont_cal not in ['y','n']:
            print('Enter a valid input....(y/n)')
            cont_cal = input('Continue Calculation..(y/n): ')
            continue
    
        print('Enter \'a\' for Addition')
        print('Enter \'s\' for Substruction')
        print('Enter \'m\' for Multiplication')
        print('Enter \'d\' for Division')
        print('Enter \'q\' to stop')        
       
        userinput = input('Selection: ')

        if userinput == 'a':
            num = float(input('Enter number: '))
            print('Addition')
            ans += num
        elif userinput == 's':
            num = float(input('Enter number: '))
            print('Substruction')
            ans -= num
        elif userinput == 'm':
            num = float(input('Enter number: '))
            print('Multiplication')
            ans *= num
        elif userinput == 'd':
            num = float(input('Enter number: '))
            print('Division')
            ans /= num
        elif userinput == 'q':
            print('No more Calculation')
            break
        else:
            print('Please enter valid input....')
            continue

        print('Current Result: ', round(ans,3))
        inputs += 1
        
    return [round(ans,3),inputs]

def division():
    print('Division')

    cont_cal = 'y'
    inputs = 2

    num1 = float(input('Enter a number: '))
    num2 = float(input('Enter another number: '))

    ans = num1/num2

    print(f'Current Result: {ans}')

    while cont_cal == 'y':
        cont_cal = input('Continue Calculation..(y/n): ')

        while cont_cal not in ['y','n']:
            print('Enter a valid input....(y/n)')
            cont_cal = input('Continue Calculation..(y/n): ')
            continue
    

        if cont_cal.lower() == 'n':
            break
        
        print('Enter \'a\' for Addition')
        print('Enter \'s\' for Substruction')
        print('Enter \'m\' for Multiplication')
        print('Enter \'d\' for Division')
        print('Enter \'q\' to stop')


        userinput = input('Selection: ')

        if userinput == 'a':
            num = float(input('Enter number: '))
            print('Addition')
            ans += num
        elif userinput == 's':
            num = float(input('Enter number: '))
            print('Substruction')
            ans -= num
        elif userinput == 'm':
            num = float(input('Enter number: '))
            print('Multiplication')
            ans *= num
        elif userinput == 'd':
            num = float(input('Enter number: '))
            print('Division')
            ans /= num
        elif userinput == 'q':
            print('No more Calculation')
            break
        else:
            print('Please enter valid input....')
            continue

        print('Current Result: ', round(ans,3))
        inputs += 1
        
    return [round(ans,3),inputs]
    





def Calculator():
    quit = False
    while not quit:
        print('Welcome to the Calculator project !!')
        print('Enter \'a\' for Addition')
        print('Enter \'s\' for Substruction')
        print('Enter \'m\' for Multiplication')
        print('Enter \'d\' for Division')
        print('Enter \'q\' to Quit')

        userinput = input('Selection: ')

        if userinput == 'q':
            quit = True
            continue

        if userinput == 'a':
            result = addition()
            print('Ans: ',result[0], 'Total inputs: ', result[1])
        elif userinput == 's':
            result = substruction()
            print('Ans: ',result[0], 'Total inputs: ', result[1])
        elif userinput == 'm':
            result = Multiplication()
            print('Ans: ',result[0], 'Total inputs: ', result[1])
        elif userinput == 'd':
            result = division()
            print('Ans: ',result[0], 'Total inputs: ', result[1])
        else:
            print('Please enter valid in input....')
            continue



if __name__ ==  '__main__':
    Calculator()


        
