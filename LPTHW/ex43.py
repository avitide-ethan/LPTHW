# Define concepts/create class hierarchy
#
# characters
    # aliens
    # hero
#
# location/scene
        # -enter
    # spaceship
    # maze of rooms
    # escape pod
    # planet belw
#
# actions
    # defeat
    # escape
    # death
#
# game engine
#     play
#
# map
#     opening scene
#     next scene

class Scene(object):

    def enter(self):
        pass


class Death(Scene):

    def enter(self):
        pass


class CentralCorridor(Scene):
    pass


class LaserWeaponArmory(Scene):

    def enter(self):
        pass


class TheBridge(Scene):

    def enter(self):
        pass


class EscapePod(Scene):

    def enter(self):
        pass


class Engine(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        pass

    def enter(self):
        input("""You enter the central corridor. Several scary lizards come out at you.
        What do you do?
        1. Duck and hide
        2. Face them with a pitchfork
        3. Nothing
        > """)


class Map(object):

    def __init__(self, start_scene):
        print(f"You initialized an instance of Map class. {start_scene} is the start scene.")

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


# a_map = Map('central_corridor')
# a_game = Engine(a_map)
# # a_game.play()


class Coordinate(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "<" + str(self.x) + ", " + str(self.y) + ">"

    def distance(self, other):
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5


class Fraction(object):

    def __init__(self, num, denom):
        assert type(num) == int
        assert type(denom) == int
        self.num = num
        self.denom = denom

    def __str__(self):
        return str(self.num) + "/" + str(self.denom)

    def __add__(self, other):
        top = self.num * other.denom + self.denom * other.num
        bottom = self.denom * other.denom
        return Fraction(top, bottom)

    def __sub__(self, other):
        top = self.num * other.denom - self.denom * other.num
        bottom = self.denom * other.denom
        return Fraction(top, bottom)

    def __float__(self):
        return self.num/self.denom

    def inverse(self):
        return Fraction(bottom, top)


f1 = Fraction(1, 2)
f2 = Fraction(2, 1)

print(f1 + f2)


c = Coordinate(3, 4)
print(c)
print(type(c))
print(type(Coordinate))
print(isinstance(c, Coordinate))

origin = Coordinate(0,0)
