#The Most Comprehensive Python List Comprehensions Tutorial, Currently
#By Tyler Garrett
#
#Automate generating a list of values using python 2.X - List comprehensions 101
# If you are new, eager to learn quickly, want to learn without having to code, need lots of examples...
# Looking for a lot of sample code, that tests a lot of different variations of list comprehensions, or maybe...
# You looked online, didn't find anything decent, a little upset trying to learn python, need a better guide...
# Cool that's why I write, to replace the TRASH WATER blogs online. No monetizing, no click ads, just solutions.
#---------------------------------
#---------------------------------
#---------------------------------
#Before we begin, let's discuss two simple methods to printing our list comprehensions.
#---------------------------------
#----------Code basics------------
#---------------------------------
print [i for i in range(3)]
#or we can use a letter, word, or letters+words. We will only use this method below.
x = [i for i in range(3)]
print x
#---------------------------------
#---------------------------------
#---------------------------------
#Below, I will explain how to use list comprehensions, what list comprehensions is all about, and various ways to use
# list comprehensions when utilizing Python! Woohoo, getting excited, I can tell. (I can't, I'm weird)
#
#What is list comprehensions?
# List comprehensions is the name of a way to create lists. A more technical rationale would be that list comprehensions
# provide a more concise way to create lists in situations where map() and filter() and/or nested loops would currently
# be used.
#
#What is the goal with list comprehensions?
# It is proposed to allow conditional construction of list literals using for and if clauses. It's like you haven't
# heard of either of these today, if so, go check out python's website on list comprehensions. If this does make sense,
# you may also be interested to know the proposed solution not only lets you generate conditional lists with for and if,
# they would nest the same way for loops and if statements nest now.
#
#Alert, red alert, altert... Read this before beginning.
#So, you decided to read, and that means you're a lot like me, thinking I was smart as shit, until I really started
# reading content online that was way above my knowledge base, and i remember I could read stuff...
# and not remember a damn thing i just read... I was having a lot of trouble letting go of my ego.
# So, long short, you decided you will start learning list comprehensions in python by my stupid face...
# Please read this little paragraph below... Because this has been entirely written for noobs, like me.
#
#About the tutorials below.
# If you're not entirely sure what any of the above text means, woohoo. You're on the right track,
# you're on the right blog, and if you do know the techie words above, but not entirely sure what it means in code,
# or in python... Check it out...
#
# The next few tutorials on list comprehnsions will be right up your alley, if you understand the techie mumbo jumbo
# this will be a good refresh and a hilarious chunk of code you can likely help optimize, and I will gladly add
# anyone in the tutorial blog posts - and link to whatever website, github profile, etc, and help you rank better.
# As a novice at all things python, I'm excited to get to know you more as you take the journey I once took.
#
# I'm excited to get to know people who think this is total trash too. I need that kind of feedback.
# I'm learning every day, coding is hard, and I only know what I know, and that means
# if someone could show me all the ways the code works, I will master the code, otherwise I'm MR. Trial and error.
# so longest story short, you're here to learn, me too, so let's get started
# by learning everything there is to know about list comprehensions.
#
#
#
# are you scrolling and not reading?
# are you scrolling and not reading?
# are you scrolling and not reading?
#
# read a couple of paragraphs above, or you may be wasting your time.
#
#
# Feedback? https://tylergarrett.com
#
#Tutorial 1, making a simple list of data in python using List Comprehensions
#There are two different ways to make a list of numbers in python.
#Take a look at List Comprehension and another more complicated method.
#---------------------------------
#Easy method to make a simple list in python.
x = [i for i in range(10)]
print x
#Output
## >>>[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Complex method to make a simple list in python.
x2 = []
for x3 in range(10):
    x2.append(x3)
print x2
#Output
## >>>[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Both X and X2 generate the same output!
#We will focus on the Easy method known as "List comprehension"

#Notice we are using a different letter in the list comprehension code below.
# When learning python, a lot of example code has "words" which can be
# changed to letters. Like below, I'm using a "y"... Later in this tutorial or lesson...
# I'm going to keep changing the "y", which is the results of the list comprehension in python below!
y = [i for i in range(11)]
print y

#You may be thinking, okay, we are increasing the numbers each time, and changing the letter in the beginning.
# That's true, it's a nice little pyramid if you run every bit of code together, which is pretty cool to know...
# You might be copy pasting different pieces of the code, and in this particular chunk of code, you can run the entire
# Set of code, and not need to worry about anything! It will give you a results of our list comprehension code, which
# is clearly marked as "print" "firstletter"... easy enough to keep up with.
# here's a curve ball, I changed i to meow, and that works too.
z = [meow for meow in range(12)]
print z

#This list comprehension code below has more than a letter, similar to the complex list generation code above, we used
# x2 (example 2), and similarly, we are not using a letter to describe the results of the list comprehension.
# For the new programmers -> Light bulb moment? You can name the "X", "Y", "Z" anything you damn please...
# If you're following here, you should now see a pattern, and easy pattern to generate simple lists with a range of #'s.
# Also, you might be seeing a little bit of math. How exciting! You're doing math, in python!
tyler = [i for i in range(14-1)]
print tyler

#In the list comprehension below, I'm simply demonstrating addition... On the range() portion of the code.
tyler2 = [DOG for DOG in range(12+2)]
print tyler2

#More math, yes division, multiplication, subtraction and addition work in python, pretty well too..
# I tested, it's accurate.
tyler3 = [i for i in range(14/2+7+1)]
print tyler3

#All results should look like:
#[0, 1, 2]
#[0, 1, 2]
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]