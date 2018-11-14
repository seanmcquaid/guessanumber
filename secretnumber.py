import random
secret_number = random.randint(1, 10);
user_guess = 0;
guesses = 5;
gameOn = True;
userName = raw_input("What is your name? ");

print "I am thinking of a number between 1 and 10"

while (gameOn == True):
    user_guess = int(raw_input(" What's the number? "));
    guesses -= 1;
    if (user_guess != secret_number):
        if (user_guess < secret_number):
            print str(user_guess) + " is too low. Try Again!";
        else:
            print str(user_guess) + " is too high. Try Again!";
    else: 
        print "You Win! Congratulations %s" % userName;
        break

    if (guesses == 0 & user_guess != secret_number):
        print "Sorry %s, you're out of guesses!" % userName;
        break
    elif (guesses == 1):
        print "You have 1 guess left";
    else:
        print "You have " + str(guesses) + " guesses left!";