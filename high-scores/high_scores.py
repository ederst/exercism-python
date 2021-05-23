def latest(scores: list[int]) -> int:
    return scores[-1]


def personal_best(scores: list[int]) -> int:
    return max(scores)


def personal_top_three(scores: list[int]) -> list[int]:
    return sorted(scores, reverse=True)[:3]


def personal_top_three_slice_magic(scores: list[int]) -> list[int]:
    """
    This uses step -1 and a negative index instead of reverse sorting the list.
    """

    return sorted(scores)[:-4:-1]
