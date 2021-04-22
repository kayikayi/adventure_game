from StoryAFile import storyA
from StoryBFile import storyB

print("----------4000CEM Week 4 Lab 2 Task----------")
print("----------------Murder House---------------")
print("---------------<Nica Dragos>--------------")
print("\n")

print("You just moved in. You enter in the house and from nowhere the door shuts behinde you.What do you do?")
print("a) It was just the wind...")
print("b) Try to get out")
answer = input("Enter a or b: ")
if answer == "a":
    storyA()
elif answer == "b":
    print("The door is loked, you panic and scream for help...")
    storyB()
else:
    print("That is not an option")
    