import sys # don't use quit() or exit () in production code. Use sys.exit

# Make program repeat:
while True:

    # get user input for file:
    file_variable = input('''
    what file would you like to search for?:
    a) 60s-music file
    b) athletes file
    x) to exit
    ''')

# process user input
    if file_variable == 'x':
        sys.exit() # this requires
    elif file_variable == 'a':
        file_variable = '60s-music.csv'
    elif file_variable == 'b':
        file_variable= 'athletes.csv'
    else:
        print("Invalid option. Please select a, b, or x")
        continue
    
    # enter a search term this // is a global variable
    search_variable = input(f"Enter the serach term for {file_variable} file: ")
    search_variable = search_variable.title() # Make it so that the user can enter lower-case term.
    

# go to 02_search_for_term.py to continue .....
def find(file_variable, search_variable):
    with open(file_variable, "r") as file:
        content = file.read()
# now the file is in the memory buffer as content
