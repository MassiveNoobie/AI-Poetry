import random
import sys

poems = open("buster.txt", "r").read()
poems = ''.join([i for i in poems if not i.isdigit()]).replace("\n\n", " ").split(' ')
# This process the list of poems. Double line breaks separate poems, so they are removed.
# Splitting along spaces creates a list of all words.

# creates new file with output and prints it to the terminal
with open("outputTEST.txt", "w") as file:
	file.write(poems)
output = open("outputTEST.txt","w")
print(output.read())
