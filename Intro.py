import time
from PathA import *
from PathB import *
from PathC import *

def intro():
  print ("You wake up, groggy and confused. You look around, trying to get\n"
  "your bearings only to have no idea where you are but you realise its\n"
  "a forest clearing. You try to stand and although your legs feel like jelly\n" 
  "you eventually get to your feet.\nOn checking your pockets, you find a\n"
  "small pocket knife, some string, a mint covered in fluff and a strange\n"
  "packet of powder. Suddenly from between the trees, in the darkness, you\n"
  "hear a low growl. Do you:")
  time.sleep(1)
  print("\n A. Stay perfectly still\n"
  " B. Grab the pocket knife and get ready\n"
  " C. Throw the fluff covered mint towards the noise")
  
  loop = True

  while(loop):
    choice=str(input("\nPick a letter: ")).upper()

    if(choice == "A"):
      pathA()
      loop = False
    elif(choice == "B"):
      pathB()
      loop = False
    elif(choice == "C"):
      pathC()
      loop = False
    elif(choice == "Q"):
      quit = str(input("Are you sure you want to quit? (Y/N): ")).upper()
      qLoop = False
      if(quit == "Y"): 
        qLoop = True
        loop = False
      else:
        print("Resuming game...")
        time.sleep(1)
      while(qLoop):
        saveFile=str(input("You have chosen to quit, would you like to save your progress? (Y/N): ")).upper()
        if(saveFile == "Y"):
          # save the file
          with open('save.txt', 'w') as output:
            output.write(__name__+".py")
          print("Progress saved successfully. Thank you for playing Octofluff Traveller!")
          qLoop = False
        elif(saveFile == "N"):
          print("You will quit without saving your progress. Thank you for playing Octofluff Traveller!")
          qLoop = False
        else:
          print("I think you accidentally chose something other than Y or N, please try again")
    else:
      print("I think your finger slipped, please try again chosing only A, B or C")
      time.sleep(1)

if __name__ == "builtins":
  intro()