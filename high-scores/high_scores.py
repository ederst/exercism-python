"""
Solution of 'high-scores' exercise in the 'python' track.

exercism-cd:
    exercise: high-scores
    track: python
    author: ederst
    git-url: https://github.com/ederst/exercism-python.git
    pull-request: https://github.com/ederst/exercism-python/pull/11
    state: draft|submit|submitted|reviewed

:param exercise: high-scores
:param track: python
:param state: draft
"""

import yaml


def latest(scores: list[int]) -> int:
    return scores[-1]


def personal_best(scores: list[int]) -> int:
    return max(scores)


def personal_top_three(scores: list[int]) -> list[int]:
    return sorted(scores, reverse=True)[:3]

