calculation_to_units =24# assign the value to the variable name-calculation_to_units
name_of_unit = "Hours" #assign the string Hours to the variable name-name_of_unit


def days_to_units(num_of_days):#define a function nane-num_of_days to calculate the days to hours
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
def validate_and_execute():# define a function name-validate_and_execute to validate the user input is correct or not
    try:
        user_input_number =int(user_input)# type casting the user input to iteger.
        if user_input_number >0:# if user input is a positive integer then only calculate the values.
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)# printing the value of  calculated_value.
        elif user_input_number == 0:# if user input is a 0?
            print("You Entered  0,Please enter a valid positive number")#display the message -You Entered  0,Please enter a valid positive number.
        else:
            print("You Entered a negative number,Not Possible conversion")# if user input is a negative value? display the message-You Entered a negative number,Not Possible conversion.
    except ValueError:
        print("Your input is not a valid number")# if user input is a string/Text or a character?display the message-Your input is not a valid number

user_input =""# creating a variable name -user_input
while user_input != "exit":# run the loop continuesly untill the user typed a word "exit"
    user_input =input("Enter number of Days for convert to Hours\n")# prompting user to Enter the number of days for convertion Days to Hours.
    validate_and_execute()# calling the function -validate_and_exicute.
