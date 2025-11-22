def count_file_details(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        num_lines = len(lines)
        num_characters = sum(len(line) for line in lines)
        num_words = sum(len(line.split()) for line in lines)

        print(f"File name: {file_name}")
        print(f"Number of lines: {num_lines}")
        print(f"Number of characters: {num_characters}")
        print(f"Number of words: {num_words}")

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")

file_name = input("Enter the file name: ")
count_file_details(file_name)
