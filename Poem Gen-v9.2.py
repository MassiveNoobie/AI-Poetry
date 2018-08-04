#here's my last iteration of handling a space in the link below and avoiding generating 3 rows for the
#tylergarrett.com link, which has a space between "a href" and Tyler(SPACE)Garrett...
#The following script opens a book, replaces the main characters name with an HTML link to my personal blog
#The link generates an data cleansing problem, which is a great end goal for anyone trying to learn how to clean data...
#Like a person, who is me. lol So below, you will notice the SPLIT() number dos has a weird little text in it...
#The secondary split appears to "want to split" in certain areas. But you can pass a failed argument, and maintain
#the previous split on spaces, so... with that said...Don't put a word that you CAN split on... For example, this book
#was written back in the deezy, (back in the day)... So, I can write something like LOL, or WTF... or YoMAMA...
#if your incoming text has a chance of change, maybe incoming comments from youtube, emails, etc... Split 2
#should be a smarter selection than my current yoMAMA joke.
#Btw, original goal here - we want to rip and replace, the link is breaking the text, we don't know jack shit
#about python and generating a use case helps me learn! Also, no service, and lately python has been making a lot more sense.
#currently im on the river, and wanted to mention that because I have no wifi and learning this actually requires
#me to fail, over and over, and try stuff, until it makes sense. Like the i for i logic from previous developer...
#that logic seems to be the typical call out, but I was also able to change the i for i and make it other text...
#similar to testing out the split portion 2 times in one script, lead me to understand you can resplit on an odd char()
#or maybe a few 1's... 111, may be a great split("111") or something along those lines, that's up to you.
#i'm really glad i slowed this code down, and learned about the ETL portion of it.
#below, I'm processing buster3.txt, where I've removed the titles of the chapters, and text explaining the story would
#continue in another chapter. Because that text wasn't very sensible to have scattered around the output.
#and buster3, i copied and pasted 10times, and then ctrl+a, ctrl+c, downarrow, to deselect the highlight, and go to the
#last character in the buster.txt file, and paste again. Now we have 20 total stories.
#a quick mention, python writes a new line with 1 character, for this book, in about 3 to 4 seconds. You can do this.
#single character per row spacing, if you remove .split(), which was explained in a previous script yesterday.
#with that removed you have flexibility to generate a single row of data, per letter, per space, per everything.
#if you add split(' ') with a SPACE, you can see, on the second re-open, that would BREAK our attempt to fix the hyperlink
#so, i've added something random. If you leave the random piece, explained above, you're going to see the same split as
#before, before being the first portion of the script, so with that said, be sure to play around with different portions.
#for example, the ''.join portion, that can be played with, you can add characters to the beginning of every row of data.
#my kid wants to hit the keyboard now, let's see what damange he does...
#
#mmmmmmmmmy
#
#I guess he needs his morning coffee. 925am, his teeth are bothering him. Good luck below and have fun.
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

x = open("z1-Test.txt","w")
x.writelines(text)
x.close()

text = open("z1-Test.txt", "r")
text = 'wtf'.join([MEOW for MEOW in text]) \
    .replace("[=]"," ") \
    .replace("wtf","") \
    .replace("[","") \
    .replace("]","") \
    .split("yoMAMA")

for line in text:
    print(line)

#nod your head and say, okay let's keep kicking ass.

#btw, you can program in the rain, if the rain drys fast enough.
x = open("z1-Test.txt","w")
x.writelines(text)
x.close()

#woohoo
