from typing import List

from src.single_island_marker import SingleIslandMarker, BfsSingleIslandMarker


class IslandCounter:
    """
    A class that counts the number of islands in a 2D grid.

    Methods:
    --------
    count_islands(grid: List[List[int]], single_island_marker: SingleIslandMarker) -> int
        Counts the number of islands in the given 2D grid using the specified single island marker.
    """

    @staticmethod
    def count_islands(grid: List[List[int]],
                      single_island_marker: SingleIslandMarker = BfsSingleIslandMarker) -> int:
        """
        Counts the number of islands in the given 2D grid using the specified single island marker.

        Parameters:
        -----------
        grid: List[List[int]]
            A 2D grid of integers representing the land (1) and water (0).
        single_island_marker: SingleIslandMarker, optional (default=BfsSingleIslandMarker)
            An object that implements the SingleIslandMarker interface to mark a single island.

        Returns:
        --------
        int
            The number of islands in the given 2D grid.
        """
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])

        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid = single_island_marker.mark_single_island(grid, i, j)
                    result += 1
        return result
