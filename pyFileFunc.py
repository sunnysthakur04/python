#/usr/bin/python

#How to open a file (Syntax)
# handle = open(file_name, access_mode = 'r')

#Read file
filename = input('Enter file name: ')
fobj = open(filename, 'r')
for eachLine in fobj:
    print(eachLine)

#Write file
print("####################################")
#file = open('example.txt','w')
#file.write("This is a write command")
#file.write("It allows us to write in a particular file")
#file.close()