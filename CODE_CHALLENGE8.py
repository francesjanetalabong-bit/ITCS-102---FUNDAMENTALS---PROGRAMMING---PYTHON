# Program to print the multiplication table for a random number variable
print("MULTIPLICATION TABLE MAKER")
number = int(input("Please Enter a number --> "))
# Loop to print multiplication table range (1,10)
for f in range(1, 11):
        print(f"{number} x {f} = {number * f}")

