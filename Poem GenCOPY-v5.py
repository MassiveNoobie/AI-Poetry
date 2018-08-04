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
#it seems being able to do a concatenate would help me remove row 56, "more stuff to learn." Also, cool mention, before this was a really long string of manipulation to the incoming text, end goal was to determine how to ETL incoming data, coming from a text file. Honestly, it's pretty damn easy... And learning how to use this "\" at the end of the code, allows me to indent code out, and I'm a very visual coder and don't really do a lot of LONG string coding, prefer a prettier code. And after working at tableau.com - (im on the home page as of 7/31/18 today, lol) I was shown a video on "how to use the extract API" using python. There was a simple mistake, like capitalization or indenting, the person in the video never mentioned, I spun my wheels like crazy, maybe a few hours. Before I finally asked my friend Matt, an insanely smart dude over on the engineering team. He explained to me it was capsensative and indenting matters, and I was just coming off of learing powershell, which lets you go pretty willy nilly with spacing... (i think, i have no idea, i suck at developing) www.dev3lop.com may be my domain but that doesn't make me a good programmer. lol
# This process the text file. Double line breaks separate poems, so they are removed.
# Splitting spaces creates a list of all words

index = 1
chain = {}
count = 1000
# This loop creates a dicitonary called "chain".
# Each key is a word, and the value of each key
# is an array of the words that immediately followed it.
# Tyler feedback:
# what does this mean? Each key is a word? What does the data structure even look like at this point? what code do I need to write to see this being pushed to a text file or some visual representation of what is happening here would be extremely helpful to understanding how to build this on my own. From a relational database perspective, reading this really makes coding extremely complicated. I know what keys are, and I know these words are not considered keys, maybe it's some coding terminoloigy that I can figure out by learning how to output a "dicitonary" - because this "generated" dictionary sounds like a process that could be optimized by avoiding doing it every time. If I'm seeking to generate a poem off of a "dictionary" called chain, I believe the dictionary needs to be a static object, as the object will never change, no one will rewrite the book on "XYZ" and that means I will not need to rebuild a dictionary. On the first run, yes, but that seems it would be better as it's own process, and we pull from this dictionary=X. X sounds like a type of storage or maybe in memory storage place to put data. Index = 1 sounds like a method to generate a dynamic key, chain {} seems like it's potentially building an array of data, but this is supposed me where we are calling variables integers or something along those lines, I guess I don't understand what chain={} truly means today. I believe this dictionary portion would be good to understand next.
for word in poems[index:]:
	key = poems[index - 1]
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
with open("output-test-v10.txt", "a") as file:
#switching this to A, appends content to the file, at the end of file. otherwise you're stuck with changing the file name. if we could generate a new file, and change the file name after the file is written, every time this runs, it would be prepared to run again, self containing the operation to change the file name offers a better solution than manually changing the code... although there must be an easy method to iterating a set of numbers, and something like "only loop if the end of the file name, "output-test-v10.txt"
#this is likely a next step for me in my learning process... If i need to manually change the file name, then there should be a type of looping i can do....
#we would need to "check the end of the file name" for a number, convert the string of the file name to an integer, using a type of string manipulation, or we could figure out a sort of "request" to the directory (aka folder), this request to the directory would need to tell us a total count of files in the directory. We could even go as far as saying "how many files that are .txt" and that response could be a part of the logic to STOP the loop. So with that said.
# I need to learn more about looping, maybe googling "conditional loop based on number of files" + "python 2.7"
# before i go down a rampage of learning... I think it would make sense to understand how many ways it can be accomplished, being able to do each in python, and understanding each aspect required to handle the overall solution...
#im assuming the ramp up on these will be complicated, and knowing what the best manner would help me accomplish a lot more as I want to blog about this, sorry ahead of time. #www.tylergarrett.com/blog/ assuming I will eventually add the content right here, some blog about whatever im talking about.
#time to open 100000 tabs and not find anything helpful. lol
	file.write(message)
output = open("output-test-v10.txt","r")
print(output.read())
#the more i use the code, the more I'm interested in build a childrens book, about a bear named tyler garrett, sourcing this code... as I read about this story, i'm starting to get a little emotional about the text.
#this book is actually pretty interesting and very much a true kind of story about a bear.
#in the future id like to encourage people to highlight sentences or phrases they enjoy.
#then we can build a childrens book around this content
#the childrens book will be a profit split with any time of program helping bears and encourages more environmental education.
#by myself, I would never be able to come up with much of a big "save the world strategy" around being able to help people optimize technology or business related things... But what if i start applying that "fix" anything logic, and "nothing is impossible" - and apply it to this too...
#i could start tagging on a type of environmental project - and start finding donations, to spear head the bear book idea. I'm sure a grassroots bear book - that gives profits to companies who help with bears, is a great starting place. yeah, okay I guess my notes are turning into a bit of a blog, I'm not surprised.
