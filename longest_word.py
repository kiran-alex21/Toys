
sentence = input("Enter your sentence: ")
words = sentence.split(" ")
max_length = 0
for word in words:
	if len(word) > max_length:
		max_length = len(word)
		longest_word = word
	else:
		continue
print(f"The longest word is: {longest_word}\n{longest_word.capitalize()} is {max_length} letters long.")
