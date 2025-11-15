balance = 1000
pin = '1234'
attempts = 0
while attempts < 3:
    entered_pin = input("Enter PIN: ")
    if entered_pin == pin:
        print("Access granted")
        break
    else:
        print("Incorrect PIN")
        attempts += 1
if attempts == 3:
    print("Card blocked")
