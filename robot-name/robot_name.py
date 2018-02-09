import random
from string import ascii_uppercase


class Robot(object):
    # Keep track of generated names to avoid duplication
    generated_names = []

    def __init__(self):
        self.reset()

    def _generate_random_name(self):
        def generate():
            name = random.choice(ascii_uppercase) \
                + random.choice(ascii_uppercase) \
                + '{:03d}'.format(random.randint(0, 999))
            return name
        name = generate()

        # Keep generating until it's not in the generated list
        while name in Robot.generated_names:
            name = generate()

        Robot.generated_names.append(name)
        return name

    def reset(self):
        self.name = self._generate_random_name()
