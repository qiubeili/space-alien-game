# Rooms:
from sys import exit
from textwrap import dedent
import time

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map= scene_map
    def play(self):
        current_scene= self.scene_map.opening_scene()
        last_scene=self.scene_map.next_scene('final')
        while current_scene != last_scene:
            next_scene_name=current_scene.enter()
            current_scene=self.scene_map.next_scene(next_scene_name)
        current_scene.enter()

class Fail():
    def enter(self):
        print("You have failed...RIP")
        exit(1)
# start
class Start():
    def enter(self):
        print("Please enter your name")
        name = input("> ")

        print(dedent(f"""Hello Agent {name}. You have been selected to exterminate
the aliens on this spaceship. Do you accept? Type \"yes\" to accept and \"no\"
to forfeit the mission.""" ))

        answer = input("> ")

        if answer == "yes":
            return 'bedroom'

        elif answer == "no":
            exit(1)

        else:
            print("You can't read...you can't complete this mission. Goodbye")
            exit(1)

inventory = []
def addinventory(item):
    inventory.append(item)

# Corridor
class Bedroom():
    global inventory
    def enter(self):
        print(dedent("""Every selected agent gets their own armor and weapon. Type
'yes' to pick it up."""))

        action = input("> ")

        if action == "yes":
            print("You picked up basic armor and wooden sword.")
            addinventory("basic armor")
            addinventory("wooden sword")
            input("Press enter to continue")
            print("Here is your inventory: ")
            print(inventory)
            print("Now you're all equipped and ready. Let's go train first.")
            return 'train'

        else:
            print("You cannot begin without the proper weapons...")
            return 'bedroom'

# Cafeteria
class Training():
    def enter(self):
        print(dedent(f"""Welcome Agent {name}! We've been expecting you. You are abroad
spaceship 738."""))
        return 'lobby'

# Lobby
class Lobby():
    def enter(self):
        print(dedent("""The lobby is devoid of aliens. You stay in the lobby waiting
        and waiting. Suddenly everything goes black"""))
        return 'wakeup'


# Alien Spaceship (?)
class AlienSpaceship():
    def enter(self):
        print(dedent("""You find the bomb by the alienspaceship. Quickly, using the skills
        you were taught in school, you try to dismantle it before it explodes. But
        time runs out. You close your eyes bracing for the explosion, but nothing
        comes. You take a peek and instead find a flag saying \"Good job you made it\" """ ))
        return 'final'
class Final():
    def enter(self):
        print(dedent("""The general notes that you were the only one who made it to the dock. You
        got a promotion and a whole week of vacation as a reward. You are extremely happy but
        you then hear this annoying sound...sounds familiar."""))
        return 'final'

#something to start game and make the rooms link together
class Map(object):

    scenes = {
    'start': Start(),
    'bedroom': Bedroom(),
    'train': Training(),
    'lobby': Lobby(),
    'alienspaceship':  AlienSpaceship(),
    'fail': Fail(),
    'final': Final(),
    }

    def __init__(self, start_scene):
        self.start_scene=start_scene
    def next_scene(self,scene_name):
        val = Map.scenes.get(scene_name)
        return val
    def opening_scene(self):
        return self.next_scene(self.start_scene)

start_map = Map('start')
game = Engine(start_map)
game.play()
