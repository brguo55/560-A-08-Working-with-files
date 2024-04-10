import sys

def search_file(file_variable, search_term):
    # Open the file and read the contents
    with open(file_variable, "r") as file:
        content = file.read()

    # Check if the search term is in the file content
    if search_term in content:
        print(f"Your search term '{search_term}' exists in the '{file_variable}' file!")
        decision = input("Would you like to see the entries? (y or n): ").lower()

        # Show entries if the user chooses 'y'
        if decision == 'y':
            print(f"Here are all of the entries with the term '{search_term}':")
            with open(file_variable, 'r') as file:
                for line in file:
                    if search_term in line:
                        print(line.strip())
        elif decision == 'n':
            print('Goodbye')
            sys.exit()
        else:
            print("Invalid option. Please enter 'y' or 'n'.")
    else:
        print(f"The term '{search_term}' does not exist in '{file_variable}'.")

# Main program loop
while True:
    print("What file would you like to search for?")
    print("a) 60s_music file")
    print("b) athletes file")
    print("x) to exit")
    file_choice = input("Please select an option: ").strip().lower()

    # Map the user input to the respective file names
    file_map = {'a': '60s-music.csv', 'b': 'athletes.csv', 'x': sys.exit}
    file_variable = file_map.get(file_choice)

    # Exit if the choice is 'x'
    if file_choice == 'x':
        print("Exiting the program.")
        sys.exit()

    # If the file choice is invalid, continue the loop
    if file_variable is None:
        print("Invalid option. Please select a, b, or x.")
        continue

    # Get the search term from the user
    search_variable = input(f"Enter the search term for '{file_variable}': ").title()

    # Call the search function
    search_file(file_variable, search_variable)
