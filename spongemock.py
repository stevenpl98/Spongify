import spongemock
import os

while True:
    text= input("Enter text to spongify: ")
    print("Converting...\n")
    stext= os.system('spongemock %s' % (text))
    print(stext)