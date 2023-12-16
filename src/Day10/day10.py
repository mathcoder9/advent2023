from typing import List, Set, Tuple


class Solution:
    def __init__(self) -> None:
        self.sol1 = 0
        self.sol2 = 0
        with open("day10.txt") as file:
            self.maze = file.read().split("\n")
        self.initMapping()
        self.get_s_coords()

    def initMapping(self) -> None:
        self.mapping = dict()
        self.mapping["-"] = {(0, 1): (0, 1), (0, -1): (0, -1)}
        self.mapping["|"] = {(1, 0): (1, 0), (-1, 0): (-1, 0)}
        self.mapping["F"] = {(0, -1): (1, 0), (-1, 0): (0, 1)}
        self.mapping["J"] = {(0, 1): (-1, 0), (1, 0): (0, -1)}
        self.mapping["7"] = {(0, 1): (1, 0), (-1, 0): (0, -1)}
        self.mapping["L"] = {(1, 0): (0, 1), (0, -1): (-1, 0)}
        self.mapping["."] = {}

    def get_dimensions(self) -> Tuple[int, int]:
        return len(self.maze), len(self.maze[0])

    def get_s_coords(self) -> None:
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                if self.maze[i][j] == "S":
                    self.s_x = i
                    self.s_y = j
                    return

    def is_in_bounds(self, a: int, b: int) -> bool:
        return 0 <= a < len(self.maze) and 0 <= b < len(self.maze[0])

    def get_start_and_end(self) -> List[Tuple[int, int, int, int]]:
        if self.s_x < 0 or self.s_y < 0:
            return None, None
        res = []
        dir_set = set()
        for dir_x, dir_y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x = self.s_x + dir_x
            new_y = self.s_y + dir_y
            if not self.is_in_bounds(new_x, new_y):
                continue

            if (dir_x, dir_y) in self.mapping[self.maze[new_x][new_y]]:
                res.append((new_x, new_y, dir_x, dir_y))
                dir_set.add((dir_x, dir_y))

        # update S for part 2
        for char, item in self.mapping.items():
            char_dir_set = set(item.values())
            if len(dir_set.intersection(char_dir_set)) == 2:
                self.maze[self.s_x] = (
                    self.maze[self.s_x][: self.s_y]
                    + char
                    + self.maze[self.s_x][self.s_y + 1 :]
                )
                break
        return res

    def solve(self) -> int:
        start, end = self.get_start_and_end()

        if not start or not end:
            return -1

        start_x, start_y, d_start_x, d_start_y = start
        end_x, end_y, d_end_x, d_end_y = end
        seen = set()
        seen.add((self.s_x, self.s_y))
        while True:
            seen.add((start_x, start_y))
            seen.add((end_x, end_y))
            d_start_x, d_start_y = self.mapping[self.maze[start_x][start_y]][
                (d_start_x, d_start_y)
            ]
            start_x += d_start_x
            start_y += d_start_y

            d_end_x, d_end_y = self.mapping[self.maze[end_x][end_y]][(d_end_x, d_end_y)]
            end_x += d_end_x
            end_y += d_end_y

            if (
                (start_x, start_y) in seen
                or (end_x, end_y) in seen
                or start_x == end_x
                and start_y == end_y
            ):
                break

        seen.add((start_x, start_y))
        seen.add((end_x, end_y))
        self.sol1 = len(seen) // 2

        self.solve_two(seen)

    def solve_two(self, seen: Set[Tuple[int, int]]) -> None:
        for x in range(len(self.maze)):
            is_valid = False
            for y in range(len(self.maze[0])):
                if (x, y) in seen:
                    if self.maze[x][y] in "|JL":
                        is_valid = not is_valid
                else:
                    self.sol2 += is_valid

    def get_sol(self) -> None:
        print(f"Solutions\na {self.sol1}\nb {self.sol2}")


solution = Solution()
solution.solve()
solution.get_sol()
