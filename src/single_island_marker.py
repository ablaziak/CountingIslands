from abc import ABC, abstractmethod
from typing import List


class SingleIslandMarker(ABC):
    """
    An abstract base class that provides the interface for marking a single island in a 2D grid.

    Methods:
    --------
    mark_single_island(grid: List[List[int]], i: int, j: int) -> List[List[bool]]
        Marks the single island that contains the cell (i, j) in the given 2D grid.
    """
    @classmethod
    @abstractmethod
    def mark_single_island(cls, grid: List[List[int]], i: int, j: int) -> List[List[int]]:
        """
        Marks the single island that contains the cell (i, j) in the given 2D grid.

        Parameters:
        -----------
        grid: List[List[int]]
            A 2D grid of integers representing the land (1) and water (0).
        i: int
            The row index of the cell to start marking from.
        j: int
            The column index of the cell to start marking from.

        Returns:
        --------
        List[List[int]]: The grid with the marked island. Each cell in the marked island
            should be marked as -1, and all other cells should be marked as 0 or 1.

        Raises:
        -------
        NotImplementedError
            If the method is not implemented in a subclass.
        """
        raise NotImplementedError()


class BfsSingleIslandMarker(SingleIslandMarker):
    """
    A class that marks a single island in a 2D grid using BFS.

    Methods:
    --------
    mark_single_island(grid: List[List[int]], i: int, j: int) -> List[List[int]]
        Marks the single island that contains the cell (i, j) in the given 2D grid using BFS.
    """

    @staticmethod
    def __is_safe(grid: List[List[int]], x: int, y: int) -> bool:
        """
        Checks if the cell (x, y) is a valid land cell in the given grid.

        Parameters:
        -----------
        grid: List[List[int]]
            A 2D grid of integers representing the land (1) and water (0).
        x: int
            The row index of the cell to check.
        y: int
            The column index of the cell to check.

        Returns:
        --------
        bool
            True if the cell is a valid land cell, False otherwise.
        """
        return (0 <= x < len(grid)) and (0 <= y < len(grid[0])) and grid[x][y] == 1

    @classmethod
    def mark_single_island(cls, grid: List[List[int]], i: int, j: int) -> List[List[int]]:
        """
        Marks the single island that contains the cell (i, j) in the given 2D grid.

        Parameters:
        -----------
        grid (List[List[int]]):
            The grid to mark the island in.
        i (int):
            The row index of the starting cell.
        j (int):
            The column index of the starting cell.

        Returns:
        --------
            List[List[int]]: The grid with the marked island. Each cell in the marked island
            should be marked as -1, and all other cells should be marked as 0 or 1.
        """
        if grid[i][j] != 1:
            raise ValueError("Value in (i, j) cell is not equal to 1")

        q = [(i, j)]
        grid[i][j] = -1

        possible_moves = (
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        )

        while q:
            x, y = q.pop(0)
            for move in possible_moves:
                new_x = x + move[0]
                new_y = y + move[1]
                if cls.__is_safe(grid, new_x, new_y):
                    grid[new_x][new_y] = -1
                    q.append((new_x, new_y))
        return grid
