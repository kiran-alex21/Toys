T = True

while T:
    print("This Machine can tell you your age in various timeframes.\n"
          "If you want to continue, type 'Go'.\n"
          "If you want to quit, type 'Quit'.")
    
    choice = input().strip().lower()
    if choice == "go":
        pass
    elif choice == "quit":
        T = False
        break
    else:
        print("Invalid input. Please type 'Go' to continue or 'Quit' to exit.")
        continue

    age = input("Enter your age: ")
    
    if age.isdigit():
        age = int(age)
    else:
        print("The age must be in digits. Please try again.")
        continue

    change = input("What timeframe would you like?\n- days,\n- hours,\n- minutes,\n- weeks,\n- months,\n- years,\n- decades,\n- centuries,\n- millenniums: ").strip().lower()
    
    # Dictionary to store the calculations
    timeframes = {
        "days": age * 365,
        "hours": age * 365 * 24,
        "minutes": age * 365 * 24 * 60,
        "weeks": age * 365 / 7,
        "months": age * 12,
        "years": age,
        "decades": age / 10,
        "centuries": age / 100,
        "millennia": age / 1000
    }

    if change in timeframes:
        print(f"You've been living for {timeframes[change]:.2f} {change}")
    else:
        print("The timeframe was not input correctly.\n"
              "The timeframe must be from the list.")
        continue
    
    choice = input("Do you want to have another go? (yes/no): ").strip().lower()
    if choice == "yes":
        continue
    elif choice == "no":
        T = False
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
        continue