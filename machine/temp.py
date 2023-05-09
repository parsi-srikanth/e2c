from typing import Literal


def accepts_only_four(x: Literal[4]) -> None:
    pass


accepts_only_four(4)   # OK