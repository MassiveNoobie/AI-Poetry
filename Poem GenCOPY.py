# Hacked/Hijacked by Tyler Garrett ... sorry ahead of time
# Reason for hijacking - ultimatly interested in generating unique unstructured
# ... text, to generate a kind of digital "poerty," and the output will be data
# ... The data generated will tell us a lot about the neccesity of unique content
# ... when ranking and generating backlinks. Not to manipulate ranking, rather to
# ... understand SEO best practices, to apply to content written by a human.
# ... The test below is a simple form of randomizing from a file input. Any input.
# ... because I'm new at Python, I want to start here, using Mehrab's script, pycharm...
# ... and a little free time while my son is going down for sleep.
# ... I'm eager to understand the how and why below, and generate a mountain of SEO data.
# ... The true reasoning is to generate a unique use case, I want to eventually pump this
# ... content into Medium.com, where I will keep track of the incoming analytics.
# ... incoming analytics will tell us an independent use case, generated roboticly.
# ... The output will be SEO data to dive in, discover, and test again. The training
# ... for me will offer a place to write about automated poetry.
# ... My end goal is to generate a type of robot that can scrape over the entire poetry
# ... output and tell me the overall sentiment of the project explained above. The reason
# ... behind doing all of this work is to build a type of smart poetry bot.
# ... but without data, how smart can my bot be? I want to be able to generate a few things
# ... at the end of this project, a bot that says whether or not the poetry is good, (longterm)
# ... my long term vision would be to get the data together, per page, republish my findings.
# ... The data will serve to be a guide to not only digital marketing best practices
# ... but also a good usecase to explain the complexities of digital content, content
# ... to allow end users, like you and me, to vote whether or not the bot made GOOD or BAD
# ... poetry, and effectively I want to build a community where people can collab on poems.
# ... Beyond that I would like to plug musicblip into the smart poetry machine, and
# ... come up with ways to use the "good" sounding analog recordings, with "good" poems.
# ... not trying to automate music, just trying to lay down the ground work for it...
# ... if I can get people to actively say "yes" or "no" - we could generate a logisitic
# ... regression model around what is going to be considered good or bad, based on the
# ... overall structure, sentiment analysis, and other things of that nature.
# ... I want to automate "good sounding" poetry... not just any poetry.
# ... By the time the project is complete, I will need to learn more about data science
# ... I hear some algorithms can handle this complexitiy, but to build a model...
# ... I need to build the data. And what's cool is, this nice, tangible, beautiful little
# ... bit of SEO packaged into it, and the data that comes with it will tell us...
# ... if maybe, just maybe, sentiment analysis and sentiment scoring is a part of ranking.
# ... maybe...
# # # # Cheers
# # # # https://tylergarrett.com https://dev3lop.com

import random
import sys

poems = open("buster.txt", "r").read()
poems = ''.join([i for i in poems if not i.isdigit()]).replace("\n\n", " ").replace("\n", " ").split(' ')
# This process the list of poems. Double line breaks separate poems, so they are removed.
# Splitting alPoem GenCOPY.pyong spaces creates a list of all words.
# TAG - split('.') seems to "cut" sentences with...
# EXAMPLE = " Yada. This goes away. Yada " = Yada Yada

index = 1
chain = {}
count = 9000 # TAG - When setting to 1000, it breaks on "adventures" or something odd in the data
# TAG - 900 seems to work most of the time

# This loop creates a dicitonary called "chain".
# Each key is a word, and the value of each key
# is an array of the words that immediately followed it.
for word in poems[index:]: 
	key = poems[index - 2]
	if key in chain:
		chain[key].append(word)
	else:
		chain[key] = [word]
	index += 1

word1 = random.choice(list(chain.keys())) #random first word
message = word1.capitalize()

# Picks the next word over and over until word count achieved
while len(message.split(' ')) < count:
	word2 = random.choice(chain[word1])
	word1 = word2
	message += ' ' + word2

# creates new file with output and prints it to the terminal
with open("output-test.txt", "w") as file:
	file.write(message)
output = open("output-test.txt","r")
print(output.read())
