'''
Program: Cocktail Crafter
Author: Ramandeep Singh
Date: 24/22/2024
Summary: This program will allow the user to select a cocktail from a list of cocktails and display the recipe for the selected cocktail.
            Additionally, this program will display non trivial operations such as the total number of cocktails in the list, the average of ingredients used per cocktail as well as the most commonly used ingredient across all cocktails.

'''

import csv
import os
import pandas as pd

cwd = os.getcwd()
file_name = 'final_cocktails.csv'

def main():
    welcome_message()

    #file = get_file(file_name, cwd)
    #df = pd.DataFrame(file)
    #df.style()


def get_file(file_name, file_path):
    '''
    This function will load the data from the CSV file and return the data as a list of dictionaries.
    '''
    new_file = os.path.join(file_path, file_name)
    try:
        # Load the data from the CSV file
        with open(new_file, 'r') as file:
            cocktail_data = csv.DictReader(file)

            # Convert the data to a list of dictionaries
            data = list(cocktail_data)
            print("The file has been loaded successfully.\n")

        return data

    except FileNotFoundError:
        print(f"Error: The file {file_name} was not found. Please check the file path and try again.")

    except csv.Error as e:
        print(f"Error reading the CSV file: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def welcome_message():
    '''
    This function will display the welcome message to the user.
    '''
    banner = """
    ╔════════════════════════════════════════════════════╗
    ║                                                    ║
    ║       🍸 WELCOME TO THE COCKTAIL CRAFTER 🍸        ║
    ║                                                    ║
    ╚════════════════════════════════════════════════════╝
    """
    print(banner)
    print("  Your one-stop guide to delicious cocktail recipes!")
    print("\nInstructions:")
    print("  1. Browse the menu below.")
    print("  2. Type the number corresponding to your choice and press Enter.\n")


def count_cocktails(file):
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
    return cocktail_count

def main_menu():
    '''
    This function will display the main menu
    '''
    print("\nMain Menu:")
    print("  1. Display all cocktails")
    print("  2. Search for a cocktail")
    print("  3. Random cocktail")
    print("  4. Information")
    print("  5. Exit")