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
    .split(' ')

for line in text:
    print(line)
#btw, you can program in the rain, if the rain drys fast enough.