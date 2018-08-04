import random
import sys

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

#open file for the first time
#write to the file, creates a file if no file is already named "Out-v9.5.txt"
# or whatever you decide to call it in the next line of code.
# so, you are opening the file, writing ("w") the "text" we ETLed above, and closing the file.
# i'm calling this "x" you can call it something else.
x = open("Out-v9.5.txt","w")
x.writelines(text)
x.close()

#second etl process - cleaning up previous code and splitting on your MOM.
#open the file, i for i comprehension or wtfever that is.
#replacing content, and adding a space to heal the [=] portion placed in the link ETL above.
text = open("Out-v9.5.txt", "r")
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
x = open("Out-v9.6.txt","w")
x.writelines(text)
x.close()
#####################################################################################bottom portion, doesn't work for

poems = open("Out-v9.5.txt", "r").read()
poems = ''.join([i for i in poems).replace("\n\n", " ").split('v5TEST')
# This process the list of poems. Double line breaks separate poems, so they are removed.
# Splitting along spaces creates a list of all words.

index = 1
chain = {}
count = 100 # Desired word count of output

# This loop creates a dicitonary called "chain".
# Each key is a word, and the value of each key
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
with open("Zoutput.txt", "w") as file:
	file.write(message)
output = open("Zoutput.txt","r")
print(output.read())