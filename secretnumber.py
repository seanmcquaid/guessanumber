gameOn = True
import random
secret_number = random.randint(1, 10)
guesses = 5
userName = raw_input("What is your name? ")


while (gameOn == True):
    print "I am thinking of a number between 1 and 10"
    user_guess = int(raw_input(" What's the number? "))
    guesses -= 1
    
    if (user_guess != secret_number):
        if (guesses > 0 & user_guess < secret_number):
            print "%i is too low. Try Again!" % user_guess
        elif (guesses == 1 & user_guess != secret_number):
            print "You have 1 guess left!"
        elif (guesses > 0 & user_guess > secret_number):
            print "%i is too high. Try Again!" % user_guess
        else:
            print "Sorry %s, you're out of guesses!" % userName
            gameOn = False
    else: 
        print "You Win! Congratulations %s" % userName
        gameOn = False