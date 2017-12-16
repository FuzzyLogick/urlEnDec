#!/usr/bin/env python3


'''This python script does two things:

1) Convert plain text into HTML URL encoded string.
or
2) Convert HTML URL encoded string into plain text.


This script depends on urllib to run.

This Python script was written by James Russell.

Usage: ./urlEnDec.py

This is version 1.0
'''


from urllib.parse import quote , unquote
import sys



messageNum = "Enter the number to make your selection:"
messageString = "Ready for string."
messageBye = "Type BYE to exit."


while True:

    print("")
    print("")    
    print(messageNum)
    print("")
    print("1:  Encode")
    print("2:  Decode")
    print("")
    print("")
    print(messageBye)
        
    iput = input()



    if iput == "1":
        print("")
        print("Set to  ENCODE: ")    
        print("")
            
        while True:
            print("")
            print(messageString)
            iput = input()
        
            if len(iput) != 0 and iput.upper() != "BYE":
                print("")
                print("")
                print(quote(iput))
                print("")
                print("")
            
            elif iput.upper() == "BYE":
                sys.exit()
            
            else:
                continue    

    
    
    elif iput == "2":
        print("")
        print("Set to  DECODE: ")    
        print("")
                
        while True:
            print("")
            print(messageString)
            iput = input()
        
            if len(iput) != 0 and iput.upper() != "BYE":
                print("")
                print("")
                print(unquote(iput))
                print("")
                print("")
            
            elif iput.upper() == "BYE":
                sys.exit()
            
            else:
                continue    


                       
    elif iput.upper() == "BYE":
        sys.exit()


       
    else:
        continue