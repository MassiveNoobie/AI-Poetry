#here's my last iteration of handling a space in the link below and avoiding generating 3 rows for the
#tylergarrett.com link, which has a space between "a href" and Tyler(SPACE)Garrett...
#The following script opens a book, replaces the main characters name with an HTML link to my personal blog
#The link generates an data cleansing problem, which is a great end goal for anyone trying to learn how to clean data...
#Like a person, who is me. lol So below, you will notice the SPLIT() number dos has a weird little text in it...
#The secondary split appears to "want to split" in certain areas. But you can pass a failed argument, and maintain
#the previous split on spaces, so... with that said...Don't put a word that you CAN split on... For example, this book
#was written back in the deezy, (back in the day)... So, I can write something like LOL, or WTF... or YoMAMA...
#if your incoming text has a chance of change, maybe incoming comments from youtube, emails, etc... Split 2
#should be a smarter selection.
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
