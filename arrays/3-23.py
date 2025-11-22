import MyText

text = "An apple a day keeps the doctor away"

word_count = MyText.count_words(text)
print(f"Text: {text}")
print(f"Number of words: {word_count}")

longest_first = MyText.sort_by_length(text)
print(f"Words from the longest: {', '.join(longest_first)}")

alphabetical_order = MyText.sort_alphabetically(text)
print(f"Words ordered alphabetically: {', '.join(alphabetical_order)}")
