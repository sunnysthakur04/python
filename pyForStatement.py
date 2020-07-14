#/usr/bin/python

print("I like to use the Internet for: ")
for item in ['email', 'net-surfing', 'homework', 'chat']:
    print (item)

print("I like to use the Internet for: ", end=' ')
for item in ['email', 'net-surfing', 'homework', 'chat']:
    print(item, end = ' ')

#####################
#import sys
#sys.stdout.write("Hello There")
#sys.stdout.write("Have a great day")
################
print ('\n') #Next Line
who = "knights"
what = "Na !"
print('We are the', who, 'who say', what, what, what, what)
print('We are the %s who say %s' % (who, (what + ' ') * 4))

#############
for eachNum in range(3):
    print(eachNum)

#############
for eachNum1 in [0, 1, 2]:
    print(eachNum1)

####################
foo = 'abc'
for i in range(len(foo)):
    print(foo[i], '{%d}' % i)

print('############################')
for i, ch in enumerate(foo):
    print(ch, '(%d)' % i)

