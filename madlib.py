# Print a welcome message to the user, explaining the Madlib process and command line interactions (DONE)
# Read a template Madlib file (url below), and parse that file into usable parts.
# https://codefellows.github.io/code-401-python-guide/curriculum/class-03/lab/assets/make_me_a_video_game_template.txt
# Prompt the user to submit a series of words to fit each of the required components of the Madlib template.
# With the collected user inputs, populate the template such that each provided input is placed into the correct
# position within the template.
# After the resulting Madlib has been completed, provide the completed response back to the user in the command line.
# Write the completed text to a new file on your file system (in the repo)
# Expected to have meaningful tests for your application

# Create and test a read_template function that takes in a path to text file and returns a stripped string of the
# file’s contents.
# read_template should raise a FileNotFoundError if path is invalid.
# Create and test a parse_template function that takes in a template string and returns a string with language parts
# removed and a separate tuple of those language parts.
# Create and test a merge function that takes in a “bare” template and a list of user entered language parts, and
# returns a string with the language parts inserted into the template.

# Figure out / research a way to verify terminal input/output.

print('''
-------------------------------------
** Hello there! This is the madlib **
** exercise where you will be      **
** asked to input certain grammar  **
** in order to complete a madlib   **
** sentence. The words you input   **
** will then be jumbled together   **
** and shown back to you. It will  **
** also create a new text file of  **
** your madlib!                    **
_____________________________________
''')
