"""Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. """
import random

number = random.randint(0, 9)
guess = -1
guess_counter = 0



while guess != number:
	if guess > number:
		print("guess is too high!")
	elif guess < number:
		print("guess is too low!")
	guess = int(input("please guess number (0-9): "))
	guess_counter += 1

print("you were right")
print("the number was: " + str(number))
print("number of guesses: " + str(guess_counter))



"""Ask the user for a number and determine whether the number is prime or not."""
def is_prime(num):
	is_prime = True
	for check_num in range(3, num):
		if num % check_num == 0:
			is_prime = False
	return num == 1 or num == 2 or is_prime == True




