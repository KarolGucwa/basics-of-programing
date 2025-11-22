import csv

def print_graphic_designers(file_name):
    with open(file_name, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        
        next(csv_reader)
        
        graphic_designers = []
        
        for row in csv_reader:
            if row[2] == 'Graphic Designer':
                first_name = row[0]
                last_name = row[1]
                email = row[3]
                graphic_designers.append(f"{first_name} {last_name},{email}")
        
        print("GRAPHIC DESIGNERS")
        print("=================")
        for designer in graphic_designers:
            print(designer)

file_name = 'it_company.csv'

print_graphic_designers(file_name)
