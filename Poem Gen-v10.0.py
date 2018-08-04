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

#open file for the first time
#write to the file, creates a file if no file is already named "Out-v9.5.txt"
# or whatever you decide to call it in the next line of code.
# so, you are opening the file, writing ("w") the "text" we ETLed above, and closing the file.
# i'm calling this "x" you can call it something else.
x = open("Out-v9.7.txt","w")
x.writelines(text)
x.close()

#second etl process - cleaning up previous code and splitting on your MOM.
#open the file, i for i comprehension or wtfever that is.
#replacing content, and adding a space to heal the [=] portion placed in the link ETL above.
text = open("Out-v9.7.txt", "r")
text = 'wtf'.join([MEOW for MEOW in text]) \
    .replace("[=]"," ") \
    .replace("wtf","") \
    .replace("[","") \
    .replace("]","") \
    .split("yoMAMA")

#nod your head and say, okay let's keep kicking ass.
#btw, you can program in the rain, if the rain drys fast enough.

#open the file again, re-write text to the file, and close the file. exactly the same as last time.
x = open("Buster31.txt","w")
x.writelines(text)
x.close()
#####################################################################################bottom

#import rad code libraries and stuff
import random
import sys

poems = open("Buster31.txt", "r")
poems = ''.join([i for i in poems if not i.isdigit()]) \
    .replace("\n", " ") \
    .split(' ')
#split3 needs extra love, not sure why yet, other split was more child play... like the drake song.
#i tried to play the song, without service, and found "childs play" music only, it sounded like a type of 20 year old
#tape recorder recording, lol... Okay, so wife and i are listening to Hold on, we're going home. By drake, who the F
# else would i be listening to on vacation while learning python.
#i should probably turn this music off and google more about this next portion.


#but before i do that, I will dive into the above i for i portion more, there's a lot to learn there and I need
#to build a few sample sets of txt files and sample sets of whatever is going on above...
#with code explained, output explained, change the code explained, change the output explained, really drill
#what i learned into my head. lots of failures to get this thing working, and if i dont explain it, how does anyone
#learn what happened without failing and wasting days like i just did... right, here goes. ttyl

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
with open("Out-ScratchPad2.txt", "w") as file:
	file.write(message)
output = open("Out-ScratchPad2.txt","r")
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