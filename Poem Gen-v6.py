import random
import sys

poems = open("buster.txt", "r").read()
poems = ''.join([i for i in poems if not i.isdigit()])\
	.replace(\
            "\n\n", " "\
            )\
    .replace(\
            "\n", " "\
            )\
	.replace("Buster", "<a href=http://tylergarrett.com>Tyler Garrett</a>")\
	.replace('"', "")\
	.replace("'", "")\
	.replace("http://tylergarrett.com", '"http://tylergarrett.com"')\
    .split(' ')

index = 1
chain = {}
count = 1000

for word in poems[index:]:
	key = poems[index - 1]
	if key in chain:
		chain[key].append(word)
	else:
		chain[key] = [word]
	index += 1

word1 = random.choice(list(chain.keys()))
message = word1.capitalize()

while len(message.split(' ')) < count:
	word2 = random.choice(chain[word1])
	word1 = word2
	message += ' ' + word2

with open("1.txt", "a") as file:
	file.write(message)
output = open("1.txt","r")
print(output.read())
