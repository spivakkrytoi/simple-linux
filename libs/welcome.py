import time
from art import text2art
from colorama import Fore, Style

def type_out(text, delay=0.05):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def print_ascii_slow(text, color=Fore.GREEN, delay=0.02):
    art = text2art(text, font = 'small')
    colored = color + art + Style.RESET_ALL
    for line in colored.splitlines():
        type_out(line, delay)
