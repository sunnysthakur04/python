#/usr/bin/python

aDict = {'host': 'earth'} #Create dict
aDict['port'] = 80  #add to dict
print(aDict)
print(aDict.keys())
print(aDict['host'])
for key in aDict:
    print(key, aDict[key])