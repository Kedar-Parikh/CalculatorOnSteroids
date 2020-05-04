import Conversion

class ConMenu:
    def ConverseMenu():
        user_entry = ''
        while user_entry != '0':
            user_entry = input('''
            Press the number to continue:
            1)Pounds to Kilograms
            2)Kilograms to Pounds
            3)USD to INR
            4)INR to USD
            0)Exit
            
            ''')
            if user_entry == '1':
                Conversion.weight.lbs_kg()
            elif user_entry == '2':
                Conversion.weight.kg_lbs()
            elif user_entry == '3':
                Conversion.money.dollar_rupee()
            elif user_entry == '4':
                Conversion.money.rupee_dollar()
            elif user_entry == '0':
                break
            else:
                print('Please enter a correct value!')



