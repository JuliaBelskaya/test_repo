# 1.
def inch_to_cm(inch):
    cm = inch * 2.54
    return cm


print(inch_to_cm(int(input('Enter inche: '))))

# 2.
def cm_to_inch(cm):
    inch = cm / 2.54
    return inch


print(cm_to_inch(int(input('Enter cantimeter: '))))

# 3.
def ml_to_km(ml):
    km = ml * 1.609
    return km


print(ml_to_km(int(input('Enter mile: '))))

# 4.
def km_to_ml(km):
    ml = km / 1.609
    return ml


print(km_to_ml(int(input('Enter kilometer: '))))

# 5.
def lb_to_kg(lb):
    kg = lb / 2.205
    return kg


print(lb_to_kg(int(input('Enter pound: '))))

# 6.
def kg_to_lb(kg):
    funt = kg * 2.205
    return funt


print(kg_to_lb(int(input('Enter kilogram: '))))

# 7.
def oz_to_gr(oz):
    gr = oz * 28.35
    return gr


print(oz_to_gr(int(input('Enter once: '))))

# 8.
def gr_to_oz(gr):
    oz = gr / 28.35
    return oz


print(gr_to_oz(int(input('Enter gram: '))))

# 9.
def gal_to_L(gal):
    L = gal * 3.785
    return L


print(gal_to_L(int(input('Enter gallon: '))))

# 10.
def L_to_gal(L):
    gal = L / 3.785
    return gal


print(L_to_gal(int(input('Enter liter: '))))

# 11.
def pt_to_L(pt):
    L = pt / 2.113
    return L


print(pt_to_L(int(input('Enter pint: '))))

# 12.
def L_to_pt(L):
    pt = L * 2.113
    return pt


print(L_to_pt(int(input('Enter liter: '))))
