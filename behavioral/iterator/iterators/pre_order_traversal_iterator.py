from __future__ import annotations
from collections.abc import Iterator
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from behavioral.iterator.node import Node


class PreOrderTraversalIterator(Iterator):
    """
    Concrete Iterators implement various traversal algorithms. These classes
    store the current traversal position at all times.
    """

    """
    `current` attribute stores the current traversal position.
    """
    current: Node = None

    def __init__(self, root: Node):
        self.root = self.current = root
        self.yielded_start = False

    def __next__(self):
        if not self.yielded_start:
            self.yielded_start = True
            return self.current

        if self.current.left:
            self.current = self.current.left
            return self.current
        elif self.current.right:
            if self.current.left:
                self.current = self.current.left
            elif self.current.right:
                self.current = self.current.right
            return self.current

        else:
            p = self.current.parent
            while p == self.root:
                if p and self.current.left == p.left:
                    self.current = p
                elif p and self.current.right == p.right:
                    self.current = p
                else:

            raise StopIteration
