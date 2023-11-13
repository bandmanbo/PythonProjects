#showcasing the utility of pynput
#1. Controlling your mouse
#2. Listening to your mouse
#3. Contolling your keyboard
#4. listening to your keyboard - this will be used in the keylogger
#first we import from the pynput package which utility we will be using which is the Controller

from pynput.mouse import Controller
from pynput.keyboard import Controller

#here we define our function that will control the left to right and top to bottom of our mouse.
#from top left of the screen, this is (0,0)

def controlMouse ():
    mouse = Controller()
    mouse.position = (10,20)

#controlMouse()

#next we will be creating a function that will allow us to control keystrokes
#you cant have the mouse controller and the keyboard controller working at the same time so we stored 'controlMouse()' as a comment.

def controlKeyboard():
    keyboard = Controller()
    keyboard.type("I really am the computer wizard")

controlKeyboard()

#the function will write "I really am the computer wizard" whereever your cursor is ready to type.