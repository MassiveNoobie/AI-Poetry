import random
import sys

poems = open("buster.txt", "r").read()
poems = ''.join([i for i in poems if not i.isdigit()]) \
    .replace( \
    "\n\n", " " \
    ) \
    .replace( \
    "\n", " " \
    ) \
    .replace("Buster", "<a href=http://tylergarrett.com>Tyler Garrett</a>") \
    .replace('"', "") \
    .replace("'", "") \
    .replace("http://tylergarrett.com", '"http://tylergarrett.com"') \
    .split(' ')

with open("2.txt", "a") as file:
    file.write(poems)
output = open("2.txt", "r")
print(output.read())
