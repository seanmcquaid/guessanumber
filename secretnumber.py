import random
secret_number = random.randint(1, 10)

print "I am thinking of a number between 1 and 10"

user_guess = 0;
guesses = 5;

while (user_guess != secret_number):
    user_guess = int(raw_input(" What's the number? "))
    guesses -= 1;
    if (user_guess != secret_number):
        if (user_guess < secret_number):
            print str(user_guess) + " is too low. Try Again!"
        else:
            print str(user_guess) + " is too high. Try Again!"
    else: 
        print "You Win!";
    if (guesses == 0):
        print "Sorry, you're out of guesses"
    elif (guesses == 1):
        print "You have 1 guess left"
    else:
        print "You have " + str(guesses) + " guesses left!"