calculation_to_units =24
name_of_unit = "Hours"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
def validate_and_execute():
    try:
        user_input_number =int(user_input)
        if user_input_number >0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You Entered  0,Please enter a valid positive number")
        else:
            print("You Entered a negative number,No Possible conversion")
    except ValueError:
        print("Your input is not a valid number")

user_input =""
while user_input != "exit":
    user_input =input("Enter number of Days for convert to Hours\n")
    validate_and_execute()