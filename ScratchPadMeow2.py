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

#print to see what we did. (commented out for future testing and faster app transaction, due to not needing to visually
#populate the printed text, which if you're doing a big book TIMES 20, like I am, you want those seconds back in your day.
#for line in text:
#    print(line)

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
#well that wasn't fun to figure out, the third split needs to split on something functional..
#now im pretty clueless why the previous scripts second split allows for a false flag to continue a word split...
#above, i'm saying "if there's a break in the text, or NEW ROW, add a space.
#and then I'm telling it to split on "space" - otherwise I was struggling a lot to move this beyond the below "random"
#portion, which i have in these lessons, I've not really taken the time to google and figure out that portion.

index = 1
chain = {}
count = 10000 # Desired word count of output

# This loop creates a dicitonary called "chain". Each key is a word, and the value of each key
# is an array of the words that immediately followed it.
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