cm = int(input('Enter height in cm: '))
in_total = cm / 2.54
feet = int(in_total // 12)
inches = int(in_total % 12)
print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')