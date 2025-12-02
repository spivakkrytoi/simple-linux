import os
import sys
import time
import colorama
from colorama import Fore, Style
from art import *
from rich.progress import Progress
import rainbowtext
from datetime import datetime

from libs import calc
from libs import config
from libs import settings
from libs.welcome import print_ascii_slow

month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
         "December"]

colorama.init()
os.system("clear")

with Progress() as progress:
    task = progress.add_task("Loading simple pomagator...", total=100)
    while not progress.finished:
        progress.update(task, advance=1)
        time.sleep(0.02)

os.system("clear")

print_ascii_slow("Welcome   to   SL!", delay=0.005)

def texttoart():
    listOfFonts = '''
    1. Small
    2. Medium
    3. Large
    '''
    print(listOfFonts)
    
    try:
        font = int(input("What font do you need? (Number of font): "))
    except ValueError:
        print("Please enter a valid number!")
        return
    
    atts = 5
    
    for i in range(atts):
        print(f"\n--- Attempt {i+1}/{atts} ---")
        
        send_to_art = input("Text: ")
        
        if font == 1:
            art_text = text2art(send_to_art, font='small')
        elif font == 2:
            art_text = text2art(send_to_art, font='medium')
        elif font == 3:
            art_text = text2art(send_to_art, font='large')
        else:
            print("Incorrect number of font! Please choose 1, 2, or 3.")
            try:
                font = int(input("What font do you need? (Number of font): "))
                continue
            except ValueError:
                print("Invalid input. Ending program.")
                break
        
        print(f"You have: {atts - i - 1} attempts remaining")
        print(art_text)
    
    print("\nBuy some new atts at: example.com")


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
    now = "~Time:" + datetime.now().strftime("%d") + " " + month[month_now] + " " + datetime.now().strftime(
        "%H:%M" + "~")
    print("    " + Fore.RED + now)
    print(options)

    try:
        choose = int(input("Enter option: "))
    except ValueError:
        time.sleep(1)
        os.system("clear")
        continue

    if choose == 1:
        os.system("clear")
        texttoart()
    elif choose == 2:
        os.system("clear")
        calculator()
    elif choose == 3:
        os.system("clear")
        cfgChoose = '''
        What you need?
        1. Create config
        2. Load config
        3. Return to menu
        '''
        print(cfgChoose)
        cfginput = int(input(": "))
        if cfginput == 1:
            os.system("clear")
            appquanty = int(input("How many programs you need to add to your config?"))
            config.createcfg(appquanty)
        elif cfginput == 2:
            config.menu()
            cfgToLoad = input("What config you need to load? (just name after /Configs/): ")
            config.loadcfg(cfgToLoad)
        elif cfginput == 3:
            os.system("clear")
    elif choose == 99:
        os.system("clear")
        print("Goodbye!")
        sys.exit(0)
    else:
        print("Incorrect number!")
        os.system("clear")