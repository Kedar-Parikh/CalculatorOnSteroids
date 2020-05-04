class menu:
    def addition():
        firstnum = input('Enter the first num: ')
        secondnum = input('Enter the second num: ')
        sum = int(firstnum) + int(secondnum)
        print(f'{firstnum} + {secondnum} = {sum}')

    def subtraction():
        firstnum = input('Enter the first num: ')
        secondnum = input('Enter the second num: ')
        sub = int(firstnum) - int(secondnum)
        print(f'{firstnum} - {secondnum} = {sub}')

    def multiplication():
        firstnum = input('Enter the first num: ')
        secondnum = input('Enter the second num: ')
        product = int(firstnum) * int(secondnum)
        print(f'{firstnum} x {secondnum} = {product}')

    def division():
        try:
            firstnum = input('Enter the first num: ')
            secondnum = input('Enter the second num: ')
            quotient = int(firstnum) / int(secondnum)
            print(f'{firstnum} ÷ {secondnum} = {quotient}')
        except ZeroDivisionError:
            print('Error! Division by 0')

    def exponent():
        firstnum = input('Enter the number: ')
        secondnum = input('Enter the exponent: ')
        exp = int(firstnum) ** int(secondnum)
        print(f'{firstnum} ^ {secondnum} = {exp}')
