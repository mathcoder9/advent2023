from typing import List


class Solution:
    def __init__(self) -> None:
        self.sol1 = 0
        self.sol2 = 0
        with open("day11.txt") as file:
            self.data = file.read().split("\n")

        self.x = []
        self.y = []
        self.init_coord_map()

    def init_coord_map(self) -> None:
        for i, line in enumerate(self.data):
            for j, char in enumerate(line):
                if char == "#":
                    self.x.append(j)
                    self.y.append(i)
        self.x.sort()
        self.y.sort()

    def expand_coords(self, positions: List[int], expansion_rate: int) -> List[int]:
        prev = -1
        res = [-1]
        for position in positions:
            if position == prev:
                res.append(res[-1])
            elif position == prev + 1:
                res.append(1 + res[-1])
            elif position != prev + 1:
                new_diff = expansion_rate * (position - prev - 1)
                res.append(new_diff + res[-1] + 1)
            prev = position

        return res[1:]

    def solve(self) -> None:
        x_coords = self.expand_coords(self.x, 2)
        y_coords = self.expand_coords(self.y, 2)

        big_x_coords = self.expand_coords(self.x, 10**6)
        big_y_coords = self.expand_coords(self.y, 10**6)

        for i in range(len(x_coords)):
            for j in range(i, len(x_coords)):
                self.sol1 += x_coords[j] - x_coords[i]
                self.sol1 += y_coords[j] - y_coords[i]
                self.sol2 += big_x_coords[j] - big_x_coords[i]
                self.sol2 += big_y_coords[j] - big_y_coords[i]

    def get_sol(self) -> None:
        print(f"Solutions\na {self.sol1}\nb {self.sol2}")


solution = Solution()
solution.solve()
solution.get_sol()
