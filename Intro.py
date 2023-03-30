import time

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "Yes", "yes", "YES"]
no = ["N", "n", "No", "no", "NO"]

required = ("\nUse only A, B, C\n")

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

  choice=str(input("\nPick a letter: "))