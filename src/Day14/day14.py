from typing import List, Tuple

# todo: refactor and clean code, use tuples in do_cycle, use set instead of dict


class Solution:
    def __init__(self) -> None:
        self.sol1 = 0
        self.sol2 = 0
        with open("day14.txt") as file:
            self.data = file.read().split("\n")

    def score(self, grid: List[List[int]]) -> int:
        return sum(
            row.count("O") * (len(grid) - row_number)
            for row_number, row in enumerate(grid)
        )

    def do_north(self, grid: List[List[int]]) -> List[List[int]]:
        temp = list(map("".join, zip(*grid)))
        temp = [
            "#".join(["".join(sorted(group, reverse=True)) for group in row.split("#")])
            for row in temp
        ]
        return list(map("".join, zip(*temp)))

    def do_cycle(self, grid: List[List[int]]) -> List[List[int]]:
        temp = grid
        for _ in range(4):
            temp = list(map("".join, zip(*temp)))
            temp = [
                "#".join(
                    ["".join(sorted(group, reverse=True)) for group in row.split("#")]
                )
                for row in temp
            ]
            temp = [r[::-1] for r in temp]
        return temp

    def solve_1(self) -> None:
        self.sol1 = self.score(self.do_north(self.data))

    def solve_2(self) -> None:
        seen = {tuple(self.data): 0}
        seen_grids = [self.data]
        grid = self.data
        mod = -1
        first_seen = -1
        for i in range(10**9):
            grid = self.do_cycle(grid)
            tuple_grid = tuple(grid)
            if tuple_grid in seen:
                first_seen = seen[tuple_grid]
                mod = i - first_seen
                break
            seen[tuple_grid] = i
            seen_grids.append(grid)

        if mod != -1:
            final_grid = seen_grids[(10**9 - first_seen) % mod + first_seen]
            self.sol2 = self.score(final_grid)
        else:
            self.sol2 = self.score(grid)

    def get_sol(self) -> None:
        print(f"Solutions\na {self.sol1}\nb {self.sol2}")


solution = Solution()
solution.solve_1()
solution.solve_2()
solution.get_sol()
