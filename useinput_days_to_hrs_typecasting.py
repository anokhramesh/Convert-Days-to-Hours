# A program for convert User inputed number of  days to Hours.
calculation_to_units = 24
name_of_unit = "Hours"

def days_to_units(num_of_days):
    return(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")
user_input_number = int(input("Enter the days for convert to Hrs\n "))
calculated_value = days_to_units(user_input_number)
print(calculated_value)
