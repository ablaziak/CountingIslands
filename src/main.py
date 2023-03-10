from src.input_reader import InputReader
from src.island_counter import IslandCounter


def run_app():
    test_grid = InputReader().read_input()
    print(IslandCounter.count_islands(test_grid))


if __name__ == '__main__':
    run_app()
