# Ask user for deposit amount
amount = int(input("Enter amount to deposit: "))

# List of denominations in pesos
denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 1]

print("Here is a breakdown, using PH denomination:")

# Loop through each denomination
remaining = amount
for denom in denominations:
    count = remaining // denom
    remaining %= denom
    print(f"{count} - {denom}")
