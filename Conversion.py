class weight:
    def lbs_kg():
        lbs = input('Weight in Lbs: ')
        kg = int(lbs) * 0.45
        print(f'Your Weight is {kg} kg')

    def kg_lbs():
        kg = input('Weight in Kg: ')
        lbs = int(kg) / 0.45
        print(f'Your Weight is {lbs} lbs')


class money:
    def dollar_rupee():
        dollar = input('Enter Amount in dollars: ')
        INR = int(dollar) * 75
        print(f'Your amount is ₹{INR}')

    def rupee_dollar():
        INR = input('Enter Amount in INR: ')
        dollar = int(INR) / 75
        print(f'You amount is ${dollar}')

