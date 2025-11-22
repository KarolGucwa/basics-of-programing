###
# Prints employees employed in a specified position.
#

# Employee List
file_name = 'it_company.txt'

# Position
job_title = 'Software Engineer'

with open('it_company.csv') as file:
   counter = 1
   for line in file:
      if job_title in line:
         print(f'{counter}. {line.strip()}')
         counter += 1