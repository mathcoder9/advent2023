from typing import List, Tuple
from math import sqrt, floor, ceil


class Solution:
    def __init__(self) -> None:
        self.sol1 = 1
        self.sol2 = 0
        with open("day6.txt") as file:
            self.data = file.read()
        self.parse_data()

    # returns list of times and distances
    def parse_data(self) -> Tuple[List[int]]:
        a, b = self.data.split("\n")
        return [int(val) for val in a.split(":")[1].split()], [
            int(val) for val in b.split(":")[1].split()
        ]

    # for a time t ms, the distance travelled if the button is held for x ms (0<=x<=t) is x*(t-x)
    def calculate_ways(self, time, distance) -> int:
        if distance < 0:
            return 0
        if distance == 0:
            return time - 1 if time > 1 else 0

        discriminant = time**2 - 4 * distance
        if discriminant < 0:
            return 0
        if discriminant == 0:
            return 1 if time % 2 == 0 else 0

        lb, ub = ceil((time - sqrt(discriminant) + 0.1) / 2), floor(
            (time + sqrt(discriminant) - 0.1) / 2
        )
        return ub - lb + 1

    def solve_one(self) -> None:
        times, distances = self.parse_data()
        for time, distance in zip(times, distances):
            self.sol1 *= self.calculate_ways(time, distance)

    def solve_two(self) -> None:
        times, distances = self.parse_data()
        actual_time = int("".join(map(str, times)))
        actual_distance = int("".join(map(str, distances)))
        self.sol2 = self.calculate_ways(actual_time, actual_distance)

    def get_sol(self) -> None:
        print(f"Solutions\na {self.sol1}\nb {self.sol2}")


solution = Solution()
solution.solve_one()
solution.solve_two()
solution.get_sol()
