from ACTIVITY25 import *

name  = input("Whats is your name: ")

print(f"Welcome {name} to my File compiler")

t = True

while t == True:
    print("Please Select a program based on your interest")
    print("A - ACTIVITY1\nB - ACTIVITY2\nC - ACTIVITY3\nD - ACTIVITY4\nF - ACTIVITY5\nE - Exit")

    new = input("What program would you like to run in the ff. option: ").lower()

    if new == "A":
        ACTIVITY1()
        continue
    elif new == "B":
        ACTIVITY2()
        continue
    elif new == "C":
        ACTIVITY3()
        continue
    elif new == "D":
        ACTIVITY4()
    elif new == "F":
        ACTIVITY5()
    elif new == "e":
        print("Thank you for visiting my programming compiler")
        break
    else:
        print("Please check if you input correctly")
        
