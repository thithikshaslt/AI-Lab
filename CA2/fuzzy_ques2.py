import matplotlib.pyplot as plt
import numpy as np

def triangular(x,a,b,c):
    if a < x < b :
        return (x-a)/(b-a)
    if b <= x <= c:
        return (c-x)/(c-b)
    return 0

def trapezoidal(x,a,b,c,d):
    if a < x < b:
        return (x-a)/(b-a)
    if b < x < c:
        return 1
    if c < x < d:
        return (d-x)/(d-c)
    return 0

def get_membership(x,fuzzyset):
    return trapezoidal(x, *fuzzyset) if len(fuzzyset) == 4 else triangular(x, *fuzzyset)

X_FUZZYSET = {
    "A1" : [0,5,10],
    "A2" : [5,10,15],
}

Y_FUZZYSET = {
    "B1" : [0,50,100],
    "B2" : [50,100,150,200],
}

Z_FUZZYSET = {
    "C1" : [0,10,20],
    "C2" : [20,30,40],
}

RULES = {
    1 : ["A1","B1","C1"],
    2 : ["A2","B2","C2"]
}

def fuzzify(value,set):
    return {k : get_membership(value,v) for k,v in set.items()}

x = 6
y = 25

x_fuzzified = fuzzify(x,X_FUZZYSET)
y_fuzzified = fuzzify(y,Y_FUZZYSET)

def apply_rules(x_fuzzified, y_fuzzified):
    return { i : (min(x_fuzzified[s],y_fuzzified[a]),o) for i, (s,a,o) in RULES.items() if min(x_fuzzified[s], y_fuzzified[a]) > 0}

rule_strengths = apply_rules(x_fuzzified,y_fuzzified)

def calculate_areas(rule_strengths):
    areas , weighted_areas = {}, {}

    for i , (strength, out) in rule_strengths.items():
        set_val = Z_FUZZYSET[out]
        center = set_val[1] if len(set_val) == 3 else (set_val[1]+set_val[2])/2

        if len(set_val) == 4:
            base1 = set_val[3] - set_val[0]
            base2 = set_val[2] - set_val[1]
            area = strength*(base1+base2)/2

        else:
            base = set_val[2] - set_val[0]
            area = strength * base /2 

        areas[i] = area
        weighted_areas[i] = center*area

    return areas,weighted_areas

def defuzzify(areas, weighted_areas):
    total_area = sum(areas.values())
    return sum(weighted_areas.values()) / total_area if total_area> 0 else 0

areas, weighted_areas = calculate_areas(rule_strengths)
z = defuzzify(areas,weighted_areas)
print(z)

def plot_fuzzy_sets(fuzzyset, title, start, stop, highlight_x = None):
    plt.figure(figsize=(10,6))

    x_vals = np.linspace(start,stop,500)

    for label, params in fuzzyset.items():
        y_vals = np.array([get_membership(a,params) for a in x_vals])

        plt.plot(x_vals,y_vals,label=label)

    if highlight_x is not None:
        plt.axvline(highlight_x,color="red",linestyle="--")

    plt.title(title)
    plt.xlabel("values")
    plt.ylabel("membership")
    plt.grid(True)
    plt.show()

    
plot_fuzzy_sets(X_FUZZYSET,"X FUZZY SET",0,15,None)
plot_fuzzy_sets(Y_FUZZYSET,"y fuzzy",0,200,None)
plot_fuzzy_sets(Z_FUZZYSET,"Z fuzzy",0,40,highlight_x=z)
