import sys
'''This module provides access to some variables
used or maintained by the interpreter and to functions
that interact strongly with the interpreter.
It is always available.'''

argumentList=sys.argv
'''We build a list named argumentList, and fill it up with arguments from the command line'''

g=argumentList[1]
'''Here we set our variable 'g' as the the second argument from the argv list,
the first argument with the index '0' is the name of the file passes after py/python'''

print("The variable received is "+g)
'''Use the varibale however you want to, here we are just printing it!'''
