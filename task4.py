#  Using functions on strings. We can use funct. to modify our string, or get info about it.

phrase = "Donkey Kong"
print(phrase.upper().isupper())  # Convert to all upper case, then check if string is all upper case.
print(len(phrase))
print(phrase[1])  # Lookup what is indexed at position 1, in this case.
print(phrase.index("K"))  # Index function
print(phrase.replace("Donkey", "Monkey"))
