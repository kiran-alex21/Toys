
import string

word = input("Enter a possible palindrome: ")

word = word.lower()
word = word.translate(str.maketrans("", "", string.punctuation))

if word == word[::-1]:
    print("This is a palindrome!")
else:
    print("This is not a palindrome!")

