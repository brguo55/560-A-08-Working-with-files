import sys # don't use quit() or exit() in production code. Use sys.exit

# Make program repeat:
while True:

    # get user input for file:
    file_variable = input('''
What file would you like to search for?:
a) 60s_music file
b) athletes file
x) to exit
''')

    # process user input
    if file_variable == 'x':
        sys.exit() # this requires
    elif file_variable == 'a':
        file_variable = "60s_music.csv"
    elif file_variable == 'b':
        file_variable = "athletes.csv"
    else:
        print("Invalid option. Please select a, b, or x")
        continue

    # enter a search term this // is a global variable
    search_variable = input(f"Enter the search term for {file_variable} file: ")
    search_variable = search_variable.title() # Make it so that the user can enter lower-case term.

    # go to 02_search_for_term.py to continue .....
    # find (file_variable, search_variable) ....
    with open(file_variable, "r") as file:
        content = file.read()

    # now the file is in the memory buffer as content
    # Next check to see if the search_variable is in the content buffer:
    if search_variable in content:
        # if the file print that it is in the file AND
        # if user wants to see the entries for the term
        print(f"Your search term {search_variable} exists in the {file_variable} file!")
        see_entries = input("Would you like to see the entries? (y or n)")
