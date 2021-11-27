from typing import List


class Verifier:
    """
    This class takes a 2D list and verifies that the sum of elements in every sublist is the same.
    """
    @staticmethod
    def verify(arrays: List[List[int]]) -> bool:
        first = sum(arrays[0])

        for i in range(1, len(arrays)):
            if sum(arrays[i]) != first:
                return False

        return True
