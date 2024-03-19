# checks that user response is not blank
def not_blank(question):
    while True:
        response = input(question)

        if response == "":
            print("Sorry this cant be blank. Please try again")
        else:
            return response


# functions go here
# checks users enter an integer to a given question
def num_check(question):
    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer.")


# Main routine goes here
tickets_sold = 0

while True:

    # gets user name (can't be blank)
    name = not_blank("Enter your name (or 'xxx' to quit) ")

    if name == "xxx":
        break

    # get's user age (between 12 and 120)
    age = num_check("Age: ")

    if 12 <= age <= 120:
        pass
    elif age < 12:
        print("Sorry you are too young for this movie")
        continue
    else:
        print("?? That looks like a typo, please try again.")
        continue

    tickets_sold += 1

print(f"You sold {tickets_sold}")
