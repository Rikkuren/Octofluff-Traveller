import time
from Intro import intro

def loadSave():
    try:
        file = open("save.txt","r")
        newPlayer = False
        file.close()
    except IOError:
        newPlayer = True

    print("Type Q to quit during any choice")
    time.sleep(2)
    
    if (newPlayer == False):
        loadLoop = True
        while(loadLoop):
            loading=str(input("You appear to already have a saved game.\nDo you wish to load this? (Y/N): ")).upper()
        
            if(loading == "Y"):
                print("Loading saved game...")
                time.sleep(2)
                with open('save.txt', 'r') as output:
                    loadFile = output.readlines()
                exec(open(f'{loadFile[0]}').read(), {})
            elif(loading == "N"):
                print("You will start from the beginning of Octofluff Traveller now...")
                loadLoop = False
                time.sleep(2)
                intro()
            else:
                print("Please use only Y or N. While other options exist, they will not be successful!")
            
    else:          
        time.sleep(2)
        intro()

loadSave()