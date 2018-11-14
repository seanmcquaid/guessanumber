import random
secret_number = random.randint(1, 10)
print "I am thinking of a number between 1 and 10"
user_guess = 0;
while (user_guess != secret_number):
    user_guess = int(raw_input(" What's the number? "))
    if (user_guess != secret_number):
        if (user_guess < secret_number):
            print str(user_guess) + " is too low. Try Again!"
        else:
            print str(user_guess) + " is too high. Try Again!"
    else: 
        print "You Win!";