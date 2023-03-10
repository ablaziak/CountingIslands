from typing import List


class InputReader:
    """
    A class used to read an input and convert it into a 2D list of integers.

    Methods:
    --------
        read_input() -> List[List[int]] : Read input from stdin
        and returns the 2D list of integers.

    Example:
    --------
        input_reader = InputReader()
        grid = input_reader.read_input()
    """
    @staticmethod
    def read_input() -> List[List[int]]:
        """
        Read input from stdin and returns the 2D list of integers.

        Returns:
        --------
            List[List[int]]: A 2D list of integers read from the stdin.
        """
        m, _ = tuple(map(int, input().split()))
        grid = [list(map(int, input().split())) for _ in range(m)]
        return grid
