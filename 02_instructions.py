# functions go here

def yes_no(question):

    while  True:
        response = input(question).lower()

        if response == "y" or response == "yes":
            return "yes"
        elif response == "n" or response == "no":
            return "no"
        else:
            print("Please enter yes / no")

def instructions():
    print('''
**** Instructions ****

Intructions go here
    
    ''')

# main rountine

# Display instruction on request...
want_instructions = yes_no("Do you want to see the instructions ? ")

if want_instructions == "yes":
    instructions()

print("Program contineus")