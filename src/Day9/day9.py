from collections import deque
from typing import List


class Solution:
    def __init__(self) -> None:
        self.sol1 = 0
        self.sol2 = 0
        with open("day9.txt") as file:
            self.data = file.read().split("\n")

    def solve_line(self, seq: List[int]) -> int:
        res = seq[-1]
        differences = deque(seq)
        level = 0
        while level < 1000:
            for _ in range(len(differences) - 1):
                element = differences.popleft()
                differences.append(differences[0] - element)
            differences.popleft()
            res += differences[-1]
            if len(set(differences)) == 1:
                return res
            level += 1
        return -1

    def solve_one(self) -> None:
        for line in self.data:
            self.sol1 += self.solve_line([int(val) for val in line.split()])

    def solve_two(self) -> None:
        for line in self.data:
            self.sol2 += self.solve_line([int(val) for val in line.split()][::-1])

    def get_sol(self) -> None:
        print(f"Solutions\na {self.sol1}\nb {self.sol2}")


solution = Solution()
solution.solve_one()
solution.solve_two()
solution.get_sol()
