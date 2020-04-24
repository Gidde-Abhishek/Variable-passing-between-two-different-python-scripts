import os
''''os module is needed to interact with the command shell of the operating system'''

g = "Abhishek"
'''variable to be passed out'''

commandString="py destination.py "+g
'''we build a command that executes the destination python script with 'g' as a commandline argument'''

os.system(commandString)
'''the command is executed on the system shell'''
