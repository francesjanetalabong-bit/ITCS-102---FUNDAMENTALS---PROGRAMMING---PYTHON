def intro():
    print("\t+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\n\t\t\t\t\tWELCOME TO MY PROGRAMMING CLASSES COMPILER\t\t\t\n")
    print("\t+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    print("\n\tHello! I am Frances Jane A. Talabong", "BSIT_1A_STUDENT")
    print("\n\tThis is a compilation of all of my activities \n and code_challenges from our python programming class")
    print("\n\tYou can explore the Python concepts, practice coding\n, and test things safely base on your curiosity")
    print("\n\tSUBJECT: ITCS_102 - INTRODUCTION TO PROGRAMMING")
    print("\n\tSCHOOL: DALUBHASAAN NG LUNGSOD NG LUCENA")
    print("\n\tProfessor: Mr. Leonard Andrew D. Mesiera")
    print("\n\tProgram Head: Mr.Leonard Andrew D. Mesiera")

import random 
import json
import os
import pygame

def prt():
    print("\n\t==============================================================================================")
    print("\n\t\t\t\t\t\tPRINT FUNCTION ") 
    print("\n\t==============================================================================================")

def act1():
    print("Hello World")

def act3():
    print("\tThe Quick Brown Fox \nJumps Over The Lazy Dog")
    print("The Quick Brown Fox \rJumps Over The Lazy Dog")
    print('"Always Do Your Best And God Will Do The Rest"')

def cc1():
    name = input("Type your name -> ")
    print("\t\t\t\t*\n"
            "\t\t\t*\t\t*\n"
            "\t\t*\t\t\t\t*\n"
            "\t*\t\t\tHi\t\t\t*\n"
            "*\t\t\t" + name + "\t\t\t\t*\n"
            "\t*\t\t\t\t\t\t*\n"
            "\t\t*\t\t\t\t*\n"
            "\t\t\t*\t\t*\n"
            "\t\t\t\t*")

def str():
    print("\n\t==============================================================================================")
    print("\n\t\t\t\t\tSTRING AND INPUT FUNCTION ") 
    print("\n\t==============================================================================================")
#  act2, act4, act 5, and cc3
def act2():
    print("Hi, What's your name? ")

    name = input("Enter your name:")
    print("hello!,", name)

def act4():
    name = input("Enter a string -> ")

    print("your name has ", len(name)," characters")

def act5():
    something =eval(input("Input something -->"))
    print("The data type of something is",type(something))

    answer = 6 + something
    print("the answer is ", answer)

def cc3():

    email = "francesjanetalabong@gmail.com"
    password = "secret"

    f = input("Email: ")
    t = input("Password: ")

        # Correct comparison using lower()
    if f.lower() == email and t.lower() == password:
        print("Correct password: Access granted")
    else:
        print("Invalid password: Access Denied")

def art():
    print("\n\t==============================================================================================")
    print("\n\t\t\t\t\t\tARITHMETIC FUNCTION ") 
    print("\n\t==============================================================================================")
# act 6, act7,cc4,cc6, and cc8
def act6():
    n1 = eval(input("Enter the first number :"))
    n2 = eval(input("Enter the second number :"))
    s = n1 + n2
    d = n1 - n2
    p = n1 * n2
    q = n1 / n2

    print("\nthe sum of",n1,"and",n2,"is",s)
    print("The difference of",n1,"and",n2,"is",d)
    print("The product of",n1,"and",n2,"is",p)
    print("The quotient of",n1,"and",n2,"is",q)
    print(n1, "exponent by",n2,"is",n1**n2)
    print("The remainder of",n1,"and",n2,"is",n1%n2)
    print("The floor division of",n1,"and",n2,"is",n1//n2)

def act7():
    a = 9 
    print("the value of a is ", a)
    a += 9

    a = a + 9
    print("the value of a is ", a)
    a += 0
    print("the value of a is ", a)
    a += 8
    print("the value of a is ", a)
    a *= 7
    print("the value of a is ", a)
    a  /= 21
    print("the value of a is ", a)

def cc2():
    amount = int(input("Enter amount to deposit: "))
    denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 1]

    print("Here is a breakdown, using PH denomination:")
    remaining = amount

    for denom in denominations:
        count = remaining // denom
        remaining %= denom
        print(f"{count} - {denom}")

def cc4():
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print("The number is Even.")
    else:
        print("The number is Odd.")

def cc6():
    n = int(input("Enter a number ---> "))
    result = 1
    for i in range(1, n + 1):
        result *= i
    print("The factorial of", n, "is", result)

def cc7():
    odd = 0
    for _ in range(10):
        num = int(input("Enter a number: "))
        if num % 2 == 1:
            odd += num
    print("The Sum of all odd numbers is", odd)

def cc8():

    print("MULTIPLICATION TABLE MAKER")
    number = int(input("Please Enter a number --> "))
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

def cond():
    print("\n\t==============================================================================================")
    print("\n\t\t\t\t\t\tCONDITIONAL FUNCTION ") 
    print("\n\t==============================================================================================")
#  act8, act9, act10,act11, and cc5

def act8():
    balance = 9047
    withdrawal = 8217

    b = 18
    a = 17

    #print(b > a)

    name1 =  'Frances'
    name2 =  'Eunice'

    #print (b >= a )
    print(name1 != name2)

def act9():
    username = 'frances'
    password = 'eunice'

    #print(username == 'frances')
    #print(password == 'eunice')
    #print((username == 'frances') and (password == 'eunice'))
    #print((username == 'frances') or (password == 'eunice'))
    print(not((username == 'frances') or (password == 'eunice')))

def act10():
    name = input("Input your name ---> ")
    isStudent = input("Are you a student (Yes/No) --> ")
    fare = eval(input("bayad --> "))

    if isStudent.lower()== "yes":
        discount = fare * .2
        new_fare = fare - discount
        print("Hi" , name, "student discount"
                " Discounted fare is ", new_fare)
    else: 
        print("Sorry ", name," you are not eligible for  student discount") 
        
def act11():
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

def cc5():
    print("Welcome to the Manga Library House! ")
    print("Answer a few questions to find your next read.")
    genre = input("What genre do you like? (action, romance, horror, fantasy, sci-fi): ").lower()
    length = input("How long should the manga be? (short, medium, long): ").lower()
    decade = input("Which decade? (2000s, 2010s, 2020s): ")

        # === ACTION ===
    if genre == "action":
        if length == "short" and decade == "2000s":
            print("Recommendation: Black Lagoon")
        elif length == "short" and decade == "2010s":
            print("Recommendation: One Punch Man")
        elif length == "short" and decade == "2020s":
            print("Recommendation: Jujutsu Kaisen")
        elif length == "medium" and decade == "2000s":
            print("Recommendation: Naruto")
        elif length == "medium" and decade == "2010s":
            print("Recommendation: Attack on Titan")
        elif length == "medium" and decade == "2020s":
            print("Recommendation: Demon Slayer")
        elif length == "long" and decade == "2000s":
            print("Recommendation: Bleach")
        elif length == "long" and decade == "2010s":
            print("Recommendation: My Hero Academia")
        elif length == "long" and decade == "2020s":
            print("Recommendation: Chainsaw Man")
        else:
            print("Sorry, no action manga matches your selection.")

        # === ROMANCE ===
    elif genre == "romance":
        if length == "short" and decade == "2000s":
            print("Recommendation: Lovely★Complex")
        elif length == "short" and decade == "2010s":
            print("Recommendation: Ao Haru Ride")
        elif length == "short" and decade == "2020s":
            print("Recommendation: Kubo Won't Let Me Be Invisible")
        elif length == "medium" and decade == "2000s":
            print("Recommendation: Fruits Basket")
        elif length == "medium" and decade == "2010s":
            print("Recommendation: Kimi ni Todoke")
        elif length == "medium" and decade == "2020s":
            print("Recommendation: Rent-A-Girlfriend")
        elif length == "long" and decade == "2000s":
            print("Recommendation: Boys Be...")
        elif length == "long" and decade == "2010s":
            print("Recommendation: Domestic Girlfriend")
        elif length == "long" and decade == "2020s":
            print("Recommendation: The Quintessential Quintuplets")
        else:
            print("Sorry, no romance manga matches your selection.")

        # === HORROR ===
    elif genre == "horror":
        if length == "short" and decade == "2000s":
            print("Recommendation: Another")
        elif length == "short" and decade == "2010s":
            print("Recommendation: I Am a Hero")
        elif length == "short" and decade == "2020s":
            print("Recommendation: Dandadan")
        elif length == "medium" and decade == "2000s":
            print("Recommendation: Hellsing")
        elif length == "medium" and decade == "2010s":
            print("Recommendation: Tokyo Ghoul")
        elif length == "medium" and decade == "2020s":
            print("Recommendation: Kaiju No. 8")
        elif length == "long" and decade == "2000s":
            print("Recommendation: Uzumaki")
        elif length == "long" and decade == "2010s":
            print("Recommendation: Ajin")
        elif length == "long" and decade == "2020s":
            print("Recommendation: Jujutsu Kaisen")
        else:
            print("Sorry, no horror manga matches your selection.")

        # === FANTASY ===
    elif genre == "fantasy":
        if length == "short" and decade == "2000s":
            print("Recommendation: Cardcaptor Sakura")
        elif length == "short" and decade == "2010s":
            print("Recommendation: The Ancient Magus' Bride")
        elif length == "short" and decade == "2020s":
            print("Recommendation: The Apothecary Diaries")
        elif length == "medium" and decade == "2000s":
            print("Recommendation: Fullmetal Alchemist")
        elif length == "medium" and decade == "2010s":
            print("Recommendation: The Rising of the Shield Hero")
        elif length == "medium" and decade == "2020s":
            print("Recommendation: The Beginning After the End")
        elif length == "long" and decade == "2000s":
            print("Recommendation: Fairy Tail")
        elif length == "long" and decade == "2010s":
            print("Recommendation: Re:Zero")
        elif length == "long" and decade == "2020s":
            print("Recommendation: The Faraway Paladin")
        else:
            print("Sorry, no fantasy manga matches your selection.")

        # === SCI-FI ===
    elif genre == "sci-fi":
        if length == "short" and decade == "2000s":
            print("Recommendation: Ghost in the Shell")
        elif length == "short" and decade == "2010s":
            print("Recommendation: Dr. Stone")
        elif length == "short" and decade == "2020s":
            print("Recommendation: To Your Eternity")
        elif length == "medium" and decade == "2000s":
            print("Recommendation: Nausicaä")
        elif length == "medium" and decade == "2010s":
            print("Recommendation: Steins;Gate")
        elif length == "medium" and decade == "2020s":
            print("Recommendation: Blame!")
        elif length == "long" and decade == "2000s":
            print("Recommendation: Planetes")
        elif length == "long" and decade == "2010s":
            print("Recommendation: Knights of Sidonia")
        elif length == "long" and decade == "2020s":
            print("Recommendation: Attack on Titan")
        else:
            print("Sorry, no sci-fi manga matches your selection.")
    else:
        print("Invalid genre.")   

def fl():
    print("\n\t==============================================================================================")
    print("\n\t\t\t\t\t\tFOR LOOP FUNCTION ") 
    print("\n\t==============================================================================================")
# act12, act13, act 14, act15, act16, 
def act12():
    for u in range (1 , 11):
        print(u, "hello world")

def act13():
    f = 21
    for e in range(1 ,21 ,1):
        j = eval(input("Enter the variable you want to compute ---> "))
        f += j
        print(f ,"New value of",j)
    print("total", f)
    
def act14():
    for u in range(21 ,0 ,-1):
        print(u ," Welcome to my ACTIVITY_14")
  #ascending and descending activity
  
def act15():
    even_sum = 0
    for i in range(1, 11): 
        num = int(input(f"{i} - Enter a number --> "))  
        if num % 2 == 0:  
            even_sum += num  
    print("The Sum of all even numbers is", even_sum) 

def act16():
    for f in range (1,22,1):
        for i in range (1,22,1):
            print(i,end="---> ")
        print()

def act17():
    for f in range (1,22):
        for i in range (1,f + 1):
              print(i,end=" ")
        print()

def act18():
    for f in range (1, 23, 1):
        for x in range(1, f, 1,):
            print(x, end = '  ')
        print()
  
def act19():
    for f in range(1, 23):
        for x in range(1, f):
            print("*", end='  ')
        print()

def act20():
    for f in range(1, 11):
        for x in range(1, f):
            print(">", end='  ')
        for e in range(10, f, -1):
            print("*", end='  ')
        print()

def act23():
    full_name = "FRANCES JANE A. TALABONG" 
    name = list (full_name)
    print(name)

    for i in full_name[0 : 24]:
        print (i)
        
    name.reverse()
    print(name)

def cc9():
    print("WELCOME TO THE COUNTDOWN SIMULATOR!!!")
    start = int(input("Enter starting number --> "))
    print("\nCountdown started:")
    for i in range(start, 0, -1):
        print(i)
    print("Liftoff!")

def cc10():
    for f in range(1, 11):
        for j in range(10, f, -1):
            print(" ", end=" ")
        for a in range(1, f):
            print("*", end=" ")
        for e in range(1, f):
            print("*", end=" ")
        print()

def cc11():
    for f in range(1, 11):
        for j in range(10, f, -1):
            print(" ", end=" ")
        for a in range(1, f):
            print("*", end=" ")
        for e in range(1, f):
            print("*", end=" ")
        print()

    for f in range(1, 11):
        for j in range(1, f):
            print(" ", end=" ")
        for a in range(10, f, -1):
            print("*", end=" ")
        for e in range(10, f, -1):
            print("*", end=" ")
        print()

def cc12():
    for m in range(1, 7):
        for i in range(6, m, -1):
            print(" ", end=" ")
        for s in range(6, m, -1):
            print(" ", end=" ")
        for s in range(1, m):
            print("^", end=" ")
        print()

def cc13():
    # Christmas Tree
    for f in range(2, 6):
        for r in range(7):
            print(" ", end=" ")
        for a in range(6, f, -1):
            print(" ", end=" ")
        for n in range(3, f):
            print("^", end=" ")
        for c in range(2, f):
            print("^", end=" ")
        print()

    for e in range(1, 3):
        for s in range(7):
            print(" ", end=" ")
        for a in range(2, e, -1):
            print("^", end=" ")
        for n in range(3, e, -1):
            print("^", end=" ")
        print()

    for a in range(2, 9):
        for u in range(12, a, -1):
            print(" ", end=" ")
        for s in range(2, a):
            print("^", end=" ")
        for b in range(1, a):
            print("^", end=" ")
        print()

    for t in range(2, 10):
        for i in range(12, t, -1):
            print(" ", end=" ")
        for v in range(1, t):
            print("^", end=" ")
        for e in range(2, t):
            print("^", end=" ")
        print()

    for a in range(2, 13):
        for f in range(12, a, -1):
            print(" ", end=" ")
        for j in range(1, a):
            print("^", end=" ")
        for t in range(2, a):
            print("^", end=" ")
        print()

    for s in range(1, 7):
        for x in range(1, 9):
            print(" ", end=" ")
        for y in range(1, 9):
            print("^", end="")
        print()
  
def wl():
    print("\n\t==============================================================================================")
    print("\n\t\t\t\t\t\tWHILE LOOP FUNCTION ") 
    print("\n\t==============================================================================================")

def act21():
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

def act22():
    import random

    num = random.randint(1,10)

    tries = 0
    we = True

    while we == True:
        g = int(input("What number do you think it is (1-10): "))
        tries += 1

        if g == num:
            print("Congratulations")
            print(f"The number is {num}")
            print(f"Your online took {tries} tries")
            break

        elif g > 10:
            print("Wrong input only 1-10")
            continue
        elif g < 1:
            print("Wrong input only 1-10")
            continue

        else:
            print("Sorry try again ")
            continue
def act23():
    full_name = "FRANCES JANE A. TALABONG"

    # Convert the string to a list of characters
    name_list = [char for char in full_name]  
    print("List of characters:", name_list)

    # Print each character individually
    print("\nCharacters individually:")
    for char in full_name:
        print(char)

    # Reverse the list
    reversed_list = name_list[::-1]  # safer than using .reverse()
    print("\nReversed list of characters:", reversed_list)


def act24():

    # Welcoming function
    def welcoming(name):
        print(f"Welcome to the Programming World, {name}!")

    # Summation function
    def summation(f):
        total = 0
        print(f"\nCounting down from {f} to 1:")
        for i in range(f, 0, -1):
            total += i
            print(i)
        print(f"Total sum = {total}\n")

    # Call examples
    summation(4)
    summation(21)

    welcoming("Frances Jane")
    welcoming("Nica Ella")
    welcoming("Leslie Boy")
    welcoming("Marianne Mae")
    welcoming("John Say")

    return welcoming, summation

def act24_1():
    # Get welcoming() and summation() from act24()
    welcoming, summation = act24()
    # Use the functions
    summation(24)
    welcoming("BSIT_1A")

def act25():

    # ACTIVITY 1
    def ACTIVITY1():
        print("Hello world")

    # ACTIVITY 2
    def ACTIVITY2():
        print("Hi, what's your name?")

    # ACTIVITY 3
    def ACTIVITY3():
        print("\tThe Quick Brown Fox \nJumps Over The Lazy Dog")
        print("The Quick Brown Fox \rJumps Over The Lazy Dog")
        print('"Always Do Your Best And God Will Do The Rest"')

    # ACTIVITY 4
    def ACTIVITY4():
        name = input("Enter a string -> ")
        print("Your name has", len(name), "characters")

    # ACTIVITY 5
    def ACTIVITY5():
        something = eval(input("Input something --> "))
        print("The data type of something is", type(something))
        answer = 6 + something
        print("The answer is", answer)

    # RETURN ALL ACTIVITY FUNCTIONS SO OTHER FUNCTIONS CAN USE THEM
    return ACTIVITY1, ACTIVITY2, ACTIVITY3, ACTIVITY4, ACTIVITY5

def act25_1():
    # Load all activities from act25()
    ACTIVITY1, ACTIVITY2, ACTIVITY3, ACTIVITY4, ACTIVITY5 = act25()

    name = input("What is your name: ")
    print(f"\nWelcome {name} to my File Compiler!")

    while True:
        print("\nPlease select a program:")
        print("A - ACTIVITY 1")
        print("B - ACTIVITY 2")
        print("C - ACTIVITY 3")
        print("D - ACTIVITY 4")
        print("F - ACTIVITY 5")
        print("E - Exit")

        choice = input("\nChoose an option: ").lower()

        if choice == "a":
            ACTIVITY1()

        elif choice == "b":
            ACTIVITY2()

        elif choice == "c":
            ACTIVITY3()

        elif choice == "d":
            ACTIVITY4()

        elif choice == "f":
            ACTIVITY5()

        elif choice == "e":
            print("\nThank you for visiting my programming compiler.")
            break

        else:
            print("Invalid choice. Please try again.")

def cc14():
    identity = input("What is your name: ")
    odd_total = 0
    odd_numbers = []

    while True:
        num = int(input("Put a number: "))

        if num == 0:
            print("Bye Bye")
            break

        if num % 2 == 1:
            print("Odd Detected")
            odd_total += num
            odd_numbers.append(num)

        else:
            print("Even spotted")
            print("NOT INCLUDED IN THE SUMMARY")

    # FIX: Restore built-in str in case it was overwritten
    import builtins
    str = builtins.str

    print("\n========== SUMMARY ==========")
    print(f"Name: {identity}")
    print(f"Total of all odd numbers: {odd_total}")

    if odd_numbers:
        print("All odd numbers:", ", ".join(map(str, odd_numbers)))
    else:
        print("No odd numbers were entered.")


def cc15():
    name = input("Enter your name before you start listing your Anime Title :) ")
    print("Welcome to the Anime Title List,", name)

    anime_list = []

    while True:
        anime = input("Enter the Title of the Anime (or type 'exit' to finish): ")
        if anime.lower() == "exit":
            print("\nAll done! You have exited the anime entry program.")
            print("Your anime list includes:")
            for a in anime_list:
                print(f"- {a}")
            break
        else:
            anime_list.append(anime)
            print("Anime added to the list!")

    print(f"\nAll Anime in your list: {anime_list}")
    
def cc16(): 
    import os
    import json

    os.system('cls')
    print("STUDENT INFORMATION SYSTEM")
    print("===========================")

    student_records = {}

    while True: 
        print("SELECT FROM THE OPTIONS BELOW")
        print("A - Add Information")
        print("B - Print All Records")
        print("C - Search a Student Record")
        print("D - Delete a Student Record")
        print("E - Edit a Student Record")
        print("F - Export Data")
        print("G - Import Record")
        print("X - Exit")
        
        choice = input("Your choice --->  ").lower()
        os.system('cls')

        # ------------------ A: ADD RECORD ------------------
        if choice == 'a':
            print("ADDING STUDENT INFORMATION")
            print("----------------------------")

            student_id = input("Student ID ---> ").lower()
            first_name = input("Enter first name ---> ").upper()
            last_name = input("Enter last name ---> ").upper()
            course = input("Enter course ---> ").upper()
            email = input("Email address ---> ")

            student_records[student_id] = [first_name, last_name, course, email]

            print("\nDATA SAVED!\n")
            continue

        # ------------------ B: PRINT ALL RECORDS ------------------
        elif choice == 'b':
            print("PRINTING STUDENT RECORDS")
            print("--------------------------")

            if not student_records:
                print("No records found.")
            else:
                for id, record in student_records.items():
                    print(f"ID: {id}  ->  {record}")

            print()
            continue

        # ------------------ C: SEARCH RECORD ------------------
        elif choice == 'c':
            print("SEARCH STUDENT RECORD")
            print("-----------------------")

            search_id = input("Enter ID to search ---> ").lower()

            if search_id in student_records:
                print("\nRECORD FOUND:")
                for item in student_records[search_id]:
                    print(f"-- {item}")
            else:
                print("\nNO RECORD FOUND")

            print()
            continue

        # ------------------ D: DELETE RECORD ------------------
        elif choice == 'd':
            print("DELETE STUDENT RECORD")
            print("------------------------")

            search_id = input("Enter ID to delete ---> ").lower()

            if search_id in student_records:
                print("\nRECORD FOUND:")
                for item in student_records[search_id]:
                    print(f"-- {item}")
                
                student_records.pop(search_id)
                print("\nRECORD DELETED!")
            else:
                print("\nNO RECORD FOUND")

            print()
            continue

        # ------------------ E: EDIT RECORD ------------------
        elif choice == 'e':
            print("EDIT STUDENT RECORD")
            print("----------------------")

            search_id = input("Enter ID to edit ---> ").lower()

            if search_id in student_records:
                print("\nRECORD FOUND:")
                for i in student_records[search_id]:
                    print(f"-- {i}")

                print("\nEnter NEW details:")
                first_name = input("Enter first name ---> ").upper()
                last_name = input("Enter last name ---> ").upper()
                course = input("Enter course ---> ").upper()
                email = input("Email address ---> ")

                student_records[search_id] = [first_name, last_name, course, email]

                print("\nDATA UPDATED!")
            else:
                print("\nNO RECORD FOUND")

            print()
            continue

        # ------------------ F: EXPORT TO JSON ------------------
        elif choice == 'f':
            print("EXPORTING STUDENT RECORDS...")

            with open('student_record.json', 'w') as new_file:
                json.dump(student_records, new_file, indent=4)

            print("DATA EXPORTED TO student_record.json\n")
            continue

        # ------------------ G: IMPORT FROM JSON ------------------
        elif choice == 'g':
            print("IMPORTING STUDENT RECORD...")

            try:
                with open('student_record.json', 'r') as new_file:
                    student_records = json.load(new_file)
                print("DATA IMPORTED!\n")
            except FileNotFoundError:
                print("JSON FILE NOT FOUND.\n")

            continue

        # ------------------ X: EXIT ------------------
        elif choice == 'x':
            print("SYSTEM EXIT")
            break

        # ------------------ INVALID OPTION ------------------
        else:
            print("INVALID CHOICE, PLEASE TRY AGAIN.\n")

def list():
    print("\n\t==============================================================================================")
    print("\n\t\t\t\t\t\t LIST FUNCTION ") 
    print("\n\t==============================================================================================")

def act26():
    programming_language = {'py': 'Python', 'j': 'Java', 'cs': 'C#', 'pl': 'Perl'}

    print(programming_language['py'])
    print(programming_language['j'])
    print(programming_language['cs'])
    print(programming_language['pl'])   

def dict():
    print("\n\t==============================================================================================")
    print("\n\t\t\t\t\t\tDICTIONARY LIST FUNCTION ") 
    print("\n\t==============================================================================================")

def act27():
    new = {}     # dictionary to store titles
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

        new[key] = title   # store in dictionary

        choice = input("Would you like to continue?\n""y - Yes\n" "n - No\n" "p - Print\n" "s - Search\n" "Typing..... ").lower()

        if choice == "y":
            print("Continuing...")
            continue

        elif choice == "n":
            print("Exiting....")
            print("Program Stop")
            break

        elif choice == "p":
            print("=========================")
            print("Printing....")
            print_titles()
            print("=========================")
            continue

        elif choice == "s":
            search = input("Enter the key to search: ")
            search_title(search)
            continue

        else:
            print("Error! Invalid Choice")


    import os
    import json
    os.system('cls')
    print("STUDENT INFORMATION SYSTEM")
    print("===========================")


    student_records = {}

    while True: 
        print("SELECT FROM THE OPTIONS BELOW")
        print("A-Add Information")
        print("B-Print All Record")
        print("C-Search a Student Record")
        print("D-Delete a Student Record")
        print("E-Edit a Student Record")
        print("F-Export Data")
        print("G-Import Record")
        print("X-Exit")
        choice = input("Your choice   ------>  ").lower()
        os.system('cls')
        if choice == 'a':

            print("ADDING STUDENT INFORMATION")
            print("----------------------------")
            student_id = input("Key search for this student information ID ------>").lower()

            first_name = input("Enter the student first name ---->").upper()
            last_name =input("Input student last name ------->").upper()
            course = input("Input Student Course------>").upper()
            email = input("Student email address -->")

            student_records[student_id] = [first_name, last_name, course, email]
            print("DATA SAVED")

            os.system('cls')
            continue
        
        elif choice =='b': 
            os.system('cls')
            print("PRINTING STUDENT RECORD")

            for id,record in student_records.items():
                print(f"STUDENT ID {id} in STUDENT RECORD {record}")
            continue

        elif choice =='c':
            os.system('cls')
            print("SEARCH STUDENT RECORD")
            print("=========================")

            search_id = input("Input ID to search ----> ")

            for id in student_records.keys():
                if search_id in student_records.keys():
                    print("=====================================")
                    print("\n\nRECORD FOUND")
                    print("=====================================")
                    for i in student_records[search_id]:
                        print(f"-- {i}")
                else:
                    print("=====================================")
                    print("\n\n NO RECORD FOUND")
                    print("=====================================")
                break
            continue

        elif choice == 'd':
            os.system('cls')
            print("DELETE EXISTING RECORD")
            print("=========================")

            search_id = input("Input ID to delete ----> ").lower()
            
            for id in student_records.keys():
                if search_id in student_records.keys():
                    print("=====================================")
                    print("\n\nRECORD FOUND")
                    print("=====================================")
                    for i in student_records[search_id]:
                        print(f"-- {i}")

                    student_records.pop(search_id)
                    print("RECORD DELETED")
                else:
                    print("=====================================")
                    print("\n\n NO RECORD FOUND")
                    print("=====================================")
                break
            continue    

        elif choice == 'e':
            os.system('cls')
            print("EDIT/MODIFY STUDENT RECORD")
            print("=========================")

            search_id = input("Input ID to edit ----> ").lower()

            for id in student_records.keys():
                if search_id in student_records.keys():
                    print("=====================================")
                    print("\n\nRECORD FOUND")
                    print("=====================================")

                    for i in student_records[search_id]:
                        print(f"-- {i}")
                    

                    first_name = input("Enter the student first name ---->").upper()
                    last_name =input("Input student last name ------->").upper()
                    course = input("Input Student Course------>").upper()
                    email = input("Student email address -->").upper()

                    student_records[search_id][0] = first_name
                    student_records[search_id][1] = last_name
                    student_records[search_id][2] = course
                    student_records[search_id][3] =  email

                    print("DATA UPDATED")
                
                else:
                    print("=====================================")
                    print("\n\nRECORED DELETED")
                    print("=====================================")
                break
            continue 

        elif choice == 'f':
            os.system("cls")
            print("EXPORTING STUDENT RECORD")
            
            with open('student_record.json', 'w') as new_file:
                json.dump(student_records,new_file, indent=4)
        
            print("DATA EXPORTED TO JSON")

            continue 

        elif choice =='g':
            os.system('cls')
            print("Import Student Record")

            with open('student_record.json', 'r') as new_file:
                student_json = json.load(new_file)

            student_records = student_json
            print("DATA IMPORTED TO JSON")

            continue

        elif choice == 'x': 
            print("SYSTEM EXIT")
            break

        else:
            print("INVALID CHOICE, PLEASE RE-ENTER YOUR CHOICE")

# I'll categorize and arrange it correctly later on  

def act28():
    import pygame
    import time
    import random

    pygame.init()

    width = 600
    height = 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Snake Game')

    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)

    clock = pygame.time.Clock()
    speed = 10
    snake_block = 10

    font_style = pygame.font.SysFont(None, 30)

    def draw_snake(snake_list):
        for block in snake_list:
            pygame.draw.rect(screen, green, [block[0], block[1], snake_block, snake_block])

    def game_loop():
        game_over = False
        game_close = False

        x = width / 2
        y = height / 2

        x_change = 0
        y_change = 0

        snake_list = []
        length_of_snake = 1

        food_x = round(random.randrange(0, width - snake_block) / 10) * 10
        food_y = round(random.randrange(0, height - snake_block) / 10) * 10

        while not game_over:

            while game_close:
                screen.fill(black)
                msg = font_style.render('You Lost! Q-Quit | C-Play Again', True, red)
                screen.blit(msg, [width / 6, height / 3])
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        elif event.key == pygame.K_c:
                            game_loop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -snake_block
                        y_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x_change = snake_block
                        y_change = 0
                    elif event.key == pygame.K_UP:
                        y_change = -snake_block
                        x_change = 0
                    elif event.key == pygame.K_DOWN:
                        y_change = snake_block
                        x_change = 0

            if x >= width or x < 0 or y >= height or y < 0:
                game_close = True

            x += x_change
            y += y_change
            screen.fill(black)
            pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])

            snake_head = [x, y]
            snake_list.append(snake_head)

            if len(snake_list) > length_of_snake:
                del snake_list[0]

            for segment in snake_list[:-1]:
                if segment == snake_head:
                    game_close = True

            draw_snake(snake_list)
            pygame.display.update()

            if x == food_x and y == food_y:
                food_x = round(random.randrange(0, width - snake_block) / 10) * 10
                food_y = round(random.randrange(0, height - snake_block) / 10) * 10
                length_of_snake += 1

            clock.tick(speed)

        pygame.quit()

    game_loop()

import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Interactive mode function
def run_interactive(activity_name, description, example):
    clear()
    print("="*60)
    print(f"Interactive Mode - {activity_name}")
    print("="*60)
    print(description + "\n")
    print("EXAMPLE:")
    print(example + "\n")
    print("Now you can try your own Python code below. Type 'exit()' to leave interactive mode.")
    print("="*60)
    while True:
        try:
            user_input = input(">>> ")
            if user_input.strip() == 'exit()':
                break
            else:
                exec(user_input)
        except Exception as e:
            print(f"Error: {e}")

def main_menu():
    while True : 
        clear()
        print("=================================================")
        print("\n \tWELCOME TO MY PROGRAMMING COMPILER \n")
        print("=================================================")

        print("=================================================")
        print("Hello! I am Frances Jane A. Talabong," "BSIT_1A")
        print("This is my finals project that will contain \n all of my activities and code_challenges\n ")
        print("Subject: ITCS_102 - INTRODUCTION TO PROGRAMMING")
        print("School: Dalubhasaan ng Lungsod ng Lucena")
        print("Professor: Mr. Leonard Andrew D. Mesiera")
        print("=================================================\n")

        print("===============================================")
        print("\t\tMAIN MENU")
        print("===============================================")

        print("1. Print Funnctions")
        print("2. String and Input")
        print("3. Arithmetic Function")
        print("4. conditional Function")
        print("5. For Loop Function")
        print("6. While Loop Function")
        print("7. List Function")
        print("8. Dictionary Function")
        print("9. Games")
        print("10. Code Challenges")
        print("0", "Exit")
        print("-----------------------------------------------")
        choice = input("Enter your choice (0-10):").strip()

        if choice == '1': print_menu()
        elif choice == '2': string_menu()
        elif choice == '3': arithmetic_menu()
        elif choice == '4': conditional_menu()
        elif choice == '5': for_loop_menu()
        elif choice == '6': while_loop_menu()
        elif choice == '7': list_menu()
        elif choice == '8': dictionary_menu()
        elif choice == '9': games_menu()
        elif choice == '10': code_challenges_menu()
        elif choice == '0': 
            print("\nGoodbye! Thank you for using the complier. See you next time \n")
            break
        else:
            input("Invalid choice. PLease ENTER to continue:")

# ------------------- PRINT MENU -------------------
def print_menu():
    while True:
        clear()
        print("========================================================")
        print("\t\tPRINT FUNCTION")
        print("========================================================")
        print("→ Demonstrates basic output using the print() function.")
        print("→ Used to display text, variables, and results to the user.\n")
        print("Here are some activities that mainly use Print Function:")
        print("You can try any activity listed below upon choosing. ")
        print("========================================================")
        print("\n1. Say Hello (act1)")
        print("2. Displaying text (act3)")
        print("\n0. Back to the Menu\n")
        print("========================================================")

        choice = input("Choose a program:  ").strip()

        if choice == '1':
            act1()
            input("\nPress ENTER to continue...")

            run_interactive(
                "act1",
                "This activity demonstrates printing text using the \nprint() function.",
                ">>> print('Hello World')"
            )
            input("\nPress ENTER to continue...")
        elif choice == '2':
            act3()
            input("\nPress ENTER to continue...")

            run_interactive(
                "act3",
                "This activity demonstrates displaying text using \nprint() function.",
                ">>> print('Welcome to Python!')"
            )
            input("\nPress ENTER to continue...")
        elif choice == '0':
            break
        else:
            input("Invalid choice. Press ENTER....")

# ------------------- STRING & INPUT MENU -------------------
def string_menu():
    while True:
        clear()
        print("=============================================================")
        print("\t\tSTRING & INPUT FUNCTION")
        print("=============================================================")
        print("→Teaches how to work with text (strings).")
        print("→Explains concatenation, formatting, and accepting user input.\n")
        print("Here are some activities that mainly use strings and input:")
        print("You can try any activity listed below upon choosing. ")
        print("=============================================================")
        print("\n1. Ask Name & Greet (act2)")
        print("2. Count Characters (act4)")
        print("3. Data Type Checker Number (act5)")
        print("4. Login Simulator (cc3)")
        print("\n0. Back to the Menu\n")
        print("=============================================================")

        choice = input("Choose a program:  ").strip()

        if choice == '1':
            act2()
            input("\nPress ENTER to continue...")
            run_interactive(
                "act2",
                "This activity asks for the user's name and greets them.",
                ">>> name = input('Enter your name: ')\n>>> print('Hello,', name)"
            )
            input("\nPress ENTER to continue...")
        elif choice == '2':
            act4()
            input("\nPress ENTER to return to the menu...")
            run_interactive(
                "act4",
                "Counts the number of characters in a string.",
                ">>> text = 'Python'\n>>> print(len(text))"
            )
            input("\nPress ENTER to continue...")
        elif choice == '3':
            act5()
            input("\nPress ENTER to continue...")
            run_interactive(
                "act5",
                "Checks the data type of user input.",
                ">>> value = input('Enter a number: ')\n>>> print(type(value))"
            )
            input("\nPress ENTER to continue...")
        elif choice == '4':
            cc3()
            input("\nPress ENTER to continue...")
            run_interactive(
                "cc3",
                "Simulates a login system.",
                ">>> username = input('Username: ')\n>>> password = input('Password: ')\n>>> print('Login Successful')"
            )
            input("\nPress ENTER to continue...")
        elif choice == '0':
            break
        else:
            input("Invalid choice. Press ENTER....")

# ------------------- ARITHMETIC MENU -------------------
def arithmetic_menu():
    while True:
        clear()
        print("========================================================")
        print("\t\tARITHMETIC FUNCTION")
        print("========================================================")
        print("→ Performs mathematical operations such as +, -, *, /, \n%, //, **.")
        print("→ Useful for calculations, formulas, and numeric problem\n solving.\n")
        print("Here are some activities that mainly use arithmetic\n operations:")
        print("You can try any activity listed below upon choosing. ")
        print("========================================================")
        print("\n1. Basic Computations (act6)")
        print("2. Variable Operations (act7)")
        print("3. Money Denomination (cc2)")
        print("4. Even or Odd Checker (cc4)")
        print("5. Factorial Calculator (cc6)")
        print("6. Multiplication Table (cc8)")
        print("\n0. Back to the Menu\n")
        print("========================================================")

        choice = input("Choose a program:  ").strip()

        if choice == '1':
            act6()
            input("\nPress ENTER to continue...")
            run_interactive(
                "act6",
                "Performs basic arithmetic operations.",
                ">>> a = 10\n>>> b = 5\n>>> print(a + b, a - b, a * b, a / b)"
            )
            input("\nPress ENTER to continue...")
        elif choice == '2':
            act7()
            input("\nPress ENTER to continue...")
            run_interactive(
                "act7",
                "Demonstrates arithmetic with variables.",
                ">>> x = 15\n>>> y = 3\n>>> print(x + y, x ** y)"
            )
            input("\nPress ENTER to continue...")
        elif choice == '3':
            cc2()
            input("\nPress ENTER to continue...")
            run_interactive(
                "cc2",
                "Calculates money denominations.",
                ">>> amount = 576\n>>> hundreds = amount // 100\n>>> print(hundreds)"
            )
            input("\nPress ENTER to continue...")
        elif choice == '4':
            cc4()
            input("\nPress ENTER to continue...")
            run_interactive(
                "cc4",
                "Checks if a number is even or odd.",
                ">>> num = 7\n>>> print('Even' if num % 2 == 0 else 'Odd')"
            )
            input("\nPress ENTER to continue...")
        elif choice == '5':
            cc6()
            input("\nPress ENTER to continue...")
            run_interactive(
                "cc6",
                "Calculates factorial of a number.",
                ">>> import math\n>>> print(math.factorial(5))"
            )
            input("\nPress ENTER to continue...")
        elif choice == '6':
            cc8()
            input("\nPress ENTER to continue...")
            run_interactive(
                "cc8",
                "Displays multiplication table of a number.",
                ">>> for i in range(1, 11):\n...     print('5 x', i, '=', 5*i)"
            )
            input("\nPress ENTER to continue...")
        elif choice == '0':
            break
        else:
            input("Invalid choice. Press ENTER....")

# ------------------- CONDITIONAL MENU -------------------
def conditional_menu():
    while True:
        clear()
        print("============================================================")
        print("\t\tCONDITIONAL FUNCTION")
        print("============================================================")
        print("→ Introduces decision-making using if, elif, else.")
        print("→ Allows the program to react differently based on conditions.\n")
        print("Here are some activities that mainly use Conditional statements:")
        print("You can try any activity listed below upon choosing. ")
        print("============================================================")
        print("\n1. Comparison and Booleans (act8)")
        print("2. Logical Operators (act9)")
        print("3. Student Discount (act10)")
        print("4. Temperature Checker (act11)")
        print("5. Manga Recommendation (cc5)")
        print("\n0. Back to the Menu\n")
        print("============================================================")

        choice = input("Choose a program:  ").strip()

        if choice == '1':
            act8()
            input("\nPress ENTER to continue...")
            run_interactive(
                "act8",
                "This activity demonstrates comparison operators and boolean logic.",
                ">>> a = 5\n>>> b = 10\n>>> print(a < b)\n>>> print(a == b)"
            )
            input("\nPress ENTER to continue...")
        elif choice == '2':
            act9()
            input("\nPress ENTER to continue...")
            run_interactive(
                "act9",
                "This activity uses logical operators (and, or, not)\n to evaluate conditions.",
                ">>> x = True\n>>> y = False\n>>> print(x and y)\n>>> print(x or y)"
            )
            input("\nPress ENTER to continue...")
        elif choice == '3':
            act10()
            input("\nPress ENTER to continue...")
            run_interactive(
                "act10",
                "This activity calculates student discounts based on conditions.",
                ">>> age = 18\n>>> discount = 0.1 if age < 20 else 0\n>>> print(discount)"
            )
            input("\nPress ENTER to continue...")
        elif choice == '4':
            act11()
            input("\nPress ENTER to continue...")
            run_interactive(
                "act11",
                "This activity checks the temperature and prints recommendations.",
                ">>> temp = 30\n>>> if temp > 25:\n...     print('Hot')\n... else:\n...     print('Cool')"
            )
            input("\nPress ENTER to continue...")
        elif choice == '5':
            cc5()
            input("\nPress ENTER to continue...")
            run_interactive(
                "cc5",
                "This activity recommends a manga based on a given genre.",
                ">>> genre = 'Action'\n>>> print('Try My Hero Academia!' if genre=='Action' else 'Try Naruto!')"
            )
            input("\nPress ENTER to continue...")
        elif choice == '0':
            break
        else:
            input("Invalid choice. Press ENTER....")

# ------------------- FOR LOOP MENU -------------------
def for_loop_menu():
    while True:
        clear()
        print("========================================================")
        print("\t\tFOR LOOP FUNCTION")
        print("========================================================")
        print("→ Demonstrates loops that run a fixed number of times.")
        print("→ Useful for repetition, list processing, and generating \nsequences.\n")
        print("Here are some activities that mainly use For Loops:")
        print("You can try any activity listed below upon choosing. ")
        print("========================================================")
        print("\n1. Print Hello (act12)")
        print("2. Sum Numbers (act13)")
        print("3. Countdown (cc9)")
        print("4. Sum Even Numbers (act15)")
        print("5. Print Sequence (act16)")
        print("6. Triangle Pattern (act17)")
        print("7. Pyramid Patterns (act18,19,20)")
        print("8. List Characters (act23)")
        print("9. Pattern Maker (cc12)")
        print("\n0. Back to the Menu\n")
        print("========================================================")

        choice = input("Choose a program:  ").strip()

        if choice == '1':
            act12()
            input("\nPress ENTER to continue...")
            run_interactive(
                "act12",
                "Prints 'Hello' multiple times using a for loop.",
                ">>> for i in range(5):\n...     print('Hello')"
            )
            input("\nPress ENTER to continue...")
        elif choice == '2':
            act13()
            input("\nPress ENTER to continue...")
            run_interactive(
                "act13",
                "Sums numbers from 1 to 10 using a for loop.",
                ">>> total = 0\n>>> for i in range(1,11):\n...     total += i\n>>> print(total)"
            )
            input("\nPress ENTER to continue...")
        elif choice == '3':
            cc9()
            input("\nPress ENTER to continue...")
            run_interactive(
                "cc9",
                "Counts down from 10 to 1 using a for loop.",
                ">>> for i in range(10,0,-1):\n...     print(i)"
            )
            input("\nPress ENTER to continue...")
        elif choice == '4':
            act15()
            input("\nPress ENTER to continue...")
            run_interactive(
                "act15",
                "Sums all even numbers from 1 to 20.",
                ">>> total = 0\n>>> for i in range(2,21,2):\n...     total += i\n>>> print(total)"
            )
            input("\nPress ENTER to continue...")
        elif choice == '5':
            act16()
            input("\nPress ENTER to continue...")
            run_interactive(
                "act16",
                "Prints a sequence of numbers from 1 to 10.",
                ">>> for i in range(1,11):\n...     print(i)"
            )
            input("\nPress ENTER to continue...")
        elif choice == '6':
            act17()
            input("\nPress ENTER to continue...")
            run_interactive(
                "act17",
                "Prints a triangle pattern using for loops.",
                ">>> for i in range(1,6):\n...     print('*'*i)"
            )
            input("\nPress ENTER to continue...")
        elif choice == '7':
            act18()
            input("\nPress ENTER to continue...") 
            act19()
            input("\nPress ENTER to continue...")
            act20()
            input("\nPress ENTER to continue...")
            run_interactive(
                "act18-20",
                "Prints pyramid patterns of stars.",
                ">>> for i in range(1,6):\n...     print(' '*(5-i) + '*'*(2*i-1))"
            )
            input("\nPress ENTER to continue...")
        elif choice == '8':
            act23()
            input("\nPress ENTER to continue...")
            run_interactive(
                "act23",
                "Prints each character of a string individually.",
                ">>> text = 'Python'\n>>> for char in text:\n...     print(char)"
            )
            input("\nPress ENTER to continue...")
        elif choice == '9':
            cc12()
            input("\nPress ENTER to continue...")
            run_interactive(
                "cc12",
                "Creates a custom pattern based on user input.",
                ">>> for i in range(1,6):\n...     print('*'*i)"
            )
            input("\nPress ENTER to continue...")
        elif choice == '0':
            break
        else:
            input("Invalid choice. Press ENTER....")
# ------------------- WHILE LOOP MENU -------------------
def while_loop_menu():
    while True:
        clear()
        print("=============================================================")
        print("\tWHILE LOOP FUNCTION")
        print("=============================================================")
        print("→ Shows loops that continue running while a condition is true.")
        print("→ Useful for input validation and repeated actions.\n")
        print("Here are some activities that mainly use While Loops:")
        print("You can try any activity listed below upon choosing. ")
        print("=============================================================")
        print("\n1. YES / NO loop (act21)")
        print("2. Guess Number Game (act22)")
        print("3. Welcome and Summation Functions (act24)")
        print("4. Run Activity 24 Functions (act24_1)")
        print("5. File Compiler Example (act25_1)")
        print("\n0. Back to the Menu\n")
        print("=============================================================")

        choice = input("Choose a program:  ").strip()

        if choice == '1':
            act21()
            input("\nPress ENTER to continue...")
            run_interactive(
                "act21",
                "Keeps asking user a YES/NO question until a valid response is given.",
                ">>> answer = ''\n>>> while answer.lower() not in ['yes','no']:\n...     answer = input('YES or NO? ')"
            )
            input("\nPress ENTER to continue...")
        elif choice == '2':
            act22()
            input("\nPress ENTER to continue...")
            run_interactive(
                "act22",
                "Guess a number game using while loop.",
                ">>> number = 7\n>>> guess = 0\n>>> while guess != number:\n...     guess = int(input('Guess number: '))"
            )
            input("\nPress ENTER to continue...")
        elif choice == '3':
            act24()
            input("\nPress ENTER to continue...")
            run_interactive(
                "act24",
                "Demonstrates welcome message and summation using while loops.",
                ">>> i = 1\n>>> total = 0\n>>> while i <= 5:\n...     total += i\n...     i += 1\n>>> print(total)"
            )
            input("\nPress ENTER to continue...")
        elif choice == '4':
            act24_1()
            input("\nPress ENTER to continue...")
            run_interactive(
                "act24_1",
                "Runs additional functions from Activity 24 interactively.",
                ">>> def add(a,b):\n...     return a+b\n>>> print(add(5,7))"
            )
            input("\nPress ENTER to continue...")
        elif choice == '5':
            act25_1()
            input("\nPress ENTER to continue...")
            run_interactive(
                "act25_1",
                "Demonstrates a simple file compiler example using Python.",
                ">>> with open('test.txt','w') as f:\n...     f.write('Hello World')"
            )
            input("\nPress ENTER to continue...")
        elif choice == '0':
            break
        else:
            input("Invalid choice. Press ENTER....")

# ------------------- LIST MENU -------------------
def list_menu():
    while True:
        clear()
        print("=============================================================")
        print("\t\tLIST FUNCTION")
        print("=============================================================")
        print("→Explains lists: ordered, changeable collections of items.")
        print("→Demonstrates adding, removing, sorting, and accessing values.\n")
        print("Here are some activities that mainly use lists:")
        print("You can try any activity listed below upon choosing. ")
        print("=============================================================")
        print("\n1. Anime Title List (cc15)")
        print("\n0. Back to the Menu\n")
        print("==============================================================")

        choice = input("Choose a program:  ").strip()

        if choice == '1':
            cc15()
            input("\nPress ENTER to continue...")
            run_interactive(
                "cc15",
                "Demonstrates creating a list of anime titles and printing them.",
                ">>> anime_list = ['Naruto','One Piece','Attack on Titan']\n>>> print(anime_list)"
            )
            input("\nPress ENTER to continue...")
        elif choice == '0':
            break
        else:
            input("Invalid choice. Press ENTER....")

# ------------------- DICTIONARY MENU -------------------
def dictionary_menu():
    while True:
        clear()
        print("================================================================")
        print("\t\tDICTIONARY FUNCTION")
        print("================================================================")
        print("→Shows how to store data using key-value pairs.")
        print("→Useful for labeled information (name, age, student info, etc.).\n")
        print("Here are some activities that mainly use dictionaries:")
        print("You can try any activity listed below upon choosing. ")
        print("================================================================")
        print("\n1. Student Information System (cc16)")
        print("\n0. Back to the Menu\n")
        print("================================================================")
        choice = input("Choose a program:  ").strip()

        if choice == '1':
            cc16()
            input("\nPress ENTER to continue...")
            run_interactive(
                "cc16",
                "Demonstrates storing and retrieving student information using dictionary.",
                ">>> student = {'name':'John','age':20,'course':'BSIT'}\n>>> print(student['name'])"
            )
            input("\nPress ENTER to continue...")
        elif choice == '0':
            break
        else:
            input("Invalid choice. Press ENTER....")

# ------------------- GAMES MENU -------------------
def games_menu():
    while True:
        clear()
        print("========================================================")
        print("\t\tGAME FUNCTION")
        print("========================================================")
        print("→ Contains mini-games made using programming logic.")
        print("→ Examples: guess-the-number, rock-paper-scissors, quizzes.\n")
        print("Here are some activities that mainly use game logic:")
        print("You can try any activity listed below upon choosing. ")
        print("========================================================")
        print("\n1. Snake Game (act28)")
        print("\n0. Back to the Menu\n")
        print("========================================================")

        choice = input("Choose a program:  ").strip()

        if choice == '1':
            act28()
            run_interactive(
                "act28",
                "Demonstrates a simple Snake Game logic (text-based example).",
                ">>> print('Use arrow keys to move the snake!')"
            )
            input("\nPress ENTER to continue...")
        elif choice == '0':
            break
        else:
            input("Invalid choice. Press ENTER....")

# ------------------- CODE CHALLENGES MENU -------------------
def code_challenges_menu():
    while True:
        clear()
        print("================================================================")
        print("\t\tCODE CHALLENGES FUNCTION")
        print("================================================================")
        print("→ Compilation of exercises that test logic and programming skills.")
        print("→ Includes loops, conditions, strings, math, and more.\n")
        print("Here are some activities for Code Challenges:")
        print("You can try any activity listed below upon choosing. ")
        print("================================================================")
        print("\n1. Print Your Name in Art (cc1)")
        print("2. Odd Number Sum (cc14)")
        print("\n0. Back to the Menu\n")
        print("================================================================")

        choice = input("Choose a program:  ").strip()

        if choice == '1':
            cc1()
            input("\nPress ENTER to continue...")
            run_interactive(
                "cc1",
                "Prints your name in ASCII art or stylized letters.",
                ">>> print('F R A N C E S')"
            )
            input("\nPress ENTER to continue...")
        elif choice == '2':
            cc14()
            input("\nPress ENTER to continue...")
            run_interactive(
                "cc14",
                "Sums all odd numbers within a given range.",
                ">>> total = sum(i for i in range(1,11) if i%2 !=0)\n>>> print(total)"
            )
            input("\nPress ENTER to continue...")
        elif choice == '0':
            break
        else:
            input("Invalid choice. Press ENTER....")

if __name__ == '__main__':
        intro()
        main_menu()

