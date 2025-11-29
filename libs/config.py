import json
import os

def callapp(app):
    os.system(app)

def createcfg():
    AppsToOpen = input("What program you need? : ")
    #create JSON file with cfg data
    data = {
    "app": AppsToOpen
    }   
    #save cfg to JSON file
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
