#etl process 1 - open buster3.txt, replace spacing and breaks,
# add a link, adding text things to clean in the next process
text = open("buster3.txt", "r")
text = ''.join([word for word in text]) \
    .replace( \
    "\n\n", " " \
    ) \
    .replace( \
    "\n", " " \
    ) \
    .replace("Buster", "<a[=]href=http://tylergarrett.com>Tyler[=]Garrett</a>") \
    .replace('"', "") \
    .replace("'", "") \
    .replace("http://tylergarrett.com", '"http://tylergarrett.com"') \
    .replace(" ", "[\n]") \
    .split(' ')

x = open("Out-v9.4.txt","w")
x.writelines(text)
x.close()

#second etl process - cleaning up previous code and splitting on your MOM.
#open the file, i for i comprehension or wtfever that is.
#replacing content, and adding a space to heal the [=] portion placed in the link ETL above.
text = open("Out-v9.4.txt", "r")
text = 'wtf'.join([MEOW for MEOW in text]) \
    .replace("[=]"," ") \
    .replace("wtf","") \
    .replace("[","") \
    .replace("]","") \
    .split("yoMAMA")

#print to see what we did.
#for line in text:
#    print(line)

#nod your head and say, okay let's keep kicking ass.
#btw, you can program in the rain, if the rain drys fast enough.

#open the file, and write text to the file, and close the file.
x = open("Out-v9.4.txt","w")
x.writelines(text)
x.close()

#woohoo

#phase2, let's import random because we want to use that in our next script, typically you add this to the top...
#i'm not typical.
#son wants to hit keyboard.
#
#hfhjkl,,,jja
#hj
#wow, "you broke a lot of stuff, oddly enough" not sure why i needed to say that to him outloud. He is just now doing
#two words together, and I'm over here talking about "help me program"... he goes and hits ALT, and windows key, and the
#the mouse, and I'm like cupping my hand around the letter keys...
#thinking "please help me with this content" lol...
#okay let's keep going.
import random
import sys

#previously this script has a bunch of baggage. If you want to continue and learn with me, open Poem Gen-v6.py
#copy and paste everything to the bottom of the script above, or right here... And give yourself a challenge.
#otherwise, scroll down and barely learn anything :p

#poems = open('buster.txt', 'r').read()
poems = open('Out-v9.4.txt', 'r').read()
#i for i with the null join front side... It has a i.isdigit, which coorelates to the "i" letter...
#above, if we change the i to MEOW, then it would be MEOWisdigit... the if not, is seeking to filter the results.
#evidently the previous user was scraping peoms with numbers potentially, i don't know or care, so let's delete it.
poems = ''.join([i for i in poems])\
    .replace("stuff","stuffs") \
    .split('whatEVA')

#defining the value for the words Index, Chain, and Count...
#chain is a little interesting, will research that next I assume.
index = 1
chain = {}
count = 1000
# Desired word count of output (from original author)

# This loop creates a dicitonary called "chain". Each key is a word, and the value of each key
# is an array of the words that immediately followed it. (from original author)
# from me... "what are you even talking about dude." The above chunk of text gives me zero understanding into whats
# happening, zero explanation of what terms to google to learn more, or really anything that is being done,
# that is remotely complicated, is not explained in this code. Which demonstrates a good note to learn from...
# do not make content to show that you can make content, make content as if a 5 year old wants to learn
# which unfortantely is not how anything has been written in the python community...
# maybe im missing that easy blog that explains things real good...
# so far everything ranking for the things I googled are pretty much shit. One had a virus, this one didn't explain anything
# is it just me, or am i the only person who wants to learn everything about what I googled, without having to look for more content.
# honestly - this is why i blog, and im honest all the time so I don't know why I have that backed into my vocabulary.
# anyways, if everything online is worthless, it's really up to you to share this content, otherwise...
# I'm going to have to manipulate the search algorithm, to beat the bullshit SEO cheaters sitting in this search phrases,
# and I will gladly dominate anyone in my SEO path... Because i'm passionate about not only generating good content,
# but also beating the fuck out of the websites who think it's acceptable to have a virus click through, that pops up...
# on my pops cellphone, while trying to learn basic python, from one of the most garbage dumpster websites online.
# I'm coming for you Python for whatever the hell you think you are doing ranking this garbage water.
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

x = open("Out-v9.4.01.txt","w")
x.writelines(message)
x.close()
#this code doesn't work... so, trying scratchpadmeow.py next... going to start with a working bottom portion, and then
#progress to the top half of the ETL. VS trying to plug the bottom half into the script.