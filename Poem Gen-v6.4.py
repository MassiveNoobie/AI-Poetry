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

for line in text:
    print(line)
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