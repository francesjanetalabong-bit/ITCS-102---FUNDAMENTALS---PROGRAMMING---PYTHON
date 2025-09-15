odd = 0
for x in range(1, 11,1): 
    name = eval(input("Enter a number: "))
    if name % 2:
        odd += name
print("The Sum of all odd number is",odd) 