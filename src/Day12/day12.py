from functools import lru_cache
from typing import Tuple


class Solution:
    def __init__(self) -> None:
        self.sol1 = 0
        self.sol2 = 0
        with open("day12.txt") as file:
            self.data = file.read().split("\n")

    def solve_line(self, line: str, multiplier: int = 1) -> int:
        symbols, combo = line.split()
        combo_list = tuple(int(val) for val in combo.split(","))
        symbols = "?".join([symbols] * multiplier)
        combo_list = combo_list * multiplier

        @lru_cache()
        def dp(symbols: str, combo_list: Tuple[int]) -> int:
            symbols = symbols.lstrip(".")
            if symbols == "":
                return int(combo_list == ())
            if combo_list == ():
                return int("#" not in symbols)

            if symbols[0] == "?":
                return dp("#" + symbols[1:], combo_list) + dp(symbols[1:], combo_list)

            length_needed = combo_list[0]
            if len(symbols) < length_needed or "." in symbols[:length_needed]:
                return 0
            elif len(symbols) == combo_list[0]:
                return int(len(combo_list) == 1)
            elif symbols[combo_list[0]] == "#":
                return 0
            else:
                return dp(
                    symbols[combo_list[0] + 1 :], combo_list[1:]
                )  # one less spring

        return dp(symbols, combo_list)

    def solve(self) -> None:
        for line in self.data:
            self.sol1 += self.solve_line(line)
            self.sol2 += self.solve_line(line, 5)

    def get_sol(self) -> None:
        print(f"Solutions\na {self.sol1}\nb {self.sol2}")


solution = Solution()
solution.solve()
solution.get_sol()
