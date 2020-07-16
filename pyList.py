#/usr/bin/python

squared = [x ** 2 for x in range(4)] # square of nu=
for i in squared:
    print(i)

print("#########################################")

sqdEvens = [x ** 2 for x in range(8) if not x % 2] #square of even numbers in list
for i in sqdEvens:
    print(i)
