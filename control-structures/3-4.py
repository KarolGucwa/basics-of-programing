import re

email_file = 'report.txt'

with open(email_file, 'r', encoding='utf-8') as file:
    email = file.read()

pattern = r'€\s?(\d+(\.\d{1,2})?)'

amounts = re.findall(pattern, email)

total_spent = sum(float(amount[0]) for amount in amounts)

print(f"Total money spent: €{total_spent:.2f}")
