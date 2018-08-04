#Poem Gen-v10.2
#Hi-jacked, improved, developed by Tyler Garrett
#Built on 8/1/18
#Follow: www.tylergarrett.com or www.twitter.com/itylergarrett
text = open("buster3.txt", "r")
text = ''.join([word for word in text]) \
    .replace( \
    "\n\n", " " \
    ) \
    .replace( \
    "\n", " " \
    ) \
    .replace("Buster", "<a[=]href=http://tylergarrett.com>Tyler[=]Garrett</a>") \
    .replace("http://tylergarrett.com", '"http://tylergarrett.com"') \
    .replace(" ", "[\n]") \
    .split(' ')

#open file for the first time, write to the file, close file.
x = open("Out-v10.2.txt","w")
x.writelines(text)
x.close()

#fix space in link
text = open("Out-v10.2.txt", "r")
text = 'wtf'.join([MEOW for MEOW in text]) \
    .replace("[=]"," ") \
    .replace("wtf","") \
    .replace("[","") \
    .replace("]","") \
    .split("yoMAMA")

#finish space clean and fake split to keep previous breaks
#flex I dub yiiii yoMAMA fix. and forever will yiii bask in the glory of awkward turtleness
#where you shall feast with other similiar work arounds for someone with limited service on vacation.
#open file, write text to file, close file.
# cuhhhhching
x = open("Buster-v10.2.txt","w")
x.writelines(text)
x.close()
#####################################################################################bottom

import random
import sys

poems = open("Buster-v10.2.txt", "r")
poems = ''.join([i for i in poems if not i.isdigit()]) \
    .replace("\n", " ") \
    .split(' ')

#thanks for reading any of this crap, check me out on www.twitter.com/itylergarrett or www.tylergarrett.com obviously.
index = 1
chain = {}
count = 10000
#how many words in the Poem output?

#Word randomizer using above variables
for word in poems[index:]:
	key = poems[index - 1]
	if key in chain:
		chain[key].append(word)
	else:
		chain[key] = [word]
	index += 1

word1 = random.choice(list(chain.keys())) #random first word
message = word1.capitalize()

#checking length of output, once it hits 10k words, it stops.
while len(message.split(' ')) < count:
	word2 = random.choice(chain[word1])
	word1 = word2
	message += ' ' + word2

with open("Final-Out-v10.2.1.txt", "w") as file:
	file.write(message)
output = open("Final-Out-v10.2.1.txt","r")
print(output.read())
#
#Why:
# Poem generation - I want to build poems to help inspire others with "whatever it is they need in that moment."
# Data generation - I need to make data because I'm a data nerd.
#
#Future ideas:
# AI poem generation - "can we make good poetry?"
# Understanding what "good" poetry is considered from a human perspective.
# Program the bot to follow the success data, (datascience) based on human and robot scores.
# Lastly, to apply sentiment score from several different sentiment scoring data sources.
# Release tutorials on python, rank it to the moon, as I learn through the code...
#
#Tips:
# occassionally this app hits the bottom of the poem and errors out.
# run it again (it will work). future error handling could include re-run based on error output! rad. <3 this stuff.
# Most hilarious output I've caught thus far, <a href="http://tylergarrett.com">Tyler Garrett</a> smiled, for worms.
# lol