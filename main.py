isGameOver = False
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
            print("The being falls to the ground with a deafening thud. It lets out a faint moan, and then appears to be dead.")
            print("Do you approach the being or not? (Enter 'yes' or 'no')")
            appr = input()
            if appr == 'yes':
                print("You decide to walk up to the being. As you approach it, you recognize it to be somewhat of a lion, except much bigger.")
                print("The oversized lion's mouth is hanging open, and you can see it's long row of sharp teeth.")
                print("You shudder with fear, even though the beast is clearly dead.")




if char == "2":
    print("insert story")
    print("insert story")
    dir1 = input()
if isGameOver == True:
    print("Thanks for playing, hope you enjoyed!")
