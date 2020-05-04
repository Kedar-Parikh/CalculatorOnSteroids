import maths
class mm:
    def menumath():
        user_input = ''
        while user_input != '0':
            user_input = input('''
            Choose the correct option:
            1)Addition
            2)Subtraction
            3)Multiplication
            4)Division
            5)Exponention
            0)Exit
    
            ''')
            if user_input == '1':
                maths.menu.addition()
            elif user_input == '2':
                maths.menu.subtraction()
            elif user_input == '3':
                maths.menu.multiplication()
            elif user_input == '4':
                maths.menu.division()
            elif user_input == '5':
                maths.menu.exponent()
            elif user_input == '0':
                break
            else:
                print('Please enter a correct value')
