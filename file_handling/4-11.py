def calculate_and_save_powers(file_name):
    with open(file_name, 'w') as file:
        for i in range(1, 101):
            second_power = i ** 2
            third_power = i ** 3
            line = f"{i},{second_power},{third_power}\n"
            print(line.strip())
            file.write(line)

file_name = 'powers.txt'
calculate_and_save_powers(file_name)
