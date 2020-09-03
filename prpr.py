# These lines you can keep as is
print("Think of a number between 1 and 100 (inclusive)")
print("I am going to guess what it is")
input("Press enter when you are ready to play")

# Here you might want to initialize some variables
low = int(1)
high = int(100)
guess = 50
guessing_game = True
counter = 0
# Then start a while loop
while guessing_game == True:
    # These lines you can keep as is
    if counter == 7:
        print("Tsk, tsk, don't try to cheat me")
        guessing_game = False
        break
    counter += 1
    guess = (low + high) // 2
    print("Is the number", guess, "?")
    print("Type one of the following letters and press enter:")
    print("h: if the guess is too (h)igh")
    print("l: if the guess is too (l)ow")
    print("c: if the guess is (c)orrect")
    print("q: to (q)uit the game")
    cmd = input()
    
    if cmd == "h":
        high = ((low + high) // 2) - 1
    elif cmd == "l":
        low = ((low + high) // 2) + 1
    elif cmd == "c":
        print("I AM VICTORIOUS")
        guessing_game = False
    elif cmd == "q":
        print("Quitter")
        guessing_game = False
    

    # Now it's up to you to check the command and take appropriate action

