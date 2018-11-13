secret_number = 5;
print "I am thinking of a number between 1 and 10"
user_guess = 0;
while (user_guess != secret_number):
    user_guess = int(raw_input(" What's the number? "))
    if (user_guess != secret_number):
        print "Try again!"
    else: 
        print "You Win!";