from converters import cm_to_inches, ft_inch_to_cm

print("Test 1: Konwersja centymetrów na cale")
cm_value = 100
inch_value = cm_to_inches(cm_value)
print(f"{cm_value} cm = {inch_value:.2f} cali")

print("\nTest 2: Konwersja stóp i cali na centymetry")
feet = 5
inches = 10
cm_value = ft_inch_to_cm(feet, inches)
print(f"{feet} stóp {inches} cali = {cm_value:.2f} cm")

print("\nTest 3: Kolejny test konwersji stóp i cali na centymetry")
feet = 6
inches = 0
cm_value = ft_inch_to_cm(feet, inches)
print(f"{feet} stóp {inches} cali = {cm_value:.2f} cm")
