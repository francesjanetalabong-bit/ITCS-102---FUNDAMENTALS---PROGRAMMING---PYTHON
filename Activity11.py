temp = eval(input("Enter temperature --> "))

if temp <= 0:
    print("Temperature outside is Cold")
elif temp >= 1 and temp <= 20:
    print("Temperature outside is Freezing Cold")
elif temp  >= 21 and temp <= 30:
    print("Temperature outside is Lukewarm")
elif temp  >= 31 and temp <= 40:
    print("Temperature outside is Warm")
elif temp >= 41 and temp <= 50:
    print("Temperature outside is Hot")
elif temp  >= 51:
    print("Temperature outside is Boiling Hot")
else:
    print("Invalid Temperature")
