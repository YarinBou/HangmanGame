user_guess = input("Guess a letter: ")
if (len(user_guess) > 1) and (not (user_guess.isalpha())):
    print("E3")
elif (not (user_guess.isalpha())):
    print("E2")
elif (len(user_guess) > 1):
    print("E1")
else:
    print(user_guess.lower())
