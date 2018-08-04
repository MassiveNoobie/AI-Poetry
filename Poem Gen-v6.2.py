#Tyler Garrett - below is how I learned about splitting unstructured data using python 2.7.
# The text data is coming from a book, Buster.txt, we are opening the file and doing a small bit of ETL.
# We are using a function I'm not entirely clear on, ''.join([i for an i in text if not i.isdigit()])
# I will come back and explain that later.
# This also serves as a great explanation of how one would split to rows, unstructured data.
# Before today, I was only ever familiar with Alteryx Designer offering a split to rows option, which enabled me
# to really cut the rug when hitting HTML data sources. Which stimmed the reasoning to coming to python.
# Because of all the cool libraries for hacking up html, and things like that.
# So, a cool note for myself, how much easier is this! HAHA.
# The .replace("X","Y") is pretty badass for replacing anything in a file, I hope I'm able to use this
# in other places in my career too, as find/replace is pretty much in every ETL project. Now I'm starting to
# understand why Developers think ETL tools are silly. ETLing in a codebase that changes a lot, where as an application
# has a chance to update, and not error out, I get it... But of the ETL is happening in an environment that doesn't change
# then doing ETL in a strong code/language is starting to make a lot of sense. Hopefully the .join portion
# will be a bridge into joining data and that kind of fun stuff.
# right, so below, is an app that makes incoming text, one word per row in a text file.
# also, i do some find replace on buster=tyler garrett, to start down a path of building data related to the domain.
# www.tylergarrett.com
# Next, pushing the text into another file. Wish me luck. I have no internet service while on the river.
# Which is interesting because the book starts with "born by a river" and a river is in the story a lot.
# I love how life sort of works out like that, but of course if you don't have a buster.txt file, you don't
# really know wtf I'm talking about.
# cool trick - remove the .split(' ') completely, and the app iterates 1 character per word. Pretty rad!
# print(line) prints to the command console, not to a file, that's next.
text = open("buster.txt", "r")
text = ''.join([i for i in text if not i.isdigit()]) \
    .replace( \
    "\n\n", " " \
    ) \
    .replace( \
    "\n", " " \
    ) \
    .replace("Buster", "<a href=http://tylergarrett.com>Tyler Garrett</a>") \
    .replace('"', "") \
    .replace("'", "") \
    .replace("http://tylergarrett.com", '"http://tylergarrett.com"') \
    .split(' ')

for line in text:
    print(line)
#btw, you can program in the rain, if the rain drys fast enough, so basically your machine needs to be really hot.
#thankfully this msi laptop likes to get going.
#and it's not raining that hard, maybe my next blog will be about, "don't program in the rain"