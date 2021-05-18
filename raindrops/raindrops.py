def convert(number):
    sound_mapping = {
        "Pling": number % 3,
        "Plang": number % 5,
        "Plong": number % 7,
    }

    return ''.join([k for k, v in sound_mapping.items() if not v]) or str(number)
