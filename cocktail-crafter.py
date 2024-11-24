'''
Program: Cockatil Crafter
Author: Ramandeep Singh
Date: 24/22/2024
Summary: This program will allow the user to select a cocktail from a list of cocktails and display the recipe for the selected cocktail.

'''

import csv

# Load the data from the CSV file
with open('final_cocktails.csv', 'r') as file:
    cocktail_data = csv.reader(file)

    # Skip the header row
    next(cocktail_data)

    #Count the number of disinct cocktails
    cocktail_count = 0
    for row in cocktail_data:
        cocktail_count += 1

# Display the total number of cocktails
print(f'Total number of cocktails: {cocktail_count}')