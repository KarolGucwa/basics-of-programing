import random

class Thermometer:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print("Thermometer is now ON.")

    def turn_off(self):
        self.is_on = False
        print("Thermometer is now OFF.")

    def measure_temperature(self):
        if self.is_on:
            temperature = round(random.uniform(34.0, 42.0), 1)
            if temperature >= 41.0:
                print(f"Temperature: {temperature}C (CRITICAL TEMPERATURE!!)")
            elif temperature >= 37.0:
                print(f"Temperature: {temperature}C (fever)")
            else:
                print(f"Temperature: {temperature}C")
        else:
            print("Thermometer is OFF. Please turn it on to measure the temperature.")

def main():
    thermometer = Thermometer()

    thermometer.turn_on()
    thermometer.measure_temperature()
    thermometer.turn_off()

if __name__ == "__main__":
    main()