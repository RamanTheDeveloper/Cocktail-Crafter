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
from tabulate import tabulate

cwd = os.getcwd()
file_name = 'final_cocktails.csv'

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

def print_main_menu():
    '''
    This function will display the main menu
    '''
    print("\nMain Menu:")
    print("  1. Display all cocktails")
    print("  2. Search for a cocktail")
    print("  3. Random cocktail")
    print("  4. Information")
    print("  5. Exit")

def list_all_cocktails():
    '''
    This function will display all the cocktails in the list.
    '''
    file = get_file(file_name, cwd)

    print("\nAll Cocktails:")
    print("---------------------")
    
    headers = ['name', 'category']
    df = pd.DataFrame(file)
    if all(col in df.columns for col in headers):  # Ensure required columns exist
        filtered_df = df[headers]
        print(tabulate(filtered_df, headers='keys', tablefmt='psql', colalign=("left", "left")))
    else:
        print(f"Error: One or more columns {headers} are missing in the dataset.")

def main_menu():
    '''
    This function prompts the user to choose an option from the menu.
    '''
    while True:
        print("\nPlease choose an option from the menu (1-5):")
        
        # Input validation loop
        while True:
            try:
                user_input = int(input("Enter your choice: "))
                if not valid_input_main_menu(user_input):
                    continue  
                break  
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")
        
        # Main menu logic
        match user_input:
            case 1:
                list_all_cocktails()
                user_input = input("\nWhich cocktail would you like to view? (enter number): ")
                
                # Display the recipe for the selected cocktail
                display_cocktail_details(user_input)

            case 2:
                print("Search functionality coming soon!")
            
            case 3:
                print("Random cocktail feature coming soon!")
            
            case 4:
                print("Information section coming soon!")
            
            case 5:
                print("Exiting program!")
                exit()
            
            case _:
                print(f"Invalid choice {user_input}. Please try again.")

def display_cocktail_details(user_input):
    '''
    This function will display the recipe for the selected cocktail.
    '''
    file = get_file(file_name, cwd)
    headers = ['name', 'category', 'recipe']
    df = pd.DataFrame(file)
    
    if all(col in df.columns for col in headers):  # Ensure required columns exist
        filtered_df = df[headers]
        print(tabulate(filtered_df, headers='keys', tablefmt='psql', colalign=("left", "left")))
    else:
        print(f"Error: One or more columns {headers} are missing in the dataset.")

    # Get the recipe for the selected cocktail
    selected_cocktail = df.loc[df['name'] == user_input]
    print(selected_cocktail)


def valid_input_main_menu(user_input):
    '''
    This function will validate the user input and ensure that the input is a valid choice for the given context.
    '''
    if user_input < 1 or user_input > 5:
        print("Invalid input. Please enter a number between 1 and 5.")
        return False
    return True
    
def main():
    get_file(file_name, cwd)
    
    welcome_message()
    print_main_menu()
    
    main_menu()


if __name__ == "__main__":
    main()