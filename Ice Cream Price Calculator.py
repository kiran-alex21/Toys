#Ice Cream Price Calculator - www.101computing.net/ice-cream-price-calculator
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("+                               +")
print("+      The Ice Cream Shop       +")
print("+            Welcome            +")
print("+                               +")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("")

container = input("What type of ice cream container would you like: cup or cone?")

while container!="cup" and container!="cone":
   print("Invalid answer please try again!")
   container = input("What type of ice cream container would you like: cup or cone?")

price = 0
if container == "cup":
   price = 0.50
elif container == "cone":
   price = 0.8

scoops = int(input("How many scoops would you like - 1 to 4?"))
while scoops < 1 and scoops > 4:
   print("Invalid answer please try again!")
   scoops = int(input("How many scoops would you like - 1 to 4?"))

price += scoops * 1.00

flake = input("Would you like a Flake? yes or no")
while flake!="yes" and flake!="no":
   print("Invalid answer please try again!")
   flake = input("Would you like a Flake? yes or no")
if flake == "yes":
   price += 0.4
   
sprinkles = input("Would you like Chocolate Sprinkles? yes or no")
while sprinkles!="yes" and sprinkles!="no":
   print("Invalid answer please try again!")
   sprinkles = input("Would you like Chocolate Sprinkles? yes or no")
if sprinkles == "yes":
   price += 0.3

coulis = input("Would you like Strawberry Coulis? yes or no")
while coulis!="yes" and coulis!="no":
   print("Invalid answer please try again!")
   coulis = input("Would you like Strawberry Coulis? yes or no")
if coulis == "yes":
   price += 0.4


print(f"Your icecream will cost £{price:.2f}")