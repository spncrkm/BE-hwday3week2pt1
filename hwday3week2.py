# 1. Tuple Mastery in Python

# Objective:
# The aim of this assignment is to deepen your understanding of tuples in Python, along with their interaction with lists, dictionaries, and basic Python functionalities like functions, input handling, and string formatting. 
# By completing this assignment, you will enhance your skills in data structuring, manipulation, and application of tuples in practical scenarios.

# Task 1: Formatting Flight Itineraries
# Create a Python function that takes a list of tuples as an argument. Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). The function should format and return a string that lists 
# each itinerary. For example, if the input is [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")], the output should be a string formatted as:

# "Itinerary 1: Alice - From New York to London
#  Itinerary 2: Bob - From Tokyo to San Francisco"


itinerary_one = [("Alice", "New York", "London")]
itinerary_two = [("Bob", "Tokyo", "San Francisco")]


def travel_plan():

    for index, itinerary in enumerate(itinerary_one, start=1):
        print(f"Itinerary {index}: ", itinerary[0],"- ",itinerary[1],"to ",itinerary[2])
    
    for index, new_itinerary in enumerate(itinerary_two, start =1):
        print(f"Itinerary {index}: ", new_itinerary[0],"- ",new_itinerary[1],"to ",new_itinerary[2])
    
travel_plan()

# 2. Python Data Structure Challenges in Real-World Scenarios

# Task 1: Library System Enhancement
# Sharpen your skills in managing and modifying data within tuples and lists.

# Problem Statement:
# You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding new books and ensuring no duplicates.

# Existing Library Data: library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]


# Add functionality to insert new books into library.
# Ensure that adding a duplicate book is handled appropriately.

def add_book(library):

    title = input("Enter the title of the new book: ")
    author = input("Enter the author of the new book: ")

    new_book = (title, author)
    if new_book in library:
        print("This book already exists in the library.")
        return False
    else:
        library.append(new_book)
        print("Book added successfully.")
        return True

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

#Main loop
while True:
    action = input("Do you want to add a new book, display the current library, or exit the program? (yes/no/display): ").lower() 

    if action == 'yes':
        add_book(library)
    elif action == 'no':
        print("Quitting...")
        break
    elif action == 'display':
        print("Updated library:", library)
    else:
        print("Invalid input. Please enter 'yes', 'no' or 'display'.") 


# 3. Mastering Tuple Packing and Unpacking in Python
# Objective: The goal of this assignment is to deepen your understanding of tuple packing and unpacking in Python. You will apply these techniques in various practical scenarios, enhancing your ability to work with flexible data 
# structures and improve data handling efficiency.

# Task 1: Customer Order Processing Refine your skills in tuple unpacking by managing customer orders.

# Problem Statement: You are given a list of tuples, each representing a customer's order. Each tuple contains the customer's name, the product ordered, and the quantity. Your task is to unpack each tuple and print the order details in a user-friendly format.

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
]

for name, item, quantity in orders:
    print(f"{name} purchased {item} quantity of {quantity}.")