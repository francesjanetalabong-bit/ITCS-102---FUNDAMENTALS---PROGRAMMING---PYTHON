import random



num = random.randint(1,21)

tries = 0
we = True

while we == True:
    g = int(input("What number do you think it is (1-21): "))
    tries += 1

    if g == num:
        print("Congratulations")
        print(f"The number is {num}")
        print(f"Your online took {tries} tries")
        break

    elif g > 10:
        print("Wrong input only 1-21")
        continue
    elif g < 1:
        print("Wrong input only 1-21")
        continue

    else:
        print("Sorry try again ")
        continue
