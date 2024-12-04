'''
Program: Cocktail Crafter
Author: Ramandeep Singh
Date: 24/22/2024
Summary: This program will allow the user to select a cocktail from a list of cocktails and display the recipe for the selected cocktail.
            Additionally, this program will display non trivial operations such as the total number of cocktails in the list, the average of ingredients used per cocktail as well as the most commonly used ingredient across all cocktails.

'''

import ast
import csv
import os
import random
from typing import Counter
import pandas as pd
from tabulate import tabulate

cwd = os.getcwd()
file_name = 'final_cocktails.csv'

def clear():
    '''
    This function will clear the terminal screen.
    '''
    os.system('cls' if os.name == 'nt' else 'clear')

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
    try:
        with open(file_name, 'r') as file:
            cocktail_data = csv.reader(file)
            # Skip the header row
            try:
                header = next(cocktail_data)
            except StopIteration:
                print('The file is empty')
                exit()
            #Count the number of disinct cocktails
            cocktail_count = sum(1 for row in cocktail_data if row)  # Count non-empty rows
        return cocktail_count
    except FileNotFoundError:
        print('The file is empty')
        exit()

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
                break

            case 2:
                search_cocktail()
                break
            
            case 3:
                choose_random_cocktail()
                break
            
            case 4:
                display_information()
                break
            
            case 5:
                print("Exiting program! Goodbye!")
                exit()
            
            case _:
                print(f"Invalid choice {user_input}. Please try again.")
        
        clear()
        print_main_menu()

def display_cocktail_details(user_input):
    '''
    This function will display the recipe for the selected cocktail.
    '''
    file = get_file(file_name, cwd)

    for cocktail in file:
        if user_input == cocktail['id']:
            print("\nCocktail Recipe:")
            print("---------------------")
            print(f"Name: {cocktail['name']}")
            print(f"\nCategory: {cocktail['category']}")

            try:
                ingredients_list = ast.literal_eval(cocktail['ingredients'])
                measurements_list = ast.literal_eval(cocktail['ingredientMeasures'])
            except (ValueError, SyntaxError):
                ingredients_list = []
                measurements_list = []
                print("Error in parsing ingredients or measurements.")

            if ingredients_list and measurements_list:
                combined_ingredients = [
                    f"{measure.strip()} {ingredient.strip()}" for ingredient, measure in zip(ingredients_list, measurements_list)
                ]
                ingredients_str = ', '.join(combined_ingredients)
            else:
                ingredients_str = 'No ingredients or measurements found'

            print("\nIngredients with Measurements:")
            print("  - " + ingredients_str)

            print("\nInstructions:")
            print("  - " + cocktail['instructions'])
            print("\n\n\n")

def choose_random_cocktail():
    """
    Select a random cocktail from the dataset and display its details.
    """
    print("\nThe following cocktail has been chosen for you:\n")

    file = get_file(file_name, cwd)

    if not file or len(file) == 0:
        print("The cocktail list is empty or the file could not be loaded.")
        return

    # Choose a random cocktail
    random_cocktail = random.choice(file)

    # Display the details of the random cocktail
    display_cocktail_details(random_cocktail['id'])

def valid_input_main_menu(user_input):
    '''
    This function will validate the user input and ensure that the input is a valid choice for the given context.
    '''
    if user_input < 1 or user_input > 5:
        print("Invalid input. Please enter a number between 1 and 5.")
        return False
    return True

def valid_input(user_input, min_value: int, max_value: int):
    '''
    This function will validate the user input and ensure that the input is a valid choice for the given context.
    '''
    if user_input < min_value or user_input > max_value:
        print(f"Invalid input. Please enter a number between {min_value} and {max_value}.")
        return False
    return True

def get_most_used_ingredient(file_name):
    """
    Calculate the most commonly used ingredient across all cocktails.
    """
    try:
        # Load the CSV file into a DataFrame
        df = pd.read_csv(file_name)

        # Check if the 'ingredients' column exists
        if 'ingredients' not in df.columns:
            print("The 'ingredients' column is missing in the dataset.")
            return None

        # Combine all ingredients into a single list
        all_ingredients = []
        for ingredients in df['ingredients'].dropna():  # Ignore NaN values
            all_ingredients.extend(ingredient.strip() for ingredient in ingredients.split(','))

        # Count the occurrences of each ingredient
        ingredient_counts = Counter(all_ingredients)

        # Find the most common ingredient
        most_common_ingredient, count = ingredient_counts.most_common(1)[0]
        return most_common_ingredient, count
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return None
    except pd.errors.EmptyDataError:
        print("The CSV file is empty.")
        return None

def display_information():
    '''
    This function will display the information section.
    '''

    print("\nInformation:")

    total_cocktails = count_cocktails(file_name)
    print(f"\nTotal number of cocktails in the list: {total_cocktails}")

    try:
        df = pd.read_csv(file_name)

        # Average number of ingredients per cocktail
        if 'ingredients' in df.columns:
            df['num_ingredients'] = df['ingredients'].apply(lambda x: len(x.split(',')) if pd.notna(x) else 0)
            avg_ingredients = df['num_ingredients'].mean()
            print(f"The average number of ingredients per cocktail is: {avg_ingredients:.2f}")

        # Most commonly used ingredient     
        most_common_ingredient, count = get_most_used_ingredient(file_name)
        print(f"The most commonly used ingredient is: {most_common_ingredient} (used {count} times).")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except pd.errors.EmptyDataError:
        print("The CSV file is empty.")

    print("\nPress any key to return to the main menu...")
    input()

def search_cocktail():
    """
    Allow the user to search for a specific cocktail by name.
    If the cocktail is found, display its details.
    If not, prompt the user to try again or return to the main menu.
    """
    while True:
        try:
            # Prompt the user to enter the name of the cocktail
            user_input = input("Enter the name of the cocktail you want to search for: ").strip()

            # Check if the user wants to return to the main menu
            if user_input == '1':
                print("Returning to the main menu...")
                return  # Exit the search function and return to the main menu

            # Load the file and search for the cocktail
            file = get_file(file_name, cwd)  # Load the dataset

            if not file or len(file) == 0:
                print("The cocktail list is empty or the file could not be loaded.")
                return  # Exit the search function

            # Search for the cocktail by name (case-insensitive)
            found_cocktail = None
            for cocktail in file:
                if user_input.lower() == cocktail['name'].lower():  # Case-insensitive match
                    found_cocktail = cocktail
                    break

            if found_cocktail:
                # Display the details of the found cocktail
                display_cocktail_details(found_cocktail['id'])
                return  # Exit after displaying the details
            else:
                # If cocktail is not found, ask user to try again
                print(f"The cocktail '{user_input}' was not found. Please try again or type '1' to return to the main menu.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")


def main():
    get_file(file_name, cwd)
    
    welcome_message()
    print_main_menu()
    
    main_menu()


if __name__ == "__main__":
    main()