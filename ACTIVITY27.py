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
