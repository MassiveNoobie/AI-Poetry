#learning more about list comprehension before python for beginners pops up a stupid popup computer infection nonsense
#on my dads cellphone, which is the only phone i get service on right now, yes im on vacation learning python....
#im doing this because i've never been around a business, job, or company that has let me learn python or taught me python
#no time is better than right now, its very well documented and I'm sure i can hire someone to help me when im stuck.
#alright, i for i time
text = open("buster.txt", "r")
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
    .split("ANYTHINGWORKSHERE") #need to add this last portion, v8.1.i4i was a portion to learn more about the i4i or should i say a meow for a meow
#also it seemed necessary to clean up the above ETL, well after trying not to loop it, I learned i may not be able to
#do it with 1 pass... which leads me to that pickle of development, maybe there isn't a best practice... wtf tyler..
#you're parsing over 30k words in a split second, and I don't think this is a comprehensive usecase...
#imagine what happens when you copy paste the buster story a few times.
#i wonder how fast it will run against 50 stories, vs 1 story. Woh.. That's a few clicks away.

for line in text:
    print(line)
#OKAY so ' '.join is a type of additional concatentation to the front portion of every word.
#I was able to add WTF to the text, SPLIT #2 still doesn't work, i for i does not need to be i... it can be MEOW or BARK.
#You do need to use the same word BACK to BACK, otherwise it throws an error.
#i really wish i understood why "ANYTHINGWORKSHERE" under.split() because i feel like it's making a word split, just because.
#likely a natural thing, but I find it strange that anything works, and removing it splits on the character, not the word.
#end of the story, i learned a little more, I learned about cleaning the front concatentated wtf, and also cleaned out the brackets
#which means I likely don't need to have the additional process because split seems to work, indepedently of the content inside
#although from early studies, I waas able to split(".") and it was cutting out every other sentence, or so it seemed that way
#all will be more clear the more I try and fail, okay so what's next to learn...
#go back and see if the old split is possible, maybe celebrate a little about learning all this ETL?
#i did get final approval on a job offer today, pretty excited, no major celebration at 32, you just sorta...
#nod your head and say, okay let's keep kicking ass.

#btw, you can program in the rain, if the rain drys fast enough.
x = open("z1-Test.txt","w")
x.writelines(text)
x.close()
#adding this here to also write to the same file, using identical syntax, and it updates the data in the file.
#without the last 3 lines of 49-51, you will only print the transformation in the command window
#this may not be helpful if you are trying to check for changes in your file, it will have the old output...
#looking like ]bracketcity[.
#woohoo