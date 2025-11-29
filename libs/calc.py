import os 
import time

def option():
    print("""
    1. Add
    2. Minus
    3. X
    4. /""")

def add(x, y):
    print(x + y)
    print("Clearing in 3 seconds")
    time.sleep(3)
    os.system("clear")



def minus(x, y):
    print(x - y)
    print("Clearing in 3 seconds")
    time.sleep(3)
    os.system("clear")

def multiply(x, y):
    print(x * y)
    print("Clearing in 3 seconds")
    time.sleep(3)
    os.system("clear")

def division(x, y):
    print(x / y)
    print("Clearing in 3 seconds")
    time.sleep(3)
    os.system("clear")