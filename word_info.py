## Take any word, tell you how long it is, which letter is most common, and how often it occurs
# Introduction and obtain word
print("I can tell you about the length of any word, and the most common letter in it.")

# Check word is letters only and continues to ask for a word until it is only letters
isWord = False
while not isWord:
    word = input("What word would you like to find out about? ")
    if not word.isalpha():
        print("Please type one word with letters only.")
        isWord = False
    else:
        word = word.lower().strip()
        word = word.capitalize()
        print(f"I will tell you about the word: {word}")
        isWord = True

# Find the length of the word
length = len(word)
print(f"The word '{word}' is {length} letters long.")

# Counting each letter in the word
letterCounts = {}
for letter in word:
    if letter in letterCounts:
        letterCounts[letter] += 1
    else:
        letterCounts[letter] = 1

# Find the most common letter
mostCommonLetter = max(letterCounts, key=letterCounts.get)
MCLCount = letterCounts[mostCommonLetter]

# Check for multiple common letters
for letter, count in letterCounts.items():
    if count == MCLCount and letter != mostCommonLetter:
        multiMCL = True
        continue
    else:
        multiMCL = False

# Output common letter results
if multiMCL:
    print(f"'{word}' has multiple common letters.")
    print(f"The letters appear {MCLCount} times each.")
    print(f"The most common letters are:")
    for letter, count in letterCounts.items():
        if count == MCLCount:
            print(f"{letter.upper()}")
        else:
            continue
else:
    print(f"The most common letter is {mostCommonLetter.upper()}.")
    print(f"{mostCommonLetter.upper()} occurs {MCLCount} times.")