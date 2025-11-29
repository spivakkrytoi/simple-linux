import os
import sys
import time
import colorama
from colorama import Fore, Style
from art import *
from rich.progress import Progress
import rainbowtext
from datetime import datetime

#mine "libs" :)
from libs import calc
from libs import config
from libs.welcome import print_ascii_slow

month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

colorama.init()
os.system("clear")

with Progress() as progress:
    task = progress.add_task("Loading simple pomagator...", total=100)
    while not progress.finished:
        progress.update(task, advance=1)
        time.sleep(0.02)

os.system("clear")

print_ascii_slow("Welcome     back!", delay=0.005)
while True:
    options = rainbowtext.text("""
    _____________________________
   | 1. Text to ASCII generator  |
   | 2. Calculator               |
   | 3. Configs                  |
   | 99. Exit                    |
    -----------------------------
    """)
    month_now = int(datetime.now().strftime("%m")) - 1
    now = datetime.now().strftime("%d") + " " +  month[month_now] + " " + datetime.now().strftime("%H:%M")
    print("    " + Fore.RED + now)
    print(options)

    try:
        choose = int(input("Enter option: "))
    except ValueError:
        time.sleep(1)
        os.system("clear")
        continue

    def texttoart(text):
        text = text2art(text, font='small')
        print(text)

    def calculator():
        calc.option()
        try:
            action = int(input("Enter option: "))
        except ValueError:
            return

        if action == 1:
            os.system("clear")
            x = float(input("Enter number 1: "))
            y = float(input("Enter number 2: "))
            calc.add(x, y)
        elif action == 2:
            os.system("clear")
            x = float(input("Enter number 1: "))
            y = float(input("Enter number 2: "))
            calc.minus(x, y)
        elif action == 3:
            os.system("clear")
            x = float(input("Enter number 1: "))
            y = float(input("Enter number 2: "))
            calc.multiply(x, y)
        elif action == 4:
            os.system("clear")
            x = float(input("Enter number 1: "))
            y = float(input("Enter number 2: "))
            calc.division(x, y)

    def texttoartfnc():
        atts = 5
        for i in range(atts):
            print("You have:", atts - i, "attempts :)")
            send_to_art = input("Text: ")
            texttoart(send_to_art)
        print("Buy some new atts at: example.com")

    if choose == 1:
        os.system("clear")
        texttoartfnc()
    elif choose == 2:
        os.system("clear")
        calculator()
    elif choose == 3:
        os.system("clear")
        print("Coming soon...")
    elif choose == 99:
        os.system("clear")
        print("Goodbye!")
        sys.exit(0)
    else:
        print("Incorrect number!")

    input("\nPress Enter to return to menu...")
    os.system("clear")
