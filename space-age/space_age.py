class SpaceAge:

    def __init__(self, seconds: float):
        self.seconds = seconds

    def _space_age(self, ratio: float = 1.0, ndigits: int = 2) -> float:
        return round(self.seconds / 31557600.0 / ratio, ndigits)

    def on_mercury(self) -> float:
        return self._space_age(0.2408467)

    def on_venus(self) -> float:
        return self._space_age(0.61519726)

    def on_earth(self) -> float:
        return self._space_age()

    def on_mars(self) -> float:
        return self._space_age(1.8808158)

    def on_jupiter(self) -> float:
        return self._space_age(11.862615)

    def on_saturn(self) -> float:
        return self._space_age(29.447498)

    def on_uranus(self) -> float:
        return self._space_age(84.016846)

    def on_neptune(self) -> float:
        return self._space_age(164.79132)
