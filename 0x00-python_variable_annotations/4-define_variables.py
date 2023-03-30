#!/usr/bin/env python3
"""
Define and annotate variables for specific values
"""


def define_variables(
        a: int = 1,
        pi: float = 3.14,
        i_understand_annotations: bool = True,
        school: str = "Holberton"):
    """
    Define and annotate variables for specific values
    """
    return a, pi, i_understand_annotations, school


a, pi, i_understand_annotations, school = define_variables()
