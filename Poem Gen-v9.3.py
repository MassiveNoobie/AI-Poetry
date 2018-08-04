#what's next?
#adding the rest of the code to this solution, one big fat script...
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
