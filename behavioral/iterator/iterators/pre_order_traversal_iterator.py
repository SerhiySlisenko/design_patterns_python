from __future__ import annotations
from collections.abc import Iterator
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from behavioral.iterator.node import Node


class PreOrderTraversalIterator(Iterator):
    """
    Concrete Iterators implement various traversal algorithms. These classes
    store the current traversal position at all times.
    This class contains a complete implementation of Pre-Order Traverse iteration.
    """

    # `_current` attribute stores the current traversal position.
    _current: Node = None

    def __init__(self, root: Node) -> None:
        self.root = self._current = root
        self.yielded_start = False
        self.next_time_exit = False

    def __next__(self) -> Node:
        if not self.yielded_start:
            self.yielded_start = True
            return self._current

        if self._current.left:
            self._current = self._current.left
            return self._current
        elif self._current.right:
            if self._current.left:
                self._current = self._current.left
            elif self._current.right:
                self._current = self._current.right
            return self._current

        else:
            p = self._current.parent
            if p != self.root:
                if self._current == p.left:
                    if p.right:
                        self._current = p.right
                        return self._current

                else:
                    while not p == self.root:
                        p = p.parent
                        if p.right and self._current not in [child for child in p.right if child is not None]:
                            self._current = p.right
                            return self._current

                    if not self.next_time_exit:
                        self.next_time_exit = True

                        if p.right:
                            self._current = p.right
                            return self._current

            raise StopIteration
