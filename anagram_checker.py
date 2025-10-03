allWords = []
words = input("What Words do you want to check? ")
allWords = words.split()

matchCheck = {}
for word in allWords:
    key = "".join(sorted(word.lower()))
    if key not in matchCheck:
        matchCheck[key] = [word]
    else:
        matchCheck[key].append(word)

print("The anagrams are:")
for group in matchCheck.values():
    if len(group) > 1:
        print(sorted(group))


