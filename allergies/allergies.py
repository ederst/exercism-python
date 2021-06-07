class Allergies:

    _allergies = {
        1: "eggs",
        2: "peanuts",
        4: "shellfish",
        8: "strawberries",
        16: "tomatoes",
        32: "chocolate",
        64: "pollen",
        128: "cats",
    }

    def __init__(self, score):
        self._score = score

    def allergic_to(self, item):
        return item in self.lst

    @property
    def lst(self):
        score = self._score % (sum(self._allergies.keys()) + 1)
        _allergies_list = []
        for k, v in sorted(self._allergies.items(), reverse=True):
            print(score)
            if (k <= score):
                _allergies_list.append(v)
                score -= k
        return _allergies_list
