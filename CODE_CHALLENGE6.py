factorial = eval(input("Enter a number --->  "))
variable = 1
for f in range(factorial,0,-1):
    variable *= f
print("the factorial of", factorial ,"is",variable)