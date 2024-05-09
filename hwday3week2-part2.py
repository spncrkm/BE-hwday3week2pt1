# 1. Python Sets Adventure
# Objective:
# The aim of this assignment is to deepen your understanding and application of Python sets in various scenarios, ranging from basic operations to advanced manipulations and best practices. You will correct given codes, use sets in everyday contexts, 
# and tackle challenges that require creative thinking and problem-solving.

# Task 1: Flight Route Comparison
# Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. You have two sets of flight destinations, one for each airline. Write a Python program to find out:



# 1. Destinations that both airlines fly to.
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

same_destination = our_routes.intersection(competitor_routes)
print(same_destination)

# 2. Destinations unique to your airline.
unique_destination = our_routes.difference(competitor_routes)
# printing unique destination of our_routes
print(unique_destination)

# 3. Whether there are any destinations that neither airline shares.
non_sharing_flights = our_routes.symmetric_difference(competitor_routes)
# taking both sets and printing flights that do not have the same destinations
print(non_sharing_flights)



# 2. Set Operations in Data Analysis
# Objective:
# The aim of this assignment is to enhance your skills in using Python sets for data analysis tasks. You will apply various set operations to handle real-world data scenarios, focusing on their practical application and efficiency.

# Task 1: Duplicate Entries Cleanup
# You are given a list of customer IDs, some of which are duplicated. Write a Python script to remove duplicates and display the unique customer IDs.

# Example Code:
customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]


removed_duplicates = set(customer_ids)
# after removing duplicates then printing in order
print(sorted(removed_duplicates))