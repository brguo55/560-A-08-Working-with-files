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

    