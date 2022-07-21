# Print a welcome message to the user, explaining the Madlib process and command line interactions (DONE)
# Read a template Madlib file and parse that file into usable parts.
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


def read_template(path_to_file):
    with open(path_to_file) as reader:
        return reader.read()


def parse_template(template_string):
    # "It was a {Adjective} and {Adjective} {Noun}."
    capturing = False
    captured_list = []
    stripped_string = ""  # "It was a  and  ."
    captured_string = ""  # Adjective, Adjective, Noun
    for k in template_string:
        if capturing:
            if k == "}":
                captured_list.append(captured_string)
                stripped_string += k
                captured_string = ""
                capturing = False
            else:
                captured_string += k
        else:
            stripped_string += k
            if k == "{":
                capturing = True
    return stripped_string, tuple(captured_list)

# Create and test a merge function that takes in a “bare” template and a list of user entered language parts, and
# returns a string with the language parts inserted into the template.


def merge(bare_template, user_inputs):
    iterating = False
    captured_string = ""
    my_list = list(user_inputs)
    print(my_list)

    for k in bare_template:
        if iterating:
            if k == "}":
                bare_template.__add__(my_list[0])
                iterating = False
        else:
            captured_string += k
            if k == "{":
                iterating = True
    return print(captured_string)


merge("It was a {} and {} {}.", ("dark", "stormy", "night"))

# "It was a {} and {} {}.", ("dark", "stormy", "night")
# adj1_input = input()
# adj2_input = input()
# noun_input = input()
# input_list = list(adj1_input, adj2_input, noun_input)
