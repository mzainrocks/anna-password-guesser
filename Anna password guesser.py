print("Welcome back ANNA")
password = input("Please set a password to guess:")
guessername = input("Guesser, please enter your name:")
print("Welcome to the Password Guessing Game",guessername,".You have 8 attempts to guess my password! GoodLuck!")
guesscount = 0
for i in range(8):
    guess = input("Take a guess:")
    if guess == password:
        print("Contratulations, You have guessed the password")
        break
    else:
        guesscount = guesscount + 1
print("it took you",guesscount,"guesses to guess the password")

