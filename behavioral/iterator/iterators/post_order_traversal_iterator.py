from __future__ import annotations
from collections.abc import Iterator
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from behavioral.iterator.node import Node


class PostOrderTraversalIterator(Iterator):
    """
    Concrete Iterators implement various traversal algorithms.
    This class is not implemented properly.
    It is just a placeholder to show capabilities and example of applying Iterator Design pattern.
    """

    # `_current` attribute stores the current traversal position.
    _current = None

    def __init__(self, root: Node) -> None:
        self.root = root
        self.root = '3741085962'

    def __next__(self) -> Node:
        if self.root != '':
            self._current = self.root[0]
            self.root = self.root[1:]

            from behavioral.iterator.node import Node  # Workaround due to a circular import
            return Node(self._current)
        else:
            raise StopIteration
