def distance(strand_a: str, strand_b: str) -> int:
    if len(strand_a) != len(strand_b):
        raise ValueError("Invalid input.")

    return sum(x != y for x, y in zip(strand_a, strand_b))
