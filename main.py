import random
isGameOver = False
isGameDone = False
level = 1
dir = 0
dir1 = 0
soldierxp = 100
healerxp = 100
soldierinv = []
healerinv = []

name = input("Enter your name: ")
print("*During the adventure, press 'Enter' to continue after reading each line.*")
input()
char = "1"
if char == "1":
    print("You are " + name + ", and you have just landed on a strange planet.")
    input()
    print("You departed from the planet XRS-1723 100 years ago, on your quest to find life in other galaxies.")
    input()
    print("As your spaceship touches down, you look around you. There is nothing but desert for miles. It is like your planet, but much colder.")
    input()
    print("You step out onto the yellow sand. Do you go left or right? (Enter 'left' or 'right')")
    dir = input()
    if dir == "right":
        print("You decide to go right. After walking for a few minutes, what looks like a city comes into view.")
        input()
        print("You see many tall buildings that look like they are made of steel and have no windows. It is nothing like your home planet's cities.")
        input()
        print("You get closer to the city. Something doesn't feel right to you, but you can't place the feeling.")
        input()
        print("Suddenly, it hits you. The city is completely silent.")
        input()
        print("You go through the city gates, onto the first road. The city is completely deserted.")
        input()
        print("Do you get creeped out and turn around or do you continue on? (Enter 'leave' or 'continue')")
        choice = input()
        if choice == "leave":
            print("You decide it isn't safe and you turn around to leave.")
            input()
            print("When you turn around, the gates are closed. A chill runs down your spine as you wonder how they got that way so quickly and so silently.")
            input()
            print("Your only choice now is to continue into the city.")
            input()
            choice = "continue"
        if choice == "continue":
            print("You pay no attention to your first instincts, and you continue on deeper into the city.")
            input()
            print("You come to a dead end. Do you go left or right? (Enter 'left' or 'right')")
            dir = input()
            if dir == 'right':
                print("You decide to go right. As you walk down the deserted street, you begin to feel many people are watching you.")
                input()
                print("You walk more cautiously now, expecting something could happen at any moment.")
                input()
                print("The road goes on farther than you can see, with no more turns.")
                input()
                print("Do you turn around or continue on down the road? (Enter 'turn' or 'continue')")
                choice = input()
                if choice == "continue":
                    print("You decide to continue on. As you walk farther along, the air becomes foggy, to the point where you can't even see a foot in front of you.")
                    input()
                    print("The fog becomes even thicker, and you notice a small red dot piercing through the fog.")
                    input()
                    print("The dot begins to pulse and you hear a beeping sound. Suddenly, there is a blinding flash and an ear-splitting squealing noise.")
                    input()
                    print("You are thrown backwards, and you lose your vision for a few seconds.")
                    input()
                    print("Once you can see again, the fog has cleared.")
                    input()
                    print("You get up and look around. All of the buildings have disappeared and you can see your ship in the distance.")
                    input()
                    print("Relieved, you run to your ship and get in. You blast off, extremely confused and disoriented.")
                    input()
                    print("You hope you can do better on your next mission.")
                    input()
                    Sxp = random.randint(10,100)
                    print("You have earned "+ str(Sxp) + " xp")
                    soldierxp = soldierxp + Sxp
                    print("Current xp needed for next level: " + str(100 - Sxp))
                    input()
                    isGameDone = True
                if choice == "turn":
                    print("You go back towards where you entered the city.")
                    input()
                    print("As you approach the entrance, a robot jumps out from behind the corner. You black out on impact.")
                    input()
                    print("You are dead.")
                    input()
                    Sxp = random.randint(10,100)
                    print("You have earned "+ str(Sxp) + " xp")
                    soldierxp = soldierxp + Sxp
                    print("Current xp needed for next level: " + str(100 - Sxp))
                    input()
                    isGameOver = True
            if dir == "left":
                print("You decide to go left. As soon as you turn the corner, a robot jumps at you and you black out on impact.")
                input()
                print("You are dead.")
                input()
                Sxp = random.randint(10,100)
                print("You have earned "+ str(Sxp) + " xp")
                soldierxp = soldierxp + Sxp
                print("Current xp needed for next level: " + str(100 - Sxp))
                input()
                isGameOver = True
    if dir == "left":
        print("You decide to go left. You walk for what seems like miles, with still nothing other than sand dunes to see.")
        input()
        print("Finally, you see something faintly in the distance. It appears to be approaching with great speed.")
        input()
        print("As it gets closer, you are able to make out the shape. It is very tall, taller than your rocketship.")
        input()
        print("Do you wait for it to get closer, or do you pull out your gun? (Enter 'wait' or 'gun')")
        choice = input()
        if choice == "wait":
            print("You decide to wait until it gets closer to do anything.")
            input()
            print("As you watch, it gets faster and faster, coming closer faster than you had expected at first.")
            input()
            print("Suddenly, a chill goes down your spine. You pull out your gun, but it is too late.")
            input()
            print("Before you have time to pull the trigger, you see a flash of purple light and everything goes black.")
            input()
            print("You are dead.")
            Sxp = random.randint(10,100)
            print("You have earned "+ str(Sxp) + " xp")
            soldierxp = soldierxp + Sxp
            print("Current xp needed for next level: " + str(100 - Sxp))
            input()
            isGameOver = True
        if choice == "gun":
            print("You were always a cautious person, so just in case, you have your gun at the ready.")
            input()
            print("As you watch, it suddenly advances with speed you have never seen before.")
            input()
            print("Luckily, you have your gun out and cocked, and you fire just in time.")
            input()
            print("The beast falls to the ground with a deafening thud. It lets out a faint moan, and then appears to be dead.")
            input()
            print("Do you approach the being or not? (Enter 'yes' or 'no')")
            appr = input()
            if appr == "yes":
                print("You decide to walk up to the being. As you approach it, you recognize it to be somewhat of a lion, except much bigger.")
                input()
                print("The oversized lion's mouth is hanging open, and you can see its long row of sharp teeth.")
                input()
                print("You shudder with fear, even though the beast is clearly dead.")
                input()
                print("Do you investigate the beast further or walk away? (Enter 'beast' or 'walk')")
                invest = input()
                if invest == "walk":
                    appr = "no"
            if appr == "no":
                print("You decide to walk away instead of investigating the beast.")
                input()
                print("It was a lucky decision, because as you walk away, you hear a low growl from behind you.")
                input()
                print("Do you turn around to look or do you just run away? (Enter 'look' or 'run')")
                choice = input()
                if choice == "look":
                    print("You turn around to look at the beast, you see the lion on its feet. 'Turns out my bullet wasn't effective,' you think to yourself.")
                    input()
                    print("Unfortunately, that was the last thing you would ever think, because the beast jumps at you.")
                    input()
                    print("It has a very powerful jump, and you have no time to react. You black out on impact.")
                    input()
                    print("You are dead.")
                    input()
                    Sxp = random.randint(10,100)
                    print("You have earned "+ str(Sxp) + " xp")
                    soldierxp = soldierxp + Sxp
                    print("Current xp needed for next level: " + str(100 - Sxp))
                    input()
                    isGameOver = True
                if choice == "run":
                    print("As soon as you hear the growl, your mind enters panic mode. You run as fast as you can towards your spaceship.")
                    input()
                    print("You make it just in time. You clamber into your ship and slam the door behind you.")
                    input()
                    print("The beast cannot enter, and you blast off, postponing your mission.")
                    input()
                    Sxp = random.randint(10,100)
                    print("You have earned "+ str(Sxp) + " xp")
                    soldierxp = soldierxp + Sxp
                    print("Current xp needed for next level: " + str(100 - Sxp))
                    input()
                    isGameDone = True





if char == "2":
    print("insert story")
    print("insert story")
    dir1 = input()
if isGameOver == True:
    print("Thanks for playing, hope you enjoyed!")
if isGameDone == True:
    print("Thanks for playing, hope you enjoyed! You can continue your adventure in the next episode.")
