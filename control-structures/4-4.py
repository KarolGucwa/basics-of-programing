file_name = 'it_company.csv'

with open(file_name, 'r') as file:
    lines = file.readlines()

start_index = 0
lines_per_batch = 5

while start_index < len(lines):
    for i in range(start_index, min(start_index + lines_per_batch, len(lines))):
        print(lines[i], end="")
    
    input("\nPress Enter key...")
    start_index += lines_per_batch
