## welcome message and explainer
print(f"Welcome to the savings helper.\nThis will let you know how much to save each month\nto reach you goal in your set timeframe.")

## Input (goal) in GBP
# collect goal from user
goal = input("What is your Savings Goal? £")
x = 0
while x < 3:
    # checking goal is not in words
    if goal.isalpha():
        goal = ("Please enter your goal in digits. £")
        x += 1
        continue
    # seeing if goal has a decimal
    elif "." in goal:
        goal = float(goal)
        break
    # check if goal is just numbers
    elif goal.isdigit():
        goal = int(goal)
        break
    # just in case error exit
    else:
        print("There has been an error in your goal. Please try agian later")
        exit()
# debug checks
"""print(goal)
print(type(goal))
print(x)"""
# exit when tries exceed 3
if x == 3:
    print("You have exceeded 3 attempts. Goodbye.")
    exit()

## Input (months) to reach (goal)
# collect months from user
months = input(f"How long do you have to save £{goal} (in months)? ")
x = 0
while x < 3:
    # check if months is in letters. user prompted to re-enter in digits if it is
    if months.isalpha():
        months = input("Please enter the months in digits. ")
        x += 3
        continue
    # seeing if months is in numbers
    elif months.isdigit():
        months = int(months)
        break
    # just in case error
    else:
        print("There has been an error in your months. Please try again later.")
        exit()
# debug checks
"""print(months)
print(type(months))
print(x)"""
# exit when tries exceed 3
if x == 3:
    print("You have exceeded 3 attempts. Goodbye.")
    exit()

## (monthly amount) = (goal) / (months)
save_monthly = float(goal / months)
# debugging
### print(save_monthly)
# round to 2 dp
save_monthly = round(save_monthly, 2)

## Output save (monthly amount) to reach (goal) in (months)
print(f"You need to save £{save_monthly} per month to reach £{goal} in {months} months.")