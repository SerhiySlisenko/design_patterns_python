from __future__ import annotations
from collections.abc import Iterator
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from behavioral.iterator.node import Node


class InOrderTraversalIterator(Iterator):
    """
    Concrete Iterators implement various traversal algorithms. These classes
    store the current traversal position at all times.
    This class contains a complete implementation of In-Order Traverse iteration.
    """

    # `_current` attribute stores the current traversal position.
    _current: Node = None

    def __init__(self, root: Node) -> None:
        self.root = self._current = root
        self.yielded_start = False
        while self._current.left:
            self._current = self._current.left

    def __next__(self) -> Node:
        if not self.yielded_start:
            self.yielded_start = True
            return self._current

        if self._current.right:
            self._current = self._current.right
            while self._current.left:
                self._current = self._current.left
            return self._current
        else:
            p = self._current.parent
            while p and self._current == p.right:
                self._current = p
                p = p.parent
            self._current = p
            if self._current:
                return self._current
            else:
                raise StopIteration
