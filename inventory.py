from tabulate import tabulate

# Defined a class called 'Shoes'. The attributes of the class include details of the shoes
# the class also includes three functions to return cost, quantity and string representation of the class
class Shoes:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"Country: {self.country}\nCode: {self.code}\nProduct: {self.product}\nCost: {self.cost}\nQuantity: {self.quantity}\n"


# List updated through the 'read_shoes_data' with the shoe objects
shoe_objects = []

# Reads in the 'inventory.txt' file and creates an objects from the data on each line
# then it appends the 'shoe_objects' list with the each objects
# if the 'inventory.txt' file is not found an error message is returned to the user
# if the format of the 'inventory.txt' file is not correct an error message is returned
def read_shoes_data():
    try:
        with open("inventory.txt", "r") as inventory_data:
            line_number = 0
            for line in inventory_data:
                line_number += 1
                if line_number != 1:
                    clean_data = line.replace("\n", "").split(",")
                    new_object = Shoes(
                        clean_data[0],
                        clean_data[1],
                        clean_data[2],
                        int(clean_data[3]),
                        int(clean_data[4]),
                    )
                    shoe_objects.append(new_object)
    except FileNotFoundError as file_error:
        print(
            "\nFile not found. Please ensure the inventory file exists before running the program."
        )
        print(file_error)
        quit()
    except ValueError as error:
        print("Error. Please ensure the inventory data is correct.")
        print(error)
        quit()


# Function asks the user to enter details of the new item
# it checks if for 'cost' and 'quantity' the value entered is int if not it returns an error message
# and asks the suer to try it again
# then it creates a new object using the user inputs and appends the 'inventory.txt' and the 'shoe_objects' list file with the new data
def capture_shoes():
    print("Enter details of new item")
    country = input("Country: ")
    code = input("Code: ")
    product = input("Product: ")
    while True:
        try:
            cost = int(input("Cost: "))
            break
        except ValueError:
            print("Incorrect input. Please make sure input is number.")
    while True:
        try:
            quantity = int(input("Quantity: "))
            break
        except ValueError:
            print("Incorrect input. Please make sure input is number.")
    new_object = Shoes(country, code, product, cost, quantity)
    shoe_objects.append(new_object)
    with open("inventory.txt", "a") as inventor_data:
        inventor_data.write(f"\n{country},{code},{product},{cost},{quantity}")


# Shows all the products and details in a table format
def view_all():
    view_all_list = []
    for i in shoe_objects:
        view_all_list.append(
            [i.country] + [i.code] + [i.product] + [i.cost] + [i.quantity]
        )
    print(
        tabulate(
            view_all_list,
            headers=["Country", "Code", "Product", "Cost", "Quantity"],
            tablefmt="fancy_grid",
        )
    )


# Prints out the item with the smallest quantity
# then it asks the user if they want to 're-stock' the item
# if they choose 'yes' it asks for the new stock quantity then it updates the object's quantity value and
# writes the data to the 'inventory.txt' file
def re_stock():
    index = -1
    lowest_quantity = shoe_objects[0].quantity
    for i in shoe_objects:
        index += 1
        if shoe_objects[index].quantity < lowest_quantity:
            lowest_quantity = shoe_objects[index].quantity
            item = shoe_objects[index]
    print(item)
    choice = int(input("Would you like to re-stock this item?\n1 - Yes\n2 - No\n"))
    if choice == 1:
        item.quantity = int(input("Please enter new quantity: "))
        print(item)
    export_data()


# Writes out the data from 'shoe_objects' list to the 'inventory.txt' file
def export_data():
    with open("inventory.txt", "w") as inventor_data:
        for i in shoe_objects:
            inventor_data.write(
                f"{i.country},{i.code},{i.product},{i.cost},{i.quantity}\n"
            )


# Asks the user to enter the SKU code of the product they are looking for
# the it iterates through the 'shoe_object' list and if the item is found it prints out the details
# if the item was not found a not found text is printed to the console
def search_shoe():
    shoe_code = input("Please enter the item's SKU code: ")
    match = False
    for i in shoe_objects:
        if shoe_code == i.code:
            print(i)
            match = True
    if match == False:
        print("Item not found!")


# Calculates the total stock value for each product and prints out the product code, name and stock value in a table
def value_per_item():
    total_value_list = []
    for i in shoe_objects:
        total_value_list.append([i.code] + [i.product] + [i.quantity * i.cost])
    print(
        tabulate(
            total_value_list,
            headers=["SKU Code", "Product", "Total Value"],
            tablefmt="fancy_grid",
        )
    )


# Iterates through the 'shoe_objects' list and prints out the details of the item with the highest inventory quantity
def highest_qty():
    index = -1
    highest_quantity = shoe_objects[0].quantity
    for i in shoe_objects:
        index += 1
        if shoe_objects[index].quantity > highest_quantity:
            highest_quantity = shoe_objects[index].quantity
            item = shoe_objects[index]
    print("The below item has the highest inventory stock: ")
    print(item)


# Imports the inventory data
read_shoes_data()
# Prints out a welcome message to the user then it presents the menu options
# Functions are called based on the user input
# If input is not recognized an error message is returned
print("Welcome to Inventory Management 2022")
while True:
    menu = input(
        """    
    1 - Add a new product
    2 - View all products 
    3 - Re-stock 
    4 - Search 
    5 - Inventory value
    6 - Sales
    Q - Quit
    """
    ).lower()
    if menu == "1":
        capture_shoes()
    elif menu == "2":
        view_all()
    elif menu == "3":
        re_stock()
    elif menu == "4":
        search_shoe()
    elif menu == "5":
        value_per_item()
    elif menu == "6":
        highest_qty()
    elif menu == "q":
        print("Goodbye!")
        break
    else:
        print("Input not recognized, please try again.")
