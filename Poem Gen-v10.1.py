text = open("buster3.txt", "r")
#From a link perspective...
#Wake up because - this portion lets you replace any word with a link of your choosing.
#I'm also solving for the "space" which is, now a [=], and the overall oddity of the html link syntax,
# previous versions - link coming soon ()
# offer insights into how we got here, and what's what. If you change the link,
#give me a shoutout on your blog, or link to some of my content, would be also cool to
#chat/learn/work with any of you. I learned some interesting things with the google algorithm _____________________________that i love sharing with people willing to network and grow together. Not looking for clients, looking for buds who think learning and sharing that knowledge is more important than monetizing stuff for profit. Yep.
#hit me up at www.twitter.com/itylergarrett im terrible at programming but will be keep
# learning, this is like day 5...and i think im barely scratching the surface, long term,
# i will be giving away little solution/python apps for blogging help, SEO, scraping,
# data, and whatever else i can come up with in my spare time - or for a customer with a cool idea.
# 4real, seriously, thanks for your time. 8/1/18
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

#open file for the first time
#write to the file, creates a file if no file is already named "Out-v9.7.txt"
x = open("Out-v10.1.txt","w")
x.writelines(text)
x.close()

#second etl process - cleaning up previous code and splitting on your MOM.
#open the file, i for i comprehension or wtfever that is.
#replacing content, and adding a space to heal the [=] portion placed in the link ETL above.
text = open("Out-v10.1.txt", "r")
text = 'wtf'.join([MEOW for MEOW in text]) \
    .replace("[=]"," ") \
    .replace("wtf","") \
    .replace("[","") \
    .replace("]","") \
    .split("yoMAMA")

#nod your head and say, okay let's keep kicking ass.
#btw, you can program in the rain, if the rain drys fast enough.

#open the file again, re-write text to the file, and close the file. exactly the same as last time.
x = open("Buster-v10.1.txt","w")
x.writelines(text)
x.close()
#####################################################################################bottom

#import rad code libraries and stuff
import random
import sys

poems = open("Buster-v10.1.txt", "r")
poems = ''.join([i for i in poems if not i.isdigit()]) \
    .replace("\n", " ") \
    .split(' ')

#oh btw, golf friggen clap for 10k unique words. Golf clap you champion you... if you played with the code, or had fun
#reading any of this bullshit, check me out on www.twitter.com/itylergarrett or www.tylergarrett.com obviously.
index = 1
chain = {}
count = 10000

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
with open("Out-v10.1.txt", "w") as file:
	file.write(message)
output = open("Out-v10.1.txt","r")
print(output.read())

#awesome, shits working, just thought of a cool idea too...
#i want to scrape a blog, grab the first sentence of every blog, and the first header.
#sentiment score those, filter the shit ones out, find trends,...
#what is the most said word, best sentiment response, etc... etc. etc...
#okay that will be a fun side project.
#let me try and rephrase it, as rephrasing things typically helps people understand complicated content better.
#
#scrape blogs for links, jump to new blog posts, identify whats a blog post, grab sentence=x, find X sentiment,
# filter out bad X, understand what's the best from a score perspective, grab scores too.
# keep track of scores overtime and changes to the text, that should be really interesting knowledge.
# also a good example of a solution i architected for a company, they were interested in an SEO solution
# based on web scrapping, i said "point it at your competitors ranking page you want to beat" if it changes, send alert
# now you know they are trying to beat you in ranking again.
# okay time to chill with wife for a bit, this was a little too fun...
# next would be automating more links like this, maybe to WIKI based on the words being used...
# i think there are only so many words in the world, and the more i can learn about how things are commonly said
# the better my bot will be, currently im making random stuff but the random stuff generates interesting thoughts
# that's why I call it poetry, not just junk.. but really techie poetry. Eat your heart out some artist i dont know the
# name of because i went to college for databases, not python, not peotry.
#