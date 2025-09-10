print("Welcome to the Manga Library House! ")
print("Answer a few questions to find your next read.")
genre = input("What genre do you like? (action, romance, horror, fantasy, sci-fi): ")
length = input("How long should the manga be? (short, medium, long): ")
decade = input("Which decade? (2000s, 2010s, 2020s): ")

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

elif genre == "sci-fi":
    if length == "short" and decade == "2000s":
        print("Recommendation: Ghost in the Shell")
    elif length == "short" and decade == "2010s":
        print("Recommendation: Dr. Stone")
    elif length == "short" and decade == "2020s":
        print("Recommendation: To Your Eternity")
    elif length == "medium" and decade == "2000s":
        print("Recommendation: Nausicaä of the Valley of the Wind")
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
    print("Invalid genre. Please choose action, romance, horror, fantasy, or sci-fi.")
