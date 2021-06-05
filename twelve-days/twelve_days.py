ordinals = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
]

gifts = [
    "a Partridge in a Pear Tree",
    "two Turtle Doves, and",
    "three French Hens,",
    "four Calling Birds,",
    "five Gold Rings,",
    "six Geese-a-Laying,",
    "seven Swans-a-Swimming,",
    "eight Maids-a-Milking,",
    "nine Ladies Dancing,",
    "ten Lords-a-Leaping,",
    "eleven Pipers Piping,",
    "twelve Drummers Drumming,",
]


def recite(start_verse, end_verse):
    return [
        f"On the {ordinal} day of Christmas my true love gave to me: {' '.join(gifts[ordinals.index(ordinal)::-1])}."
        for ordinal in ordinals[start_verse - 1:end_verse]
    ]
