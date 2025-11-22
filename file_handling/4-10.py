import csv

def print_clothing(file_name):
    with open(file_name, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        
        for row in csv_reader:
            product_name = row[1]
            price = float(row[5])
            stock = int(row[6])

            if price < 60 and stock < 40:
                print(f"{product_name} - Price: ${price}, Stock: {stock}")

file_name = 'clothing.csv'
print_clothing(file_name)
