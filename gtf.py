# main routine starts here
# functions go here

def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "y" or response == "yes":
            return "yes"
        elif response == "n" or response == "no":
            return "no"
        else:
            print("Please enter yes / no")

def not_blank(question):

    while True:
        response = input(question)

        if response == "":
            print("Sorry this cant be blank. Please try again")
        else:
            return response

# checks users enter an integer to a given question
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer.")

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

print("Program continues")
# set maximum number of tickets below
MAX_TICKETS = 3
tickets_sold = 0
# loop to sell tickets

while tickets_sold < MAX_TICKETS:
    name = not_blank("Enter your name (or 'xxx' to quit) ")

    if name == 'xxx':
        break

    tickets_sold += 1

# Output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("Congratulations you have sold all the tickets")
else:
    print("You have sold {} ticket/s.There is {} ticket/s remaining".format(tickets_sold, MAX_TICKETS - tickets_sold))
