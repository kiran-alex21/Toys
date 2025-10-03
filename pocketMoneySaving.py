print("I will tell you how much you can save in a year")
weeklyMoney=float(input("How much pocket money do you get a week? £"))
weeklySpend=float(input("How much do you spend each week? £"))
weeklySave=weeklyMoney-weeklySpend
yearlySave=weeklySave*52
saving=str(yearlySave)
print("You can save £"+ saving, "a year!")