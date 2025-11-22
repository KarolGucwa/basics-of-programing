###
# Reads from file, line by line
#
counter = 1
with open('countries.txt', 'r') as file:
    for line in file:
        print(f"{counter}. {line}", end="")