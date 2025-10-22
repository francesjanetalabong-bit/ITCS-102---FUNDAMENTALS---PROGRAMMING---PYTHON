#Anime list
#Using list and while loop
name = input("Enter your name before you start listing your Anime Title :) ")
print ("Welcome to the Anime Title List",  name )
print("Anime Title List")
print("*please enter  that's all, to end the list:")
anime = [] #empty list
entry = True   

while entry == True:
    num = input("Put a Title of the Anime: ")
    print("Anime Added to the List")
    anime.append(num) #new  title will be put in the bottom of the list
    if num == "that's all": #ending
        print("All done")
        anime.pop() #the word exit will be remove
        break

print(f"All Anime in your list {anime}") #will print all the anime tha the user listed 