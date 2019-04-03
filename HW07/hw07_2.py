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

user_choice = int(input("Enter your choice [1-12] or enter 0 to exit: "))

while True:
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
