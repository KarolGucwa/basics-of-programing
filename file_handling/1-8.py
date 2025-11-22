def read_from_file(name):
    with open(name, 'r') as file:
        content = file.read()
    return content

file_content = read_from_file('pets.txt')
file_lines = file_content.splitlines()
total_word_count = 0

for line in file_lines:
    words = line.split()
    total_word_count += len(words)
    print(line)

print(f"Total word count: {total_word_count}")
