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
  print("your name has ", len(name)," characters")
  
def ACTIVITY5():
  something =eval(input("Input something -->"))
  print("The data type of something is",type(something))
  answer = 6 + something
  print("the answer is ", answer)

def ACTIVITY6():
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

def ACTIVITY7():
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

def ACTIVITY8():
  balance = 9047
  withdrawal = 8217

  b = 18
  a = 17

  #print(b > a)

  name1 =  'Frances'
  name2 =  'Eunice'

  #print (b >= a )
  print(name1 != name2)
    
def ACTIVITY9():
  username = 'frances'
  password = 'eunice'

  #print(username == 'frances')
  #print(password == 'eunice')
  #print((username == 'frances') and (password == 'eunice'))
  #print((username == 'frances') or (password == 'eunice'))
  print(not((username == 'frances') or (password == 'eunice')))

def ACTIVITY10():
  #comments
  #jeepney fare
  #user would input their name
  #if user is student , student discount must be applied
  #20% discount on the student, if not student no discount

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
  
def ACTIVITY11():
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
  
def ACTIVITY12():
  for u in range (1 , 11):
    print(u, "hello world")
  
def ACTIVITY13():
  f = 21
  for e in range(1 ,21 ,1):
    j = eval(input("Enter the variable you want to compute ---> "))
    f += j
    print(f ,"New value of",j)
  print("total", f)
  
def ACTIVITY14():
  for u in range(21 ,0 ,-1):
    print(u ," Welcome to my ACTIVITY_14")
  #ascending and descending activity
  
def ACTIVITY15():
  even_sum = 0
  for i in range(1, 11): 
    num = int(input(f"{i} - Enter a number --> "))  
    if num % 2 == 0:  
        even_sum += num  
  print("The Sum of all even numbers is", even_sum) 
  
def ACTIVITY16():
  for f in range (1,22,1):
    for i in range (1,22,1):
        print(i,end="---> ")
    print()
    
def ACTIVITY17():
  #for f in range (1,22,1):
  #   for i in range (1,22,1):
  #     print(i,end=" ")
  #  print()

  for f in range (1,22):
      for i in range (1,f + 1):
          print(i,end=" ")
      print()
      
def ACTIVITY18():
  for f in range (1, 23, 1):
      for x in range(1, f, 1,):
        print(x, end = '  ')
      print()
  
def ACTIVITY19():
  for f in range(1, 23, 1):
      for x in range(1, f, 1):
        print("*" , end= '  ')
      print()

def ACTIVITY20():
  for f in range(1, 11, 1):
    for x in range(1, f, 1):
      print(">", end= '  ')
    for e in range(10, f, -1):
      print("*", end= "  ")
    print()
    
def ACTIVITY21():
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

def ACTIVITY22():
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
  
def ACTIVITY23():
  # months = ( "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", )
  # # print("months")
  # months.append ("AUGUST")

  full_name = "FRANCES JANE A. TALABONG" 
  name = list (full_name)
  print(name)

  for i in full_name[0 : 24]:
    print (i)
    
  name.reverse()
  print(name)

  
def ACTIVITY24():
  def welcoming(name): 
    print( f"Welcome too the Programming World. {name}!")


  def sum(f):
      sum = 21
      for i in range (f, 0, -1):
          sum = sum + i 
          print(i)
      print(f"The sum of number from f to 1 should be : {sum}")

  sum(4)
  sum(21)


  welcoming("Frances Jane")
  welcoming("Nica Ella")
  welcoming("Leslie Boy")
  welcoming("Marianne Mae")
  welcoming("John Say")

def ACTIVITY24_1():
  from ACTIVITY24 import welcoming, sum

  sum(24)

  welcoming("BSIT_1A")
  
def ACTIVITY25():
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
    print("your name has ", len(name)," characters")
    
  def ACTIVITY5():
    something =eval(input("Input something -->"))
    print("The data type of something is",type(something))
    answer = 6 + something
    print("the answer is ", answer)

  
def ACTIVITY25_1():
  from ACTIVITY25 import ACTIVITY1, ACTIVITY2, ACTIVITY3, ACTIVITY4, ACTIVITY5

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
          

  
def ACTIVITY26():
  programming_language = {'py': 'Python', 'j': 'Java', 'cs': 'C#', 'pl': 'Perl'}

  print(programming_language['py'])
  print(programming_language['j'])
  print(programming_language['cs'])
  print(programming_language['pl'])

  
def ACTIVITY27():
  print("Adding new title to the Dictionary")

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

def CODE_CHALLENGE1():
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


def CODE_CHALLENGE2():
    amount = int(input("Enter amount to deposit: "))
    denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 1]

    print("Here is a breakdown, using PH denomination:")
    remaining = amount

    for denom in denominations:
        count = remaining // denom
        remaining %= denom
        print(f"{count} - {denom}")


def CODE_CHALLENGE3():
    email = "francesjanetalabong@gmail.com"
    password = "secret"

    f = input("Email: ")
    t = input("Password: ")

    # Correct comparison using lower()
    if f.lower() == email and t.lower() == password:
        print("Correct password: Access granted")
    else:
        print("Invalid password: Access Denied")


def CODE_CHALLENGE4():
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print("The number is Even.")
    else:
        print("The number is Odd.")


def CODE_CHALLENGE5():
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


def CODE_CHALLENGE6():
    n = int(input("Enter a number ---> "))
    result = 1
    for i in range(1, n + 1):
        result *= i
    print("The factorial of", n, "is", result)


def CODE_CHALLENGE7():
    odd = 0
    for _ in range(10):
        num = int(input("Enter a number: "))
        if num % 2 == 1:
            odd += num
    print("The Sum of all odd numbers is", odd)


def CODE_CHALLENGE8():
    print("MULTIPLICATION TABLE MAKER")
    number = int(input("Please Enter a number --> "))
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")


def CODE_CHALLENGE9():
    print("WELCOME TO THE COUNTDOWN SIMULATOR!!!")
    start = int(input("Enter starting number --> "))
    print("\nCountdown started:")
    for i in range(start, 0, -1):
        print(i)
    print("Liftoff!")


def CODE_CHALLENGE10():
    for f in range(1, 11):
        for j in range(10, f, -1):
            print(" ", end=" ")
        for a in range(1, f):
            print("*", end=" ")
        for e in range(1, f):
            print("*", end=" ")
        print()


def CODE_CHALLENGE11():
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


def CODE_CHALLENGE12():
    for m in range(1, 7):
        for i in range(6, m, -1):
            print(" ", end=" ")
        for s in range(6, m, -1):
            print(" ", end=" ")
        for s in range(1, m):
            print("^", end=" ")
        print()


def CODE_CHALLENGE13():
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


def CODE_CHALLENGE14():
    identity = input("What is your name: ")
    odd = 0
    numb = ""

    while True:
        num = int(input("Put a number: "))
        if num % 2 == 1:
            print("Odd Detected")
            odd += num
            numb += str(num) + ","
        elif num == 0:
            print("Bye Bye")
            break
        else:
            print("Even spotted")
            print("NOT INCLUDED IN THE SUMMARY")
    print(f"Total of all odd numbers: {odd}")
    print(f"All odd numbers: {numb}")


def CODE_CHALLENGE15():
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
