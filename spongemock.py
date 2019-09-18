import spongemock
import os

while True:
    text= input("\nEnter text: ")
    print("Spongifying...\n")
    stext= os.system('spongemock %s' % (text))