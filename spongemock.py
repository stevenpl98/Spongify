import spongemock
import os

while True:
    text= input("\nEnter text: ")
    prompt= input("\nContinue/ (y/n): ")
    if prompt == "y":
        print("Spongifying...\n")
        stext= os.system('spongemock %s' % (text))
    else:
        break