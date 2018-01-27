MAX_FRAME = 10


class Frame(object):
    def __init__(self, idx):
        self.idx = idx
        self.throws = []
        self.fill_balls = []
        self.next_frame = None
        self.frame_after_next = None

    @property
    def total_pins(self):
        return sum(self.throws)

    def is_strike(self):
        return self.throws and self.throws[0] == 10

    def is_spare(self):
        return self.throws and self.throws[0] < 10 and self.total_pins == 10

    def is_open(self):
        return len(self.throws) == 2 and self.total_pins < 10

    def is_closed(self):
        """Return if a frame is over."""
        if self.total_pins < 10:
            return len(self.throws) == 2
        elif self.idx < MAX_FRAME - 1:
            # A strike or spare not in the last
            return True
        elif self.is_spare():  # Tenth frame that is spare
            return len(self.fill_balls) == 1
        elif self.is_strike():  # Tenth frame that is strike
            return len(self.fill_balls) == 2

    def throw_bonus(self, pins):
        """Throw a bonus in the tenth frame."""
        self.fill_balls.append(pins)

        # Check against invalid fill balls, e.g. [3, 10]
        if (len(self.fill_balls) == 2 and
            self.fill_balls[0] != 10 and
            sum(self.fill_balls) > 10):
            raise ValueError("invalid fill balls")

        # Check if there are more bonuses than it should be
        if self.is_strike() and len(self.fill_balls) > 2:
            raise ValueError(
                "wrong number of fill balls when the tenth frame is a strike")
        elif self.is_spare() and len(self.fill_balls) > 1:
            raise ValueError(
                "wrong number of fill balls when the tenth frame is a spare")

    def throw(self, pins):
        if not 0 <= pins <= 10:
            raise ValueError("invalid pins")

        if self.idx == MAX_FRAME - 1:
            if self.is_closed():
                raise IndexError(
                    "cannot throw bonus with a open tenth frame")
            if self.is_strike() or self.is_spare():
                self.throw_bonus(pins)
            else:
                self.throws.append(pins)
        else:
            self.throws.append(pins)
            if self.total_pins > 10:
                raise ValueError("cannot roll more than 10 pins in a frame")

    def score(self):
        if self.is_open():
            score = self.total_pins
        elif self.is_spare():
            if self.next_frame is not None:
                score = self.total_pins + self.next_frame.throws[0]
            else:
                # The spare is the tenth frame
                score = self.total_pins + self.fill_balls[0]
        else:  # It's a strike
            if self.next_frame is None:
                # The strike is the tenth frame
                score = 10 + sum(self.fill_balls)
            elif not self.next_frame.is_strike():
                # A not-the-last strike, followed by a non-strike
                score = 10 + self.next_frame.total_pins
            elif self.frame_after_next is None:
                # The strike is the ninth frame, followed by a strike
                score = 20 + self.next_frame.fill_balls[0]
            else:
                # The strike is a frame with idx < 8, followed by a strike
                score = 20 + self.frame_after_next.throws[0]

        return score


class BowlingGame(object):
    def __init__(self):
        self.current_frame_idx = 0
        self.frames = [Frame(idx) for idx in range(MAX_FRAME)]

        # Init next_frame and frame_after_next attributes in each frame
        for idx, frame in enumerate(self.frames):
            frame.next_frame = self.frames[idx+1] if idx < MAX_FRAME - 1 else None
            frame.frame_after_next = self.frames[idx+2] if idx < MAX_FRAME - 2 else None

    @property
    def current_frame(self):
        return self.frames[self.current_frame_idx]

    def roll(self, pins):
        if self.current_frame.is_closed():
            self.current_frame_idx += 1

        self.current_frame.throw(pins)

    def score(self):
        if self.current_frame_idx < MAX_FRAME - 1:
            raise IndexError("frame less than 10")

        if not self.frames[-1].is_closed():
            raise IndexError("bonus must be rolled")

        return sum(frame.score() for frame in self.frames)
