from typing import Generator, List


def spring(wall=500, difference=50) -> Generator[List[int], None, None]:
    """
    Generate list of two elements lists with points of spring.
    wall: lenght of the longest (first) wall in pixels
    offset: difference in the length of successive walls

     wall
    ─────┐

    ─────┐   ─┐ difference
    ┌──┐ │   ─┘
    │ ─┘ │
    └────┘
    >>> list(spring()) == \
    [[500, 0], [0, 450], [-400, 0], [0, -350], \
    [300, 0], [0, 250], [-200, 0],  [0, -150], \
    [100, 0], [0, 50], [0, 0]]
    True
    """
    i = 0
    while wall >= 0:
        yield [0, [1, 1, -1, -1][i % 4] * wall][::i % 2 * 2 - 1]
        wall -= difference
        i += 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
