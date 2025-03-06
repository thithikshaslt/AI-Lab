import numpy as np
import matplotlib.pyplot as plt

# membership functions
def triangular(x,a,b,c):
    if a < x < b:
        return (x-a)/(b-a)
    if b <= x <= c:
        return (c-x)/(c-b)
    return 0

def trapezoidal(x,a,b,c,d):
    if a < x < b:
        return (x-a)/(b-a)
    if b <= x <= c:
        return 1
    if c < x < d:
        return (d-x)/(d-c)
    return 0


#func to get membership
def get_membership(x,fuzzy_set):
    return trapezoidal(x, *fuzzy_set) if len(fuzzy_set) == 4 else triangular(x, *fuzzy_set)


#define fuzzy sets as per question
FUZZY_SETS = {
    "NL":[0,0,31,61],
    "NM":[31,61,95],
    "NS":[61,95,127],
    "ZE":[95,127,159],
    "PS":[127,159,191],
    "PM":[159,191,223],
    "PL":[191,223,225,255],
}


#define rules as per question
RULES = {
    1: ["NL","ZE","PL"],
    2: ["ZE","NL","PL"],
    3: ["NM","ZE","PM"],
    4: ["NS","PS","PS"],
    5: ["PS","NS","NS"],
    6: ["PL","ZE","NL"],
    7: ["ZE","NS","PS"],
    8: ["ZE","NM","PM"],
}


# given values for inputs
SPEED_DIFFERENCE = 100
ACCELERATION = 70


#fuzzification
def fuzzify(value,sets):
    return {k : get_membership(value,v) for k,v in sets.items()}


#fuzzify the inputs
speed_fuzzy = fuzzify(SPEED_DIFFERENCE,FUZZY_SETS)
print("Speed Fuzzy Values", speed_fuzzy)

accel_fuzzy = fuzzify(ACCELERATION, FUZZY_SETS)
print("Acceleration Fuzzy Values", accel_fuzzy)


#apply rules func
def apply_rules(speed_fuzzy,accel_fuzzy):
    return {i: (min(speed_fuzzy[s],accel_fuzzy[a]), o) for i , (s,a,o) in RULES.items() if min(speed_fuzzy[s],accel_fuzzy[a]) > 0}

rule_strengths = apply_rules(speed_fuzzy,accel_fuzzy)
print("Rule Strengths:", rule_strengths)


#area calc func
def calculate_areas(rule_strengths):
    areas , weighted_areas = {},{}
    for i, (strength, out) in rule_strengths.items():
        set_vals = FUZZY_SETS[out]
        center = set_vals[1] if len(set_vals) == 3 else (set_vals[1]+set_vals[2])/2

        if len(set_vals) == 4:
            base1 = set_vals[3] - set_vals[0]
            base2 = set_vals[2] - set_vals[1]
            area = strength * (base1 + base2)/2
        
        if len(set_vals) == 3:
            base = set_vals[2] - set_vals[0]
            area = strength * base/2

        areas[i] = area
        weighted_areas[i] = center*area
    return areas, weighted_areas


#defuzzification
def defuzzify(areas,weighted_areas):
    total_area = sum(areas.values())
    return sum (weighted_areas.values())/ total_area if total_area > 0 else 0


areas, weighted_areas = calculate_areas(rule_strengths)
throttle = defuzzify(areas, weighted_areas) #output


#visualization
def plot_fuzzy(fuzzy_sets, title,highlight_x=None):
    plt.figure(figsize=(10,6))
    x_val = np.linspace(0,255,500)

    for label, params in fuzzy_sets.items():
        y_vals = np.array([get_membership(x,params) for x in x_val])
        plt.plot(x_val,y_vals,label=label)

    if highlight_x is not None:
        plt.axvline(x=highlight_x,color='red',linestyle='--',label=f"Output: {highlight_x:.2f}")

    plt.title(title)
    plt.xlabel("Value")
    plt.ylabel("Membership")
    plt.legend()
    plt.grid(True)
    plt.show()

plot_fuzzy(FUZZY_SETS,"Speed Difference")
plot_fuzzy(FUZZY_SETS,"Acceleration")
plot_fuzzy(FUZZY_SETS,"Throttle output")

print(throttle)