import re

def count_vowels(text):
    pattern = r'[aeiouAEIOU]'
    vowels = re.findall(pattern, text)
    return len(vowels)

text = input("Enter some text: ")

vowel_count = count_vowels(text)

print(f"Number of vowels: {vowel_count}")
