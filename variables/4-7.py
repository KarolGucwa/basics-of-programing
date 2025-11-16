def Z11642(Z11642K1):
	NATO_CODE = {
		"A": "Alfa",
		"B": "Bravo",
		"C": "Charlie",
		"D": "Delta",
		"E": "Echo",
		"F": "Foxtrot",
		"G": "GOLF",
		"H": "Hotel",
		"I": "India",
		"J": "Juliett",
		"K": "Kilo",
		"L": "Lima",
		"M": "MIKE",
		"N": "NOVEMBER",
		"O": "Oscar",
		"P": "PAPA",
		"Q": "Quebec",
		"R": "Romeo",
		"S": "Sierra",
		"T": "TANGGO",
		"U": "Uniform",
		"V": "Victor",
		"W": "Whiskey",
		"X": "X-ray",
		"Y": "Yankee",
		"Z": "Zulu ",
	}
	result =', '.join(NATO_CODE[letter] for letter in str(Z11642K1))+'.'
	return result
chars = input('Enter integer number: ')
result = Z11642(chars)
print(result)