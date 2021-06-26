from typing import List, Dict


class Garden:

    DEFAULT_STUDENTS = [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Eve",
        "Fred",
        "Ginny",
        "Harriet",
        "Ileana",
        "Joseph",
        "Kincaid",
        "Larry",
    ]

    PLANTS = {
        "R": "Radishes",
        "V": "Violets",
        "G": "Grass",
        "C": "Clover",
    }

    DEFAULT_CUPS = 2

    def _resolve_plant_names(self, string: str) -> List[str]:
        return [Garden.PLANTS[c] for c in string]

    def _chunkify(self, string: str, chunk_size) -> List[str]:
        return [string[i:i+chunk_size] for i in range(0, len(string), chunk_size)]

    def __init__(self, diagram: str, students: List[str] = DEFAULT_STUDENTS, cups: int = DEFAULT_CUPS):
        # What the code essentially does:
        #   1. split the `diagram` string into an array on line breaks
        #        -> ['ABCD', 'EFGH']
        #   2. for every line split the string into chunks (of 2 in our case)
        #        -> [['AB', 'CD'], ['EF', 'GH']]
        #   3. unpack the list of lists so that they act as args for the first zip()
        #        -> ['AB', 'CD'] ['EF', 'GH']
        #   4. zip the unpacked values, to pair the nth element of every list
        #        -> ('AB', 'EF') ('CD', 'GH')
        #   5. join the pairings into a string
        #        -> ['ABEF', 'CDGH']
        #   6. resolve each char to its plant name
        #        -> [['A...', 'B...', 'E...', 'F...'], ['C...', 'D...', 'G...', 'H...']]
        #   7. zip it with the sorted student list and make a dict out of it
        #        -> { 'Alice': ['A...', 'B...', 'E...', 'F...'], ... }
        #  Note: The code adapts to changes in rows and number of cups.
        self._plant_ownerships = dict(
            zip(
                sorted(students),
                [
                    self._resolve_plant_names("".join(p))
                    for p in zip(*[self._chunkify(line, cups) for line in diagram.splitlines()])
                ],
            )
        )

    def plants(self, student: str) -> List[str]:
        return self._plant_ownerships[student]
