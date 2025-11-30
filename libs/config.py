import json
import os
import glob


def menu():
    os.system("clear")
    files = glob.glob("Configs/*.json")
    list = '''
    _________________________
    |List of current configs:
    |
    '''
    print(list)
    for file in files:
        print( "    |" + file) 


def createcfg(prgms):
    #app masive

    apps = []
    os.system("clear")
    #asking for config name
    name = input("Enter the name of cfg: ")
    #receiving list of programs for start
    for i in range(prgms):
            os.system("clear")
            app = input("What program you need? : ")
            apps.append(app)
            print("Current apps:", apps)
    #ask for save or dont save
    os.system("clear")
    quest = input("Do you want to save cfg? (Y/n)")
    if quest == "Y":
            data = { "apps": apps }
            #creating directory for configs in main folder
            os.makedirs("Configs", exist_ok=True)
            project_root = os.path.dirname(os.path.abspath(os.path.join(__file__, "..")))
            configs_dir = os.path.join(project_root, "Configs")
            os.makedirs(configs_dir, exist_ok=True)

            path = os.path.join(configs_dir, name + ".json")
            #saving cfg
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

    else:
        print("Dont saved!")
    return name


# we need to receive name of cfg out of user 
def loadcfg(name):
    #opening cfg file
    project_root = os.path.dirname(os.path.abspath(os.path.join(__file__, "..")))
    configs_dir = os.path.join(project_root, "Configs")
    path = os.path.join(configs_dir, name + ".json")
    with open(path, "r") as file:
        data = json.load(file)
    #checking how many programs we need to load
    programs = data["apps"]
    num_of_apps = len(data) -1
    # loading all programs
    for item in programs:
        os.system(item)
    os.system("clear")