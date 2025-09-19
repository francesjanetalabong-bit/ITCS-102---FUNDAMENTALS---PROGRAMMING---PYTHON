even_sum = 0
for i in range(1, 11): 
    num = int(input(f"{i} - Enter a number --> "))  
    if num % 2 == 0:  
        even_sum += num  

print("The Sum of all even numbers is", even_sum)
