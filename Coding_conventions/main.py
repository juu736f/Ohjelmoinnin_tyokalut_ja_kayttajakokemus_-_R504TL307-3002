def a(x):
    if x > 10: # tarkista onko x suurempi kuin 10
        print(f"x ({x}) is greater than 10")
    else: # jos ei suorita tämä
        print(f"x ({x}) is equal or less than 10")

def b(y):
    z = y * 2 # kerro y kahdella ja tallenna se z variableen
    if z < 20: # tarkista onko z pienempi kuin 20
        print(f"y times by 2 ({z}) is equal or less than 20")
    else: # jos ei suorita tämä
        print(f"y times by 2 ({z}) is greater than 20")

a(5) # kutsu funktiota a parametrilla 5
b(15) # kutsu funktiota b parametrilla 15
