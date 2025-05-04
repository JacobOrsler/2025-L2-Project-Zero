# Functions go here
def int_check(question, low, high):
    """Checks users enter an integer between two values"""

    error = f"Oops - Please enter an integer between {low} and {high} (ie: a number which does not have a decimal part)."

    while True:

        try:
            # Change the response to an integer and check if it's between the chosen numbers
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine goes here

# Loop for testing purposes
while True:

    print()

    # Ask user for an integer
    my_int = int_check("Choose a integer: ", 1, 10)
    print(f"You chose {my_int}")
