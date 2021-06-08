from typing import List


class Allergies:

    _allergens: List[str] = [
        "eggs",
        "peanuts",
        "shellfish",
        "strawberries",
        "tomatoes",
        "chocolate",
        "pollen",
        "cats",
    ]

    def __init__(self, score: int):
        self._score: int = score

    def allergic_to(self, item: str) -> bool:
        return item in self.lst

    def _lst_with_zip(self) -> List[str]:
        """
        This calculates the allergens Tom is allergic to by converting the score, which is limited with a modulu of
        2^(number of allergens), into the a bit string representation.

        The bits are reversed and zipped with the allergens lists and only those matching with a 1 bit are taken into
        consideration.

        Not the most mathy solution, but the one my brain came up with when I realized this is some sort of number to
        bit representation exercise.
        """

        score_mod = self._score % (2**len(self._allergens))
        score_bits = reversed(f"{score_mod:b}")

        return list(allergen for bit, allergen in zip(score_bits, self._allergens) if int(bit))

    def _lst_bitops(self) -> List[str]:
        """
        This calculates the allergens Tom is allergic to by converting shifting the score bit for bit and looking if
        the first bit is set after the shifting.

        I came up with this solution after searching for a more mathy way of converting an int to a binary number.

        Instead of `& 1` it is also possible to use `% 2`, since this would return 1 when the shifted number is odd,
        and thus the first bit would be set.
        """

        return [self._allergens[i] for i in range(len(self._allergens)) if self._score >> i & 1]

    def _lst_bitops_improved(self) -> List[str]:
        """
        This basically does the same thing like `_lst_bitops()`, but instead of shifting the score for the length of
        the allergens list, it only considers the number of bits in the modulu score.

        IDK if this really improves anything (have not benchmarked), but I did not like the fact that the other bitops
        solution just blindly does unecessary shifts (which are probably not that expensive).
        """

        score_mod = self._score % (2**len(self._allergens))

        return [self._allergens[i] for i in range(len(bin(score_mod)[2:])) if score_mod >> i & 1]

    @property
    def lst(self) -> List[str]:
        # return self._lst_with_zip()
        # return self._lst_bitops()
        return self._lst_bitops_improved()
