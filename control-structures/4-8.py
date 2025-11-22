def filter_files_with_four_char_extension(file_name):
    try:
        with open(file_name, 'r') as file:
            file_names = file.readlines()

        for file_name in file_names:
            file_name = file_name.strip()
            if file_name.endswith('.') and len(file_name) > 4 and len(file_name.split('.')[-1]) == 4:
                print(file_name)
    
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")

file_name = 'files.txt'

filter_files_with_four_char_extension(file_name)
