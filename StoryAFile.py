from time import sleep
def storyA():
    print("You continue unpacking and go to sleep.\nIn the middle of the night a noise from downstairs wakes you up.What do you do?")
    print("a) Going back to sleep \nb) Grab the baseball bat and walk slowly to check what has that")
    x=None
    while x!="a".lower() or x!="b".lower():
      x = input("Enter a or b:")
      if x=="a" or x=="b":
        break
    if x=="a".lower():
      print("You never woke up from the sleep, now you leaving in an etarnal dream, someone killed you!")
      return None
    elif x=="b".lower():
      print("You are in the hallway now. WAIT ... you saw a shadow going downstairs...\nWhat you are doing?")
    print("a)Fallow the mysterious shadow?\nb)Run for your life and try to escape")
    x=None
    while x!="a".lower() or x!="b".lower():
      x = input("Enter a or b:")
      if x=="a" or x=="b":
        break
    if x=="a".lower():
      print("You are brave, what can I say... you going down slowly, your heart is pumping really fast, you breathe faster and faster")
      print("Now you are in the leavingroom... you try to reach the light switch... The light is now on...")
      sleep(3)
      print("Everything is a mess, nothing is where you let it, the table is upside down...")
    if x=="b".lower():
      print("You run to the window and then saw a strange figure... looking at you")
      sleep(2)
      print("And is waving at you...in a creepy way and smiling and pointing to look behind\nYour petrified... to scared to look, you sense the breath behind you")
      sleep(2)
      print("You start to feel someone hands touching you... you try to escape and succeed but with some wounds...")