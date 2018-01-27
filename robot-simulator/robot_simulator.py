# Globals for the bearings
# Change the values as you see fit
EAST, NORTH, WEST, SOUTH = range(4)


class Robot(object):
    _moves = {
        EAST: (1, 0),
        WEST: (-1, 0),
        NORTH: (0, 1),
        SOUTH: (0, -1),
    }

    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.x, self.y = x, y

    @property
    def coordinates(self):
        return self.x, self.y

    def turn_left(self):
        self.bearing = (self.bearing + 1) % 4

    def turn_right(self):
        self.bearing = (self.bearing - 1) % 4

    def advance(self):
        delta_x, delta_y = self._moves[self.bearing]
        self.x += delta_x
        self.y += delta_y

    def simulate(self, instructions):
        for instruction in instructions:
            if instruction == 'L':
                self.turn_left()
            elif instruction == 'R':
                self.turn_right()
            elif instruction == 'A':
                self.advance()
            else:
                raise ValueError("invalid instruction")
