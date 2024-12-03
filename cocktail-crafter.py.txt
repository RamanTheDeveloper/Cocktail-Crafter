'''
Program: Cocktail Crafter
Author: Ramandeep Singh
Date: 24/22/2024
Summary: This program will allow the user to select a cocktail from a list of cocktails and display the recipe for the selected cocktail.
            Additionally, this program will display non trivial operations such as the total number of cocktails in the list, the average of ingredients used per cocktail as well as the most commonly used ingredient across all cocktails.

'''

import csv

file_name = '/Users/ramandeep.singh/Abertay Uni/Python Projects/Cocktail-Crafter/final_cocktails.csv'

try:
    # Load the data from the CSV file
    with open(file_name, 'r') as file:
        cocktail_data = csv.reader(file)

        try:
            # Skip the header row
            header = next(cocktail_data)
        except StopIteration:
            print('The file is empty')
            exit()

        #Count the number of disinct cocktails
        cocktail_count = 0
        for row in cocktail_data:
            if row:
                cocktail_count += 1

    # Display the total number of cocktails
    print("The file has been loaded successfully.\n")
    print(f'Total number of cocktails found: {cocktail_count}')

except FileNotFoundError:
    print(f"Error: The file {file_name} was not found. Please check the file path and try again.")

except csv.Error as e:
    print(f"Error reading the CSV file: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")