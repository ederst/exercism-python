def distance(strand_a: str, strand_b: str) -> int:
    if len(strand_a) != len(strand_b):
        raise ValueError("Invalid input.")

    distance = 0
    for i, c in enumerate(strand_a):
        if c != strand_b[i]:
            distance += 1
    return distance
