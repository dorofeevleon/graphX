# Update this text to match your story.
start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
There is a hallway to your right and to your left.
'''

print(start)

while True:
    print("Type 'left' to go left or 'right' to go right.")
    user_input = input()
    if user_input == "left":
        print("You decide to go left and you've landed in a pit of fire.")


    elif user_input == "right":
        print("You choose to go right and you've fallen in a out of water.")

    else: print(start)
