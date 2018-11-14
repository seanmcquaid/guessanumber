gameOn = True
keepPlaying = True
import random
secret_number = random.randint(1, 10)
guesses = 5
userName = raw_input("What is your name? ")

while(keepPlaying == True):
    while (gameOn == True):
        print "I am thinking of a number between 1 and 10"
        user_guess = int(raw_input(" What's the number? "))
        guesses -= 1
        
        if (user_guess != secret_number):
            if ((guesses > 1) & (user_guess < secret_number)):
                print "%i is too low. Try Again!" % user_guess
                print "You have %i guesses left!" % guesses
            elif ((guesses == 1) & (user_guess > secret_number)):
                print "%i is too high. You have 1 guess left!" % user_guess
            elif ((guesses == 1) & (user_guess < secret_number)):
                print "%i is too low. You have 1 guess left!" % user_guess
            elif ((guesses > 1) & (user_guess > secret_number)):
                print "%i is too high. Try Again!" % user_guess
                print "You have %i guesses left!" % guesses
            else:
                print "Sorry %s, you're out of guesses!" % userName
                gameOn = False
        else: 
            print "You Win! Congratulations %s" % userName
            gameOn = False

    playAgain = raw_input("Would you like to play again? (y or n) ")
    if (playAgain == "n"):
        keepPlaying = False
        print "Thanks for playing, %s" % userName
    elif (playAgain == "y"):
        secret_number = random.randint(1, 10)
        guesses = 5
        gameOn = True
    else: 
        print "Huh?"