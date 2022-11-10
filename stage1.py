import time, sys, json, os
def sprint (s):
    for c in s + '\n':
        sys.stdout.write (c)
        sys.stdout.flush ()
        time.sleep (1. / 15)
def slowerprint (s):
    for c in s + '\n':
        sys.stdout.write (c)
        sys.stdout.flush ()
        time.sleep (1. / 1)
sprint ("Simulation loaded...")
name = input("Hello Dr. ")
drname = "Dr. " + name
time.sleep (1)
sprint ("(Every time you get a new patient you have to tell us your name again, Sorry!)")
time.sleep (2)
os.system ("clear")
sprint (f'So, {drname}...')
sprint ("What do you do these days?")
time.sleep(2)
slowerprint ("...")
time.sleep(1)
sprint("Not much of a talker, 'eh?")
time.sleep(.5)
sprint("Well you gotta talk when you have patients!")
sprint("Lets get started!")
time.sleep(.8)
os.system("clear")
