"""
Написать 12 функций по переводу:
    Дюймы в сантиметры
    Сантиметры в дюймы
    Мили в километры
    Километры в мили
    Фунты в килограммы
    Килограммы в фунты
    Унции в граммы
    Граммы в унции
    Галлон в литры
    Литры в галлоны
    Пинты в литры
    Литры в пинты
Примечание: функция принимает на вход число и возвращает конвертированное число
"""

# 1.
def inch_to_cm(inch):
    cm = inch * 2.54
    return cm


# 2.
def cm_to_inch(cm):
    inch = cm / 2.54
    return inch


# 3.
def ml_to_km(ml):
    km = ml * 1.609
    return km


# 4.
def km_to_ml(km):
    ml = km / 1.609
    return ml


# 5.
def lb_to_kg(lb):
    kg = lb / 2.205
    return kg


# 6.
def kg_to_lb(kg):
    funt = kg * 2.205
    return funt


# 7.
def oz_to_gr(oz):
    gr = oz * 28.35
    return gr


# 8.
def gr_to_oz(gr):
    oz = gr / 28.35
    return oz


# 9.
def gal_to_L(gal):
    L = gal * 3.785
    return L


# 10.
def L_to_gal(L):
    gal = L / 3.785
    return gal


# 11.
def pt_to_L(pt):
    L = pt / 2.113
    return L


# 12.
def L_to_pt(L):
    pt = L * 2.113
    return pt


print(f"Enter:"
      f"\n\t1 to convert inches to centimeters "
      f"\n\t2 to convert centimeters to inches "
      f"\n\t3 to convert miles to kilometers "
      f"\n\t4 to convert kilometers to miles "
      f"\n\t5 to convert pounds to kilograms "
      f"\n\t6 to convert kilograms to pounds "
      f"\n\t7 to convert ounce to grams "
      f"\n\t8 to convert grams to ounce "
      f"\n\t9 to convert gallons to liters "
      f"\n\t10 to convert liters to gallons "
      f"\n\t11 to convert pints to liters "
      f"\n\t12 to convert liters to pints "
      )


while True:
    user_choice = int(input("Enter your choice [1-12] or enter 0 to exit: "))
    if user_choice == 0:
        print('Goodbye')
        break
    elif user_choice not in range(1, 12):
        print('Your choice must be within a number from 1 to 12')
        continue
    elif user_choice == 1:
        print(inch_to_cm(int(input('Enter inches to convert to cm: '))))
    elif user_choice == 2:
        print(cm_to_inch(int(input('Enter centimeters to convert to inches: '))))
    elif user_choice == 3:
        print(ml_to_km(int(input('Enter miles to convert to kilometers: '))))
    elif user_choice == 4:
        print(km_to_ml(int(input('Enter kilometers to convert to miles: '))))
    elif user_choice == 5:
        print(lb_to_kg(int(input('Enter pounds to convert to kilograms: '))))
    elif user_choice == 6:
        print(kg_to_lb(int(input('Enter kilograms to convert to pounds: '))))
    elif user_choice == 7:
        print(oz_to_gr(int(input('Enter ounce to convert to grams: '))))
    elif user_choice == 8:
        print(gr_to_oz(int(input('Enter grams to convert to ounce: '))))
    elif user_choice == 9:
        print(gal_to_L(int(input('Enter gallons to convert to liters: '))))
    elif user_choice == 10:
        print(L_to_gal(int(input('Enter liters to convert to gallons: '))))
    elif user_choice == 11:
        print(pt_to_L(int(input('Enter pints to convert to liters: '))))
    elif user_choice == 12:
        print(L_to_pt(int(input('Enter liters to convert to pints: '))))
        
        
        
#var2

import conversion as cv
from time import sleep


functions = {
    1: cv.inchs_to_centimeters,
    2: cv.centimeters_to_inchs,
    3: cv.miles_to_km,
    4: cv.km_to_miles,
    5: cv.pounds_to_kilos,
    6: cv.kilos_to_pounds,
    7: cv.ounces_to_grams,
    8: cv.grams_to_ounces,
    9: cv.gallons_to_liters,
    10: cv.liters_to_gallons,
    11: cv.pints_to_liters,
    12: cv.liters_to_pints
}

units = {
    1: 'Inchs to centimeters',
    2: 'Centimeters to inchs',
    3: 'Miles to kilometers',
    4: 'Kilometers to miles',
    5: 'Pounds to kilograms',
    6: 'Kilograms to pounds',
    7: 'Ounces to grams',
    8: 'Grams to ounces',
    9: 'Gallons to liters',
    10: 'Liters to gallons',
    11: 'Pints to liters',
    12: 'Liters to pints'
}

while True:

    print('*' * 50)
    print('\n\t\t\tChoose conversion below\nand ENTER the appropriate number for the operation\n')
    print('*' * 50)

    # Display options
    for k, v in units.items():
        print(f'\t\t{k}.  {v}')
        sleep(.07)

    print('x' * 50)
    print('\t\t\tFor EXIT enter 0')
    print('x' * 50)
    sleep(1)
    operation = input('Enter operation number >>>\t')

    # Validation for exit
    if operation.isdigit() and not int(operation):

        print('---\t' * 13)
        print('\t\t\t\t\t Bye!')
        print('''
         _____
        ( bye )
         -----
                O   ^__^
                 o  (oo)\_______
                    (__)\       )\/*
                        ||----w |
                        ||     ||
        ''')
        print('  ---' * 10)
        break

    elif operation.isdigit() and int(operation) <= 12 and int(operation) >= 1:
        operation = int(operation)

        argument = input(f'Enter amount of {units[operation].split()[0].lower()} >>> ')
        if argument.isdigit():
            argument = float(argument)
            print(f'{functions[operation](argument)} {units[operation].split()[2].lower()}')
            sleep(4)
        else:
            continue
    else:
        print('Incorrect value!')
        continue
