#!/usr/bin/python
"""This module provides methods for parsing comments from C family languages.
Works with:
  C99+
  C++
  Objective-C
  Java
"""

import re, inspect
from bisect import bisect_left
# from comment_parser.parsers import common


def get_pattern(type):
    # patterns = {
    #     "rs": r"""
    #             (?P<literal> (\"([^\"\n])*\")+) |
    #             (?P<single> //(?P<single_content>.*)?$) |
    #             (?P<multi> /\*(?P<multi_content>(.|\n)*?)?\*/) |
    #             (?P<error> /\*(.*)?)
    #             """,
    #     "py": r"""
    #             (?P<single> \#(?P<single_content>.*)?$) |
    #             (?P<multi> '''(?P<multi_content>(.|\n)*?)?''') |
    #             (?P<error> /\*(.*)?)
    #             """,
    # }

    patterns = {
        "rs": r"""
                (?P<multi> /\*(?P<multi_content>(.|\n)*?)?\*/) |
                (?P<error> /\*(.*)?)
                """,
        "py": r"""
                (?P<single> \#(?P<single_content>.*)?$) |
                (?P<multi> '''(?P<multi_content>(.|\n)*?)?''') |
                (?P<error> /\*(.*)?)
                """,
    }

    return patterns[type]


def extract_comments(code, type):
    """Extracts a list of comments from the given C family source code.
    Comments are represented with the Comment class found in the common module.
    C family comments come in two forms, single and multi-line comments.
      - Single-line comments begin with '//' and continue to the end of line.
      - Multi-line comments begin with '/*' and end with '*/' and can span
        multiple lines of code. If a multi-line comment does not terminate
        before EOF is reached, then an exception is raised.
    Note that this doesn't take language-specific preprocessor directives into
    consideration.
    Args:
      code: String containing code to extract comments from.
    Returns:
      Python list of common.Comment in the order that they appear in the code.
    Raises:
      common.UnterminatedCommentError: Encountered an unterminated multi-line
        comment.
    """

    pattern = get_pattern(type)

    compiled = re.compile(pattern, re.VERBOSE | re.MULTILINE)

    lines_indexes = []
    for match in re.finditer(r"$", code, re.M):
        lines_indexes.append(match.start())

    comments = []
    for match in compiled.finditer(code):
        kind = match.lastgroup

        start_character = match.start()
        line_no = bisect_left(lines_indexes, start_character)

        if kind == "single":
            comment_content = match.group("single_content")
        elif kind == "multi":
            comment_content = match.group("multi_content").replace(" *", "")
        elif kind == "error":
            raise ValueError("comment not terminated")

        print(line_no, inspect.cleandoc(comment_content))


    return comments


file_names = [
    r".hack/test/test.rs",
    r".hack/test/test.py",
]

for file_name in file_names:
    with open(file_name) as f:
        type = file_name.split(".")[-1]
        extract_comments(f.read(), type)
