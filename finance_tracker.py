# Capstone Project: Personal Finance Tracker
# This project is a command line program that allows the user to:
#   - Add an expense with a description, category and amount
#   - View all expenses
#   - View a summary of expenses by category

# This function prints a welcome message when the program starts.
def welcome_msg():
    print("Welcome to the Personal Finace Tracker!")

# This function adds a new expense to the dictionary 
def add_expenses(data):
    try:
        # Prompts the user for the expense description, category and amount
        # Checks if the input is valid 
        description = input("Enter expense description: ")
        if not description:
            raise ValueError("Description cannot be empty.")
        category = input("Enter category: ")
        if not category:
            raise ValueError("Categoty cannot be empty.")
        amount = float(input("Enter amount: "))
        if amount<0:
            raise ValueError("Amount cannot be negative")
        
        # Checks if the entered category is already in the dictionary
        # if its not create a new list for that category
        if category not in data:
            data[category] = []
        
        # Adds the description and amount to the correct category in the dictionary
        data[category].append((description, amount))
        print("Expense added successfully!")
    except ValueError as e:
        print(f"Invalid input: - {e}")
    except Exception as e:
        print(f"Unexpected Input: - {e}")
    # print(data)
    # pass

# This function prints all the categories and their expenses
def view_expenses(data):
    # Loop through the dictionary and get the category
    for category,expenses in data.items():
        print(f"Category {category}")
        # Loop to print the description and amount
        for description, amount in expenses:
            print(f"- {description}: ${amount}")

# This function shows the total amount spent per category
def view_summary(data):
    print("Summary:")
    for category, expenses in data.items():
        total=sum(amount for _, amount in expenses)
        print(f"{category}: ${total:.2f}")

def menu():
    print("What would you like to do?")
    # Get user response
    print("1. Add Expense\n2. View All Expenses\n3. View Summary\n4. Exit")
    user_Choice = int(input("Choose an option: "))
    return user_Choice

# Function call to print the welcome message 
welcome_msg()

# Gets the user input
choice=menu()

# Create empty dictionary
dict = {}

# Loop to continuously prompt the user 
while True:
    match(choice):
        case 1: # Case to add a new expense
            add_expenses(dict)
        case 2: # Case to view all expenses
            view_expenses(dict)
        case 3: # Case to view summary by category
            view_summary(dict)
        case 4: # Case to exit the program
            print("\nGoodbye!")
            exit()
        case _: # Case for invalid input
            print("Invalid Input!")
            exit()
    choice = menu()