#noticed the spacing is hitting the link input, I want to see if I can avoid this by reopening, redoing, or something...
#because i want to be able to have more control of this final output, and make an exception for spaces, by re-replacing
#.replace("[=]","").split(basically needs to come after the replace) and i have no clue why.
#thanks for checking this code out, i really suck a programming! www.tylergarrett.com
text = open("buster.txt", "r")
text = ''.join([i for i in text if not i.isdigit()]) \
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

#for line in text:
#    print(line)
#btw, you can program in the rain, if the rain drys fast enough.
#this print(line) -> shows a row level in the command output BUT doesn't stay when doing the write line below...

x = open("z1-Test.txt","w")
x.writelines(text)
x.close()

#for some reasons this doesn't iterate new rows.
#added .replace(" ","[ ]") and leave .split(" ") to enable a divider where once there was only a space.
#one really great thing about this .replace(" ","[ ]") is it quickly finds the first word and last word...
#sure there's some function or something in the python world to identify the first word and last work,
#but this is also a way to figure out the first word and last word of an unstructured data source, which
#seems helpful, from a data perspective.
#furthering the .replace(" ","[ ]") discussion, I stated above, the findreplace feature wasn't functional for our usecase.
#i've pushed the run again, with a \n, which generates the needed space in the data source. Now we can go back,
#and remove the brackets, but just the complexity that I've learned here, feels far greater than any SQL i've ever learned
#or maybe im just thinking of data differently.
#with that said - .replace(" ","[\n]") leaves the brackets, and puts a space in the text file, and doesn't appear or
#generate more spacing or the "\n" in the command, which is cool, and maybe a path to adding a space above...
#i still believe running through both iterations, as described above, a reopen, and then a more optimal path,
#then explaining it. in a blog, or like this.
text = open("z1-Test.txt", "r")
text = ' '.join([i for i in text if not i.isdigit()]) \
    .replace("[=]"," ") \
    .replace('[]','') \
    .replace('[','') \
    .replace(']', '') \
    .split('wtf')

for line in text:
    print(line)

#really hacking away at the output, noticing the an oddity in the
#.split on the second go around, looping the open file again..
#seems split('wtf') has taken on its own oddity... right? split on wtf works? uhm
#remember= the inital goal was to fix the link, <a(SPACE)href="http://etc has a space, and was previously splitting
#to avoid spliting this particular row, I've generated a loop back through, to try and peel out brackets
#(yes im sure there's an easier way but no ranking python blog explains anything well enough to understand the basics
# or tricks you might know)
#the brackets were being originally used to demonstrate a wrapping around the space we split on...
#needed a value to wrap around our link that was breaking too, maybe later we can compress on brackets!
#... and split outside of brackets?
#the brackets then would go on ]bothsidesofaword[... I've additonally added a SPACE in the text=' '.join portion
#now have a little service, looking at python for beginners, and it's a true cluster truck of poorly written content
#and it just gave my dads a little bullshit virus popup. Sounds like pythonforbeginners.com has really dropped the ball
#anyways, I was learning about comprehensive lists in python. Sorry it's called "list comprehensions"
#aka, i hope I can comprehend wtf this is talking about!
#print [ifor i in range(10)] looks like it will solve our poem generation from the early bits of code.
#where i wanted to iterate through a simple list of values VS manually changing the file name. Maybe... This is the way.
#up coming I will be likely troubleshooting this extra bit of padding, and hopefully understanding why
#split has decided to stop working, because split('wtf') just doesn't seem to make sense today.
#hopefully future content I read is a bit more intuitive than pythonforbeginners crappy virus riddled junky blog.