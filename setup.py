__name__ = "__main__"


import os

path = os.getcwd()

def setup():
    file = open('notenow.bat', 'x')
    file.write("python " + path + "\main.py")

text = input("What is your preferred text editor? (Atom, Sublime Text, Notepad) ")
if text == "atom":
    file = open('main.py', 'a')
    file.write('os.system("atom " + t + ".txt")')
    setup()
elif text == "sublime text":
    file = open('main.py', 'a')
    file.write('os.system("sublime-text " + t + ".txt")')
    setup()
elif text == "notepad":
    file = open('main.py', 'a')
    file.write('os.system("notepad " + t + ".txt")')
    setup()
else:
    print('Did not recognize that input. Try again.')
