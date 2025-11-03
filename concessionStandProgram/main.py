# Create a dictionary called 'menu' that stores food items (keys) and their prices (values)
menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "Lemonade": 4.25}

# Create an empty list to store the items that the user selects
cart = []

# Initialize the total cost variable to 0
total = 0

# Print a title for the menu section
print("------------MENU-------------")

# Loop through all key-value pairs in the menu dictionary
# 'key' represents the food name, 'value' represents the price
for key, value in menu.items():
    # Print each item and its price neatly formatted
    # {key:10} means the item name takes up 10 character spaces (for alignment)
    # ${value:.2f} formats the price to 2 decimal places
    print(f"{key:10}: ${value:.2f}")

# Print a separator line for better readability
print("-----------------------------")

# Start an infinite loop to repeatedly ask the user to choose food items
while True:
    # Ask the user to select a food item or press 'q' to quit
    # .lower() converts the input to lowercase to make it case-insensitive
    food = input("Select an item (q to quit): ").lower()

    # If the user enters 'q', exit (break) the loop
    if food == "q":
        break

    # Check if the entered food exists in the menu dictionary
    elif menu.get(food) is not None:
        # If it exists, add it to the shopping cart list
        cart.append(food)

# After the user quits, print all items in their cart
print(cart)
print()  # Print an empty line for spacing

# Print a separator before showing the order summary
print("-----------------------------")

# Loop through each food item in the cart
for food in cart:
    # Add the price of each food to the total using menu.get(food)
    total += menu.get(food)

    # Print the food item names in a single line separated by spaces
    print(food, end=" ")

print()  # Move to the next line after printing all items

# Finally, print the total price formatted to 2 decimal places
print(f"Total is: ${total:.2f}")
