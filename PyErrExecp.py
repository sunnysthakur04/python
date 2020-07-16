#/usr/bin/python

try:
    filename = input('Enter file name: ')
    fobj = open(filename, 'r')
    for eachLine in fobj:
        print(eachLine),
except IOError:
    print('file open error:')