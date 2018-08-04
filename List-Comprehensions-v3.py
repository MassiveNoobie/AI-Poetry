#The Most Comprehensive List Comprehensions Tutorial, Currently
#By Tyler Garrett
#
#Automate generating a list of values using python 2.7 - List comprehensions 101
#
#
#Tutorial 2 - using a list comprehension with a variable in python 2.7
# Bringing back the previous tutorials complex method to generate a list, it's not that complex so let's take a peak.
# Along with utilizing several examples, to show how python handles different uses cases
# My goal is to help you understand the basics because I'm learning it with you, and feel the current content
# available to an average Google Search... Needs revising.
#
#Below we are using list comprehension using a, b, and c for our result sets.
#---------------------------------
print 'Simple lists of numbers' #printing a headers, this will make reading the output easier.
print '--> Example a' #labeling our examples based on the
#---------------------------------
A = 3 #our first variable will be set at 3, pay attention to the change in the variable through the entire tutorial.
a = [i for i in range(3+A)] #adding two postive numbers together generates more numbers -> range(3+A) = 3+3 = 6
print a #print "a" list comprehensions generated above.
#
#Explained:
#range(3+A) = 3+3 = 6
# 1  2  3  4  5  6
#[0, 1, 2, 3, 4, 5]
#---------------------------------
print '--> Example b'
#---------------------------------
B = 2
b = [i for i in range(3*B)] #multipling postive numbers together generates more numbers -> range(3*B) = 3*2 = 6
print b
#Explained:
#range(3*B) = 3*2 = 6
# 1  2  3  4  5  6
#[0, 1, 2, 3, 4, 5]
#---------------------------------
print '--> Example c'
#---------------------------------
C = -1
c = [i for i in range(7+C)]
print c
#Explained:
#range(7+C) = 7+(-C) = 7+(-1) = 6
# 1  2  3  4  5  6
#[0, 1, 2, 3, 4, 5]
# #---------------------------------
print 'Complex lists of numbers\n' \
      '--> Example d'
#---------------------------------
D = 2
d = []
for d3 in range(3+D):
    d.append(d3)
print d
#Explained:
#range(3+D) = 3+D = 3+2 = 5
# 1  2  3  4  5
#[0, 1, 2, 3, 4]
#---------------------------------
print '--> Example e'
#---------------------------------
E = 2
e = []
for e3 in range(3*E):
    e.append(e3+2)
print e
#Explained:
#range(3*E) = 3*E = 3*2 = 6
# 1  2  3  4  5  6
#[2, 3, 4, 5, 6, 7]
#e.append(e3+2)
#e3="Give me sum(range())
#2=(Start my list at whatever "number" we provide)
#e3+2 generates no additional values in the list "range" of values, it does however START the list of values at '2'
#range(3*E) = 6, give me 6 values in my list of values, doing addition the append simply changes the start value.
#Or another way to explain, for people who like math and visuals, we can show it visually...
#remember the base line values in a list.
#[0, 1, 2, 3, 4, 5] Always start here in your mind, then apply the logic per number.
#[2, 3, 4, 5, 6, 7]
#[0+2=2, 1+2=3, 2+2=4, 3+2=5, 4+2=6]

#---------------------------------
print '--> Example f'
#---------------------------------
F = 3
f = []
for f3 in range(4+F):
    f.append(f3+F)
print f
#Explained:
#range(4+F) = 4+F = 4+3 = 7
# 1  2  3  4  5  6  7
#[3, 4, 5, 6, 7, 8, 9]
#Range = 7, we get 7 in our list, and we start on F, which is 3!
#---------------------------------
print '--> Example g'
#---------------------------------
G = -3
g = []
for g3 in range(7):
    g.append(g3+G)
print g
#Explained
#range(7)=7
#  1   2   3  4  5  6  7
#[-3, -2, -1, 0, 1, 2, 3]
# starting on a negative value because G=-3
#---------------------------------
print '--> Example h'
#---------------------------------
H = 2
h = []
for h3 in range(7):
    h.append(h3*H)
print h
#Explained
#range(7)=7
# 1  2  3  4  5  6   7
#[0, 2, 4, 6, 8, 10, 12]
#Multiplying offers a means of looping multiplication across every value in the range.
#to remove confusion, here's what's happening in the array of numbers
#[0*H, 1*H, 2*H, 3*H, 4*H, 5*H, 6*H]
#[0*2, 1*2, 2*2, 3*2, 4*2, 5*2, 6*2]
#[0*2=0, 1*2=2, 2*2=4, 3*2=6, 4*2=8, 5*2=10, 6*2=12]
#not too bad right?
#---------------------------------
print '--> Example x - super stupid bonus round!'
#---------------------------------
X = 2
x = []
for x3 in range(7):
    x.append(x3*X+3)
print x
#[(0*2)+3=3, (1*2)+3=5, (2*2)+3=7, (3*2)+3=9, (4*2)+3=11, (5*2)+3=13, (6*2)+3=15]
#---------------------------------
print '--> Example y - the final bit.'
#---------------------------------
Y = 3
y = [i*2 for i in range(4+Y)] #i*2 offers the multiplication, per number, per row! Similar to the above complex method.
print y
#
#Explained:
#ping me if this isn't clicking, happy to dive deeper. www.tylergarrett.com
#[0*2=0, 1*2=2, 2*2=4, 3*2=6, 4*2=8, 5*2=10, 6*2=12]
