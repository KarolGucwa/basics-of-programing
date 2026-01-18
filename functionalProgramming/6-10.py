import matplotlib.pyplot as plt

temps = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

cities = list(temps.keys())
values = list(map(lambda c: temps[c], cities))

plt.bar(cities, values)
plt.title("Temperatures in Cities")
plt.xlabel("City")
plt.ylabel("Temperature (°C)")
plt.show()
