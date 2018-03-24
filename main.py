import keyboard
isGameOver = False
isGameDone = False
level = 1
dir = 0
dir1 = 0
soldierinv = []
healerinv = []
name = input("Enter your name: ")
print(name + ". That's a good name. Choose your character.")
print("1: Soldier\n2: Healer")
char = input()
if char == "1":
    print("You are " + name + ", and you have just landed on a strange planet.")
    print("You departed from the planet XRS-1723 100 years ago, on your quest to find life in other galaxies.")
    print("As your spaceship touches down, you look around you. There is nothing but desert for miles. It is like your planet, but much colder.")
    print("You step out onto the yellow sand. Do you go left or right? (Enter 'left' or 'right')")
    dir = input()
    if dir == "right":
        print("You decide to go right. After walking for a few minutes, what looks like a city comes into view.")
        print("You see many tall buildings that look like they are made of steel and have no windows. It is nothing like your home planet's cities.")
        print("")
    if dir == "left":
        print("You decide to go left. You walk for what seems like miles, with still nothing other than sand dunes to see.")
        print("Finally, you see something faintly in the distance. It appears to be approaching with great speed.")
        print("As it gets closer, you are able to make out the shape. It is very tall, taller than your rocketship.")
        print("Do you wait for it to get closer, or do you pull out your gun? (Enter 'wait' or 'gun')")
        choice = input()
        if choice == "wait":
            print("You decide to wait until it gets closer to do anything.")
            print("As you watch, it gets faster and faster, coming closer faster than you had expected at first.")
            print("Suddenly, a chill goes down your spine. You pull out your gun, but it is too late.")
            print("Before you have time to pull the trigger, you see a flash of purple light and everything goes black.")
            print("You are dead.")
            isGameOver = True
        if choice == "gun":
            print("You were always a cautious person, so just in case, you have your gun at the ready.")
            print("As you watch, it suddenly advances with speed you have never seen before.")
            print("Luckily, you have your gun out and cocked, and you fire just in time.")
            print("The beast falls to the ground with a deafening thud. It lets out a faint moan, and then appears to be dead.")
            print("You leveled up!")
            level += 1
            print("Do you approach the being or not? (Enter 'yes' or 'no')")
            appr = input()
            if appr == "yes":
                print("You decide to walk up to the being. As you approach it, you recognize it to be somewhat of a lion, except much bigger.")
                print("The oversized lion's mouth is hanging open, and you can see its long row of sharp teeth.")
                print("You shudder with fear, even though the beast is clearly dead.")
                print("Do you investigate the beast further or walk away? (Enter 'beast' or 'walk')")
                invest = input()
                if invest == "walk":
                    appr = "no"
            if appr == "no":
                print("You decide to walk away instead of investigating the beast.")
                print("It was a lucky decision, because as you walk away, you hear a low growl from behind you.")
                print("Do you turn around to look or do you just run away? (Enter 'look' or 'run')")
                choice = input()
                if choice == "look":
                    print("You turn around to look at the beast, you see the lion on its feet. 'Turns out my bullet wasn't effective,' you think to yourself.")
                    print("Unfortunately, that was the last thing you would ever think, because the beast jumps at you.")
                    print("It has a very powerful jump, and you have no time to react. You black out on impact.")
                    print("You are dead.")
                    isGameOver = True
                if choice == "run":
                    print("As soon as you hear the growl, your mind enters panic mode. You run as fast as you can towards your spaceship.")
                    print("You make it just in time. You clamber into your ship and slam the door behind you.")
                    print("The beast cannot enter, and you blast off, postponing your mission.")
                    isGameDone = True





if char == "2":
    print("insert story")
    print("insert story")
    dir1 = input()
if isGameOver == True:
    print("Thanks for playing, hope you enjoyed!")
if isGameDone == True:
    print("Thanks for playing, hope you enjoyed! You can continue your adventure in the next episode.")
