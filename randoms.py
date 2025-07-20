import random

# Define characters to use for the password
characters = "abcdefghijklmnopqrstuvwxyz"

# Generate a random password of length 8
password = ''.join(random.choice(characters) for _ in range(8))

# Print the password
print("Generated Password:", password)
