from sys import argv
print(type(argv))
print(argv)

name=input('enter something: ')
print(name)
import os
directory = "test123"
path_ = "/home/mohammad/Desktop"
path = os.path.join(path_, directory)
os.mkdir(path)
