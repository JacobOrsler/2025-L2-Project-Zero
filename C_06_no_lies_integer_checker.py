# Functions go here
def int_check(question):
    """Checks users enter an integer"""

    error = "Oops - Please enter an integer (ie: a number which does not have a decimal part)."

    while True:

        try:
            # Return the response if it's an integer
            response = int(input(question))

            return response

        except ValueError:
            print(error)


# Main routine goes here

# Loop for testing purposes
while True:
    print()

    # Ask user for their name
    name = input("Name: ")  # Replace with call to 'not blank' function

    # Ask for their age and check if it's between 12 and 120
    age = int_check("Age: ")

    # Output error message / success message
    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue
    else:
        print(f"{name} brought a ticket")
