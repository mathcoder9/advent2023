from collections import defaultdict
from math import gcd
from typing import Generator


class Solution:
    def __init__(self) -> None:
        self.sol1 = 0
        self.sol2 = 0
        with open("day8.txt") as file:
            self.directions, self.graph_data = file.read().split("\n\n")
        self.adjList = defaultdict(list)
        self.init_graph()

    def init_graph(self) -> None:
        for line in self.graph_data.split("\n"):
            origin, neighbours = line.split(" = ")
            self.adjList[origin].append(neighbours[1:4])
            self.adjList[origin].append(neighbours[6:9])

    def get_move(self) -> Generator[int, None, None]:
        while True:
            for char in self.directions:
                if char == "L":
                    yield 0
                else:
                    yield 1

    def solve(self, start: str, match_full: bool) -> None:
        current = start
        moves = 0
        for move in self.get_move():
            moves += 1
            current = self.adjList[current][move]
            if (match_full and current == "ZZZ") or (
                not match_full and current[-1] == "Z"
            ):
                return moves

    def solve_one(self) -> None:
        self.sol1 = self.solve("AAA", True)

    # lucky w input
    def solve_two(self) -> None:
        lcm = 1
        for key in self.adjList:
            if key[-1] != "A":
                continue
            moves = self.solve(key, False)
            lcm = (lcm * moves) // gcd(lcm, moves)
        self.sol2 = lcm

    def get_sol(self) -> None:
        print(f"Solutions\na {self.sol1}\nb {self.sol2}")


solution = Solution()
solution.solve_one()
solution.solve_two()
solution.get_sol()
