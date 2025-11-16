from keyboard import input_string, input_integer, input_real, input_boolean

first_name = input_string('Enter name: ')
last_name =  input_string('Enter last_name: ')
age = input_integer("Enter age: ")
salary = input_real("Enter salary: ")
is_salary_hidden = input_boolean('Hide salary? (y/n): ')

# Prints employee's record
print('DATA RECORD')
print('===========')
print('Name:', first_name)
print('Last name:', last_name)
print('Age:', age)

if is_salary_hidden == 'N':
    print('Salary', salary)