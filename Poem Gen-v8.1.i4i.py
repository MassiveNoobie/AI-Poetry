#going to optimize the etl portion now
text = open("buster.txt", "r")
text = 'wtf'.join([word for word in text]) \
    .replace("\n", " ") \
    .replace("\n", "") \
    .replace("Buster", "<a[=]href=http://tylergarrett.com>Tyler[=]Garrett</a>") \
    .replace("http://tylergarrett.com", '"http://tylergarrett.com"') \
    .replace("[=]", " ") \
    .split(' ')

x = open("z1-Test.txt","w")
x.writelines(text)
x.close()

#nod your head and say, "okay let's keep kicking ass."

#btw, you can program in the rain, if the rain drys fast enough.

#woohoo, just learning split('anything') works to split up words... son of a... Hey that's why we learn stuff right?
#i guess next step is running this by someone who knows how to optimize and being told some potentially obvious tips
#assuming i don't need a lot of the ETL above, but it's a fun bit of content to learn how to split up words, using
#python and learning about replacing content, and fun stuff like that.