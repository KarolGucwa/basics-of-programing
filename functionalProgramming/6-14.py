bottles = [508,500,512,499,492,511,503,476,501,509]
capacity = 500
tolerance = 0.02

def incorrect_fill(cap):
    return lambda x: abs(x - cap) > cap * tolerance

incorrect = list(filter(incorrect_fill(capacity), bottles))

percentage = len(incorrect) / len(bottles) * 100

print(f"Bottle capacity:    {capacity}ml")
print(f"Filling tolerance:  {int(tolerance*100)}%")
print("Filled bottles:    ", ",".join(map(str, bottles)))
print(f"Incorrectly filled: {percentage:.0f}%")
