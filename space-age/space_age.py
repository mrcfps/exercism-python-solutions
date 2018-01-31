class SpaceAge(object):

    SECONDS_IN_A_YEAR = 365.25 * 24 * 60 * 60
    PERIOD_RATIO = {
        'mercury': 0.2408467,
        'venus': 0.61519726,
        'mars': 1.8808158,
        'jupiter': 11.862615,
        'saturn': 29.447498,
        'uranus': 84.016846,
        'neptune': 164.79132,
    }

    def __init__(self, seconds):
        self.seconds = seconds

    @property
    def earth_years(self):
        return self.seconds / self.SECONDS_IN_A_YEAR

    def on_earth(self):
        return round(self.earth_years, 2)

    def on_mercury(self):
        return round(self.earth_years / self.PERIOD_RATIO['mercury'], 2)

    def on_venus(self):
        return round(self.earth_years / self.PERIOD_RATIO['venus'], 2)

    def on_mars(self):
        return round(self.earth_years / self.PERIOD_RATIO['mars'], 2)

    def on_jupiter(self):
        return round(self.earth_years / self.PERIOD_RATIO['jupiter'], 2)

    def on_saturn(self):
        return round(self.earth_years / self.PERIOD_RATIO['saturn'], 2)

    def on_uranus(self):
        return round(self.earth_years / self.PERIOD_RATIO['uranus'], 2)

    def on_neptune(self):
        return round(self.earth_years / self.PERIOD_RATIO['neptune'], 2)
