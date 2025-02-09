#B"SD


'''Key Logger Spyware Exercise – Part 1
In this exercise, you will learn how to approach a problem, break it down into sub-problems, and then write a program that implements the solution step by step. The goal is to understand the thought process, not just to write the code. At no stage should you use AI tools such as ChatGPT.

Explanation of a Key Logger Program
In this exercise, you will need to create a program that monitors user activity, regardless of the application they are using—whether they are searching on Google, typing in the command line, or writing an email—by logging every keystroke. The program records the activity and saves it to a file. These files will be stored in an encrypted format and can only be decrypted by the spy who has the encryption key.

This exercise is divided into two parts:

The current part focuses on monitoring user activity.
The second part, later in the course, will deal with saving the data to files and encrypting it.
Functional Requirements
The program must track all user keystrokes, regardless of which application they are using.
The program must store all typed characters in an appropriate data structure.
When the command "show" is entered in the terminal, the program must print all recorded keystrokes since the last print operation.
If it is the first print operation, it should display all keystrokes since the program started.
Each printout must be internally divided by timestamps. Every minute must be printed separately, with the timestamp as the first line, followed by all keystrokes from that minute.
Example output:
***** 12:01 04/11/2024 ******
Ze hipusim google shakti
***** 12:02 04/11/2024 ******
Lorem ipsum blah blah bla
The program must run in the background and not interfere with the user’s activities.
The program must be able to terminate via a keyboard shortcut, such as Shift + Ctrl + F.
Code Quality Requirements
Use meaningful variable and function names.
Break the program into clear and focused functions, and provide comments explaining what each function does.
The main program should only consist of function calls.
No function should be too long—generally, functions should be between 5 to 15 lines.
Exercise Stages
Step 1: Identifying the Problem and Defining Requirements

Task: Describe in simple words what your program needs to do. Try to think about the main steps required to build a program that tracks keystrokes and stores them in a file.
Expected Outcome: A written description of the program’s requirements.

Step 2: Researching Modules and Libraries

Task: Research existing Python modules that can help you capture keystrokes. Check what each module offers and how it can be used.
Expected Outcome: Select the most suitable module (e.g., pynput) and write a few basic usage examples.

Step 3: Writing a Function to Capture Keystrokes

Task: Write a basic function that monitors keystrokes and prints them to the console. Do not worry about saving the data to a file yet—that will be handled in Part 2 of the exercise later in the course.
Expected Outcome: A working function that prints keystrokes in real-time.

Step 4: Making the Program Run in the Background

Task: Modify your code so that the program runs in the background, without interrupting the user’s activities.
Expected Outcome: A program that runs silently and collects data without interfering with the computer’s operation.

Step 5: Adding a Shortcut to Stop the Program

Task: Write code that allows the program to be terminated via a keyboard shortcut.
Expected Outcome: A function that immediately stops the program when a predefined shortcut is pressed.

'''




''' 
*******
Step 1: Identifying the Problem and Defining Requirements


Ok this is a pretty simple task. The goal is to track the users keypresses and display them when asked.
In a finer sense, there are critical details. The program needs to be a python code that runs in the 
background, it shouldn't interfere with the user. This is supposed to be spyware, so it shouldn't be
visible to the user in any way. Beyond that, the technical requirements stipulate that key presses are saved
by the minute of there typing. So even if "hi" and "hello" were typed 10 seconds apart, if they were in the
objectively different minutes of 12:00 and 12:01, they would be printed sepperately. These key presses need
to be stored in a data structure, and seemingly a dictionary would be the best option. This is because we are
linking the input to a time. And while the key is certainly the time stamp, it reamins to be seen if
it is better to use a list of chars for the input, or to save it as the string (which I imagine would be 
the default). Since both are additive structures that gobble memory when concatenaded or created anew, I don't
think this makes a huge difference. But seeing that we will later be saving the input to a file, saving the
value as string is more sensible. Instead of having to convert data later we can simply save the string. I will
stress, details such as this are subject to change as implementation progresses. As for the file type we will use, 
as we are saving plain text, a .txt file should suffice. Beyond that, we
Finally we need to implement two custom keyboard short cuts. One is the "show" shortcut, which will print the user inputs
and the second is a "kill command" which will stop the program when a proscribed sequence of keys is pressed. Yalla, let's
get to it.
*******

Step 2: Research
Step 2: Researching Modules and Libraries

Task: Research existing Python modules that can help you capture keystrokes. Check what each module offers and how it can be used.
Expected Outcome: Select the most suitable module (e.g., pynput) and write a few basic usage examples.

Ok I want pynput vs keyboard

pynput: Seems like it should be the winner. Firsly because it was the suggested example, and second since it says that it is non-blocking.
It also seems to do what was proscribed like  (Code below taken from https://pypi.org/project/pynput/)

A) Capture keyboard input

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
OR

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

B)block or not block
    event = events.get(1.0)
    if event is None:
          OR
  with keyboard.Events() as events:
  for event in events:
    if event.key == keyboard.Key.esc:
      break
      
C) import method as
from pynput import keyboard

D) you can even control the keyboard using the controller import...and maybe we can 
use that later on.

Keyboard:
    I was going to do more research on this...but it literally says on https://pypi.org/project/keyboard/
    that this program makes no attempt to hide itself...so don't use it for keyloggers

 





'''

''' * ok task 3 is to implement a function that captures key strokes...no further things so lets start there '''



#B"SD
from pynput.keyboard import Listener

class keyLogger:
    def __init__(self):
        self.start = start(self)


def print_back(self, key):
    print(key)

      
def start(self):
    try:
        with Listener(on_press=self.print_back(sl)) as listener:
            listener.join()
    except KeyboardInterrupt as key:
        print(key)

if __name__ == "__main__":
    keyLogger()

# import pynput
# from pynput.keyboard import Listener
# from datetime import datetime
# # spy = keyboard.Listener 

# def capture_key_strokes(key): #I HAVE TO TELL IT THO...THAT'S NOT GREAT RIGHT
#   myString = ""
#   try:
#       if format(key.char) == 'x':
#         spy.stop()
#         print(myString)
#       myString +=format(key.char)
#   except AttributeError:
#       myString += format(key)
    
  

# with Listener(capture_key_strokes) as spy: #makes an instence of it
#     spy.daemon = True
#     spy.start()
       
   

# class KeyLogger:
#   def _init_():
#     pass
kigrj1@gmail.com