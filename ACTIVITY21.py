#while loop

frances = True

while frances == True:
    moon = input("(Yes or No): ")

    if moon.lower() == "yes":
        print("Continue")
        continue
    elif moon.lower() == "no":
        print("Stop")
        break
    else:
        print("Error input")
        continue