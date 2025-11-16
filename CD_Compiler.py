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
