from sys import exit

def knife():
    print("""
    You take the knife and crawl towards the door.
    You see a narrow hallway that seems to be clear.
    Do you take the left or the right?
    """)

    choice= input("> ")

    if "left":
        print("You turn the left and walk fast but silently. You spot one unarmed guard.")
        print("What do you do? stab or sneak around")
        choice = input("> ")

        if choice == "stab":
            print("You surprised the guard and killed him. You picked up a key")
            key()
        elif choice == "sneak around":
            print("You successfully snuck around the guard.")
            next()
        else:
            print("That is not a valid answer")
            knife()
    elif "right":
        dead("You met a group of guards who shot you before you could react.")
    else:
        knife()

def gun():
    print("""
    You take the gun and crawl towards the door.
    You see a narrow hallway that seems to be clear.
    Do you take the left or the right?
    """)

    choice= input("> ")

    if "left":
        print("You turn the left and walk fast but silently. You spot one unarmed guard.")
        print("What do you do? shoot, sneak around, or attack?")
        choice = input("> ")

        if choice == "shoot":
            dead("The sound alerted other guards who quickly found you and killed you.")
        elif choice == "sneak around":
            print("You successfully snuck around the guard.")
            next()
        elif choice == "attack":
            print("The guard is an expert in self defense. He knocks you out.")
            start()
        else:
            print("That is not a valid answer")
            gun()
    elif "right":
        dead("You met a group of guards who shot you before you could open fire.")
    else:
        gun()

def next():
    """
    You approach another hallway where you see another guard.
    Do you use your weapon or sneak around?
    """
    choice = input ("> ")

    if "weapon" in choice:
        print("You got rid of the guard easily.")
        print("Thankfully nobody heard.")
        print("You find a key in the guard's pocket.")
        key()
    if "sneak" in choice:
        print("You snuck around him successfully.")
        door_fail()

def key():
    print("You reached the door just as the alarm bell started ringing.")
    print("You have a key, so they weren't able to catch you in time.")
    print("Good job, you escaped.")

def door_fail():
    print("You reached the door just as the alarm bell started ringing.")
    print("You frantically try to open the door but it would not budge.")
    dead("The guards catch up to you and kill you.")

def dead(why):
    print(why, "You die.")
    exit(0)

def start():
    print("""
    You open your eyes to find yourself tied up in an unknown bedroom.
    Thankfully you learned how to untie knots and got out of those restraints.
    You find a knife and a gun in the room.
    Which one do you take?
    """)

    choice = input("> ")

    if choice == "knife":
        knife()
    elif choice == "gun":
        gun()
    else:
        dead("You don't have that.")

start()
