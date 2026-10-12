import random

# 1. The computer picks a target number automatically
target_number = 7
guess = 0
attempts = 0

print(f"Target to find: {target_number}\n")

# 2. Loop runs until the random guess matches the target
while guess != target_number:
    guess = random.randint(1, 10)  # Generates a random number from 1 to 10
    attempts += 1
    print(f"Attempt {attempts}: Computer guessed {guess}")

print(f"\nMatch found! It took {attempts} tries.")
