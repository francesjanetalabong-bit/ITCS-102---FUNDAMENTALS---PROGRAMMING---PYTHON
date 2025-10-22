# Anime list
# Using list and while loop

name = input("Enter your name before you start listing your Anime Title :) ")
print("Welcome to the Anime Title List,", name)
print("Anime Title List")

anime_list = []  # empty list

while True:
    anime = input("Enter the Title of the Anime (or type 'exit' to finish): ")

    if anime.lower() == 'exit':  # check first before adding
        print("\nAll done! You have exited the anime entry program.")
        print("Your anime list includes:")
        for a in anime_list:
            print(f"- {a}")
        break
    else:
        anime_list.append(anime)
        print("Anime added to the list!")

print(f"\nAll Anime in your list: {anime_list}")

