print("Guess The animal!")
animal="elephant"
print("The first letter is:",animal[0],"\nThe Last Letter is:",animal[-1],"\nThe animal name is",len(animal), "letters long")
guess=input("Guess the animal: ")
trueGuess=guess.lower()
print("Your Guess is: ",trueGuess == animal)