from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

    def parentClassFunction(self):
        print("I was defined only in parent class")

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        # be sure to print out the last scene
        current_scene.enter()

class Death(Scene):
    quips = ["You died. You kinda suck at this.",
        "Your Mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."
        ]
    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print(dedent("""A BUNCH OF NONSENSE
        SHOOT, DODGE, JOKE?"""))

        action = input("> ")

        if action == "SHOOT":
            print("A bunch of stuff happens and you get eaten")
            return 'death'

        elif action == "DODGE":
            print("You tried but the alien kills you anyways")
            return 'death'

        elif action ==  "JOKE":
            print("you survive hooray!")
            return 'laser_weapon_armory'

        else:
            print("not an option")
            return 'central_corridor'

    

class LaserWeaponArmory(Scene):

    def enter(self):
        print("you arrive at the new room, now open the lock, you have 10 tries gl")

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses <9:
            print("some sound")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print("good job now proceed")
            return 'the_bridge'

        else:
            print("rip, you ran out of tries")
            return 'death'

class TheBridge(Scene):

    def enter(self):
        print("Now there  are aliens on the bridge, do something")
        print("throw bomb or slowly place bomb?")
        action=  input("> ")

        if action == "throw bomb":
            print("They see you and you die")
            return 'death'

        elif action == "slowly place bomb":
            print("good  job you survive")
            return 'escape_pod'
        else:
            print("Not an option")
            return 'the_bridge'

class EscapePode(Scene):

    def enter(self):
        print("You find 5 pods, choose  one")

        good_pod = randint(1,5)
        guess= input("[pod #]> ")


        if int(guess) != good_pod:
            print("nope, you are unlucky bye bye")
            return 'death'

        else:
            print("wow lucky, good job you survived")
            return 'finished'

class Finished(Scene):

    def enter(self):
        print("Yay good job")
        return 'finished'


class Map(object):

    scenes= {
    'central_corridor': CentralCorridor(),
    'laser_weapon_armory': LaserWeaponArmory(),
    'the_bridge': TheBridge(),
    'escape_pod': EscapePode(),
    'death': Death(),
    'finished': Finished(),
    }
    def __init__(self, start_scene):
        self.start_scene=start_scene
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    def opening_scene(self):
        return  self.next_scene(self.start_scene)
testObject = Finished()
testObject.parentClassFunction()
exit()
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
