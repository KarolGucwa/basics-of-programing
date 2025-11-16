###
# Function that returns the full name of a day of the week
# based on its number
#
def day_name(day_number):
    result = ''
    if day_number == 1:
        result = 'Monday'
    elif day_number == 2:
        result = 'Wtorek'
    elif day_number == 3:
        result = 'Środka'
    elif day_number == 4:
        result = 'Czwartke'
    elif day_number == 5:
        result = 'Piątek'
    elif day_number == 6:
        result = 'Sobota'
    elif day_number == 7:
        result = 'Niedziela'
    return result

# Function usage
print('The name of day 5 in the week is', day_name(5))
print('The name of day 3 in the week is', day_name(3))
print('The name of day 7 in the week is', day_name(7))