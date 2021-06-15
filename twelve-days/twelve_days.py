from typing import List

ordinals: List[str] = [
    "nought",
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

gifts: List[str] = [
    "",
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

verses = list(zip(ordinals, gifts))


def require_valid_verse_range(func):
    def require_valid_verse_range_func(start_verse: int, end_verse: int):
        len_gifts = len(gifts)

        assert end_verse >= start_verse, "End verse must be greater than or equal to start verse."
        assert (
            1 <= end_verse <= len_gifts and 1 <= start_verse <= len_gifts
        ), f"Start and end verse must be a number between 1 and {len_gifts}"

        return func(start_verse, end_verse)

    return require_valid_verse_range_func


@require_valid_verse_range
def recite(start_verse: int, end_verse: int) -> List[str]:
    return [
        f"On the {ordinal[0]} day of Christmas my true love gave to me: {' '.join(gift for _, gift in verses[i+start_verse:0:-1])}."
        for i, ordinal in enumerate(verses[start_verse:end_verse+1])
    ]
