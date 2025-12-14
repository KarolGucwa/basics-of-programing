class Phone:
    def __init__(self, brand, memory, battery_level=100, wifi_connected=False, screen_on=False):
        self.brand = brand
        self.memory = memory
        self.battery_level = battery_level
        self.wifi_connected = wifi_connected
        self.screen_on = screen_on
        self.notes = list()

    def add_note(self, note):
        if self.battery_level > 0:
            self.notes.append(note)
            print(f"Note added: {note}")
        else:
            print("Cannot add note, battery is dead!")

    def show_notes(self):
        if self.battery_level > 0:
            if self.notes:
                print("Your Notes:")
                for note in self.notes:
                    print(f"- {note}")
            else:
                print("No notes available.")
        else:
            print("Cannot display notes, battery is dead!")

    def turn_on(self):
        if self.battery_level > 0:
            self.screen_on = True
            print("Phone is now ON.")
        else:
            print("Cannot turn on, battery is dead!")

    def charge(self, amount):
        self.battery_level = min(100, self.battery_level + amount)
        print(f"Phone charged by {amount}%. Current battery: {self.battery_level}%.")

    def connect_to_wifi(self, network_name):
        if self.battery_level > 0:
            self.wifi_connected = True
            print(f"Connected to Wi-Fi network: {network_name}")
        else:
            print("Cannot connect to Wi-Fi, battery is dead!")

    def turn_off(self):
        self.screen_on = False
        print("Phone is now OFF.")

phone1 = Phone("BrandX", "64GB")

phone1.turn_on()
phone1.add_note("Buy groceries")
phone1.add_note("Call mom")
phone1.show_notes()
phone1.charge(20)
phone1.connect_to_wifi("HomeWiFi")
phone1.turn_off()

print(f"Brand: {phone1.brand}")
print(f"Memory: {phone1.memory}")
print(f"Battery Level: {phone1.battery_level}%")
print(f"Wi-Fi Connected: {phone1.wifi_connected}")
print(f"Screen On: {phone1.screen_on}")
