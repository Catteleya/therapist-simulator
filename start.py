import time, sys, json, os
def sprint (s):
    for c in s + '\n':
        sys.stdout.write (c)
        sys.stdout.flush ()
        time.sleep (1. / 15)
DISCLAIMER ="This is NOT to solve your problems, It is to practice on robots so you can be ready... Or just to have fun ;)"
sprint ("Hello!")
time.sleep (2)
sprint ("DISCLAIMER: " + DISCLAIMER)
def ssim ():
    sprint ("Do you wish to continue?")
    startsim = input ("(lower case!!) y/n ")
    if startsim  == "n":
        sprint("I see how it is...")
        spinrt("Ok, ok.. Cya, I guess...")
        time.sleep(1.5)
        sprint("Why would you open this application just to say no?")
        time.sleep(2)
        sprint("Y'know what?")
        time.sleep(.7)
        sprint("I dont care")
        time.sleep(.7)
        sprint("You are gonna do it anyway")
        open(os.path.join(sys.path[0], "stage1.py"), "r")
    elif startsim  == "y":
        sprint ("Alright!")
        sprint ("Starting simulator...")
        time.sleep(2)
        open(os.path.join(sys.path[0], "stage1.py"), "r")
    else:
        os.system("clear")
        sprint ("Please choose y (Yes) or n (No)")
        ssim()
ssim()
