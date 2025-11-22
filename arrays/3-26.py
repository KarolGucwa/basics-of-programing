import matplotlib.pyplot as plt
import math

x = []
y = []

# create x values (kąty w stopniach od 0 do 360)
for n in range(0, 361):
    x = x + [n]

# create y values (sin(x) dla każdego kąta)
for n in x:
    y = y + [math.sin(math.radians(n))]

# print chart
plt.plot(x, y)
plt.title("Wykres funkcji y = sin(x)")
plt.xlabel("Kąt (stopnie)")
plt.ylabel("y = sin(x)")
plt.grid(True)
plt.show()
