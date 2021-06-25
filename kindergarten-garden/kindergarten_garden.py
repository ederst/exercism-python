from typing import List, Dict


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


class Garden:
    def _resolve_plants(self, string: str) -> List[str]:
        return [self._plants[c] for c in string]

    def _chunkify(self, string: str, chunk_size=2) -> List[str]:
        return [string[i:i+chunk_size] for i in range(0, len(string), chunk_size)]

    def __init__(self, diagram: str, students: List[str] = DEFAULT_STUDENTS):
        self._plants = {
            "R": "Radishes",
            "V": "Violets",
            "G": "Grass",
            "C": "Clover",
        }

        self._plants_mapping = dict(
            zip(
                sorted(students),
                [
                    self._resolve_plants("".join(p))
                    for p in zip(*[self._chunkify(line) for line in diagram.splitlines()])
                ],
            )
        )

    def plants(self, student: str) -> List[str]:
        return self._plants_mapping[student]
