def occurs(number, array):
    return number in array

number = int(input("Enter a number: ")) 
array = [15, 38, 7, 23, 14] 

print(f"Number: {number}")
print(f"Array: {' '.join(map(str, array))}")
if occurs(number, array):
    print(f"Result: number {number} appears in the array")
else:
    print(f"Result: number {number} does not appear in the array")
