def avg_speed(distance, hours, minutes):
    time_in_hours = hours + minutes / 60
    return distance / time_in_hours

distance = float(input("Enter distance in km: "))
hours = int(input("Enter number of travel hours: "))
minutes = int(input("Enter number of travel minutes: "))

speed = avg_speed(distance, hours, minutes)
print(f"Average speed: {speed:.1f} km/h")
