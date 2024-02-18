import itertools

# Define all characters to include in the combinations
# Uppercase, lowercase, digits, and a representative set of special characters, including space
# Adding Norwegian characters æ, ø, å in both uppercase and lowercase
characters = (
    "abcdefghijklmnopqrstuvwxyz"  # Lowercase
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Uppercase
    "0123456789"                  # Digits
    " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"  # Special characters including space
    "æøåÆØÅ"                      # Norwegian characters
)

# Use itertools.product to generate all possible 2-character combinations
combinations = itertools.product(characters, repeat=2)

# Open a file to write the combinations
with open("password_combinations.txt", "w") as file:
    for combination in combinations:
        # Join the characters to form a 2-character password and write to the file
        file.write("".join(combination) + "\n")

print("Password combinations generated successfully.")
