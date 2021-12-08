from __future__ import annotations
from collections.abc import Iterable, Iterator

from iterators import InOrderTraversalIterator, PreOrderTraversalIterator, PostOrderTraversalIterator


class Node(Iterable):
    """

    """
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value

        self.parent = None

        if left:
            self.left.parent = self
        if right:
            self.right.parent = self

    def __iter__(self) -> Iterator:
        """
        The __iter__() method returns the iterator object itself, by default we
        return the in-order traversal iterator.
        """
        return InOrderTraversalIterator(self)

    def get_pre_order_traversal_iterator(self) -> Iterator:
        return PreOrderTraversalIterator(self)

    def get_post_order_traversal_iterator(self) -> Iterator:
        return PostOrderTraversalIterator(self)

    def __str__(self):
        return f"Node({self.value})"