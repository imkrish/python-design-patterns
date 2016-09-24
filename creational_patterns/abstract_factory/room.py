from abc import ABCMeta
from creational_patterns.abstract_factory.door import Door
from creational_patterns.abstract_factory.wall import Wall


class Room(metaclass=ABCMeta):

    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 4

    def __init__(self):
        self.sides = {}
        print('Room\'s been created.')

    def set_side(self, side, wall_or_door):
        assert isinstance(wall_or_door, Wall) or isinstance(wall_or_door, Door)
        if side == Room.NORTH:
            self.sides[Room.NORTH] = wall_or_door
        elif side == Room.EAST:
            self.sides[Room.EAST] = wall_or_door
        elif side == Room.SOUTH:
            self.sides[Room.SOUTH] = wall_or_door
        elif side == Room.WEST:
            self.sides[Room.WEST] = wall_or_door
        else:
            raise ValueError('Value for side is invalid.')