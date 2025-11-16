def ACTIVITY1():
    print("Hello world")
    
def ACTIVITY2():
    print("Hi, What's your name?")
    
def ACTIVITY3():
    print("\tThe Quick Brown Fox \nJumps Over The Lazy Dog")
    print("The Quick Brown Fox \rJumps Over The Lazy Dog")
    print('"Always Do Your Best And God Will Do The Rest"')
    
def ACTIVITY4():
    name = input("Enter a string -> ")
    print("Your name has", len(name), "characters")
  
def ACTIVITY5():
    something = eval(input("Input something --> "))
    print("The data type of something is", type(something))
    answer = 6 + something
    print("The answer is", answer)

def ACTIVITY6():
    n1 = eval(input("Enter the first number: "))
    n2 = eval(input("Enter the second number: "))
    s = n1 + n2
    d = n1 - n2
    p = n1 * n2
    q = n1 / n2

    print("\nThe sum of", n1, "and", n2, "is", s)
    print("The difference of", n1, "and", n2, "is", d)
    print("The product of", n1, "and", n2, "is", p)
    print("The quotient of", n1, "and", n2, "is", q)
    print(n1, "exponent by", n2, "is", n1 ** n2)
    print("The remainder of", n1, "and", n2, "is", n1 % n2)
    print("The floor division of", n1, "and", n2, "is", n1 // n2)

def ACTIVITY7():
    a = 9 
    print("The value of a is", a)
    a += 9
    print("The value of a is", a)
    a = a + 9
    print("The value of a is", a)
    a += 0
    print("The value of a is", a)
    a += 8
    print("The value of a is", a)
    a *= 7
    print("The value of a is", a)
    a /= 21
    print("The value of a is", a)

def ACTIVITY8():  
    name1 = 'Frances'
    name2 = 'Eunice'
    print(name1 != name2)
  
def ACTIVITY9():
    username = 'frances'
    password = 'eunice'
    print(not ((username == 'frances') or (password == 'eunice')))

def ACTIVITY10():
    name = input("Input your name ---> ")
    isStudent = input("Are you a student (Yes/No) --> ")
    fare = eval(input("Bayad --> "))

    if isStudent.lower() == "yes":
        discount = fare * .2
        new_fare = fare - discount
        print("Hi", name, "student discount. Discounted fare is", new_fare)
    else: 
        print("Sorry", name, "you are not eligible for student discount") 
  
def ACTIVITY11():
    temp = eval(input("Enter temperature --> "))

    if temp <= 0:
        print("Temperature outside is Cold")
    elif 1 <= temp <= 20:
        print("Temperature outside is Freezing Cold")
    elif 21 <= temp <= 30:
        print("Temperature outside is Lukewarm")
    elif 31 <= temp <= 40:
        print("Temperature outside is Warm")
    elif 41 <= temp <= 50:
        print("Temperature outside is Hot")
    elif temp >= 51:
        print("Temperature outside is Boiling Hot")
    else:
        print("Invalid Temperature")
  
def ACTIVITY12():
    for u in range(1, 11):
        print(u, "Hello world")
  
def ACTIVITY13():
    f = 21
    for e in range(1, 21):
        j = eval(input("Enter the variable you want to compute ---> "))
        f += j
        print(f, "New value of", j)
    print("Total", f)
  
def ACTIVITY14():
    for u in range(21, 0, -1):
        print(u, "Welcome to my ACTIVITY_14")
  
def ACTIVITY15():
    even_sum = 0
    for i in range(1, 11):
        num = int(input(f"{i} - Enter a number --> "))
        if num % 2 == 0:
            even_sum += num  
    print("The sum of all even numbers is", even_sum) 
  
def ACTIVITY16():
    for f in range(1, 22):
        for i in range(1, 22):
            print(i, end="---> ")
        print()
    
def ACTIVITY17():
    for f in range(1, 22):
        for i in range(1, f + 1):
            print(i, end=" ")
        print()
      
def ACTIVITY18():
    for f in range(1, 23):
        for x in range(1, f):
            print(x, end='  ')
        print()
  
def ACTIVITY19():
    for f in range(1, 23):
        for x in range(1, f):
            print("*", end='  ')
        print()

def ACTIVITY20():
    for f in range(1, 11):
        for x in range(1, f):
            print(">", end='  ')
        for e in range(10, f, -1):
            print("*", end="  ")
        print()
    
def ACTIVITY21():
    frances = True

    while frances:
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

def ACTIVITY22():
    import random

    num = random.randint(1, 21)
    tries = 0

    while True:
        g = int(input("What number do you think it is (1-21): "))
        tries += 1

        if g == num:
            print("Congratulations")
            print(f"The number is {num}")
            print(f"You only took {tries} tries")
            break

        elif g > 21 or g < 1:
            print("Wrong input only 1-21")
            continue
        else:
            print("Sorry try again")
            continue
  
def ACTIVITY23():
    full_name = "FRANCES JANE A. TALABONG" 
    name = list(full_name)
    print(name)

    for i in full_name:
        print(i)
    
    name.reverse()
    print(name)

def ACTIVITY24():

    def welcoming(name): 
        print(f"Welcome to the Programming World, {name}!")

    def sum_numbers(f):
        total = 21
        for i in range(f, 0, -1):
            total += i
            print(i)
        print(f"The sum of numbers from f to 1 is: {total}")

    sum_numbers(4)
    sum_numbers(21)

    welcoming("Frances Jane")
    welcoming("Nica Ella")
    welcoming("Leslie Boy")
    welcoming("Marianne Mae")
    welcoming("John Say")

def ACTIVITY25_1():
    from ACTIVITY25 import ACTIVITY1, ACTIVITY2, ACTIVITY3, ACTIVITY4, ACTIVITY5

    name = input("What is your name: ")
    print(f"Welcome {name} to my File compiler")

    while True:
        print("Please Select a program:")
        print("A - ACTIVITY1\nB - ACTIVITY2\nC - ACTIVITY3\nD - ACTIVITY4\nF - ACTIVITY5\nE - Exit")

        new = input("What program would you like to run: ").lower()

        if new == "a":
            ACTIVITY1()
        elif new == "b":
            ACTIVITY2()
        elif new == "c":
            ACTIVITY3()
        elif new == "d":
            ACTIVITY4()
        elif new == "f":
            ACTIVITY5()
        elif new == "e":
            print("Thank you for visiting my programming compiler")
            break
        else:
            print("Please check your input")
          
def ACTIVITY26():
    programming_language = {'py': 'Python', 'j': 'Java', 'cs': 'C#', 'pl': 'Perl'}

    print(programming_language['py'])
    print(programming_language['j'])
    print(programming_language['cs'])
    print(programming_language['pl'])

def ACTIVITY27():
    print("Adding new title to the Dictionary")

    new = {}
    tr = True

    def search_title(ky):      
        print("Searching....")
        if ky in new:
            print(f"Result: {new[ky]}")
        else:
            print("Key not found!")

    def print_titles():
        for k, t in new.items():
            print(f"Key: {k}  New Title: {t}")

    while tr:
        key = input("Key to call the new title: ")
        title = input("Enter the new title: ")

        new[key] = title

        choice = input("Would you like to continue?\n" "y - Yes\n" "n - No\n" "p - Print\n" "s - Search\nTyping..... ").lower()

        if choice == "y":
            print("Continuing...")
        elif choice == "n":
            print("Exiting....")
            print("Program Stop")
            break
        elif choice == "p":
            print("=========================")
            print("Printing....")
            print_titles()
            print("=========================")
        elif choice == "s":
            search = input("Enter the key to search: ")
            search_title(search)
        else:
            print("Error! Invalid Choice")
