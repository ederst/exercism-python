SOUND_MAPPING = {
    3: "Pling",
    5: "Plang",
    7: "Plong",
}


def convert(number):
    """
    My original and submitted solution.
    """
    sound_mapping = {
        "Pling": number % 3,
        "Plang": number % 5,
        "Plong": number % 7,
    }

    return "".join([k for k, v in sound_mapping.items() if not v]) or str(number)


def convert_improved_original(number):
    """
    This is an (IMHO) improved version of the original, because it is easier to extend (add number and mapping string
    to dict) and the mapping variable does not have to be part of the function.
    """
    return "".join([v for k, v in SOUND_MAPPING.items() if not number % k]) or str(number)


def convert_with_map_and_filter(number):
    """
    This is just me playing around with map and filter.
    """
    return "".join(map(SOUND_MAPPING.get, filter(lambda x: not number % x, SOUND_MAPPING.keys()))) or str(number)


def convert_with_map_only(number):
    """
    Here I tried to get rid of the filter, which is strictly not necessary.
    """
    return "".join(map(lambda x: x[1] if not number % x[0] else "", SOUND_MAPPING.items())) or str(number)
