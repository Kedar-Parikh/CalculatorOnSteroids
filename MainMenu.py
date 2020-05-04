import ConversionMenu
import mathmenu
class main:
        user_input = ''
        while user_input != '0':
            user_input = input('''
            Main Menu! 
            Choose a number:
            1)Regular Math
            2)Conversion
            0)Exit
            ''')
            if user_input == '1':
                mathmenu.mm.menumath()
            elif user_input == '2':
                ConversionMenu.ConMenu.ConverseMenu()
            elif user_input == '0':
                exit(0)
            else:
                print('Please enter a correct value')



