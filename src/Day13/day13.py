from typing import Dict, List, Tuple


class Solution:
    def __init__(self) -> None:
        self.sol1 = 0
        self.sol2 = 0
        with open("day13.txt") as file:
            self.data = file.read().split("\n\n")

    def get_map(self, grid: List[str]) -> Tuple[Dict[int, int], Dict[int, int]]:
        horizontal_map = dict()
        vertical_map = dict()

        for i, line in enumerate(grid):
            val = 0
            for char in line:
                val <<= 1
                val += 1 if char == "#" else 0
            horizontal_map[i] = val

        for j in range(len(grid[0])):
            val = 0
            for i in range(len(grid)):
                val <<= 1
                val += 1 if grid[i][j] == "#" else 0
            vertical_map[j] = val

        return horizontal_map, vertical_map

    def score_map(self, map: Dict[int, int]) -> Tuple[int, int]:
        res = 0
        smudge_res = 0
        for i in range(len(map) - 1):
            l = i
            r = i + 1
            skip = False
            smudge = 0
            while l >= 0 and r < len(map):
                if map[l] != map[r]:
                    skip = True
                    if smudge == 1:
                        smudge += 1
                        break
                    xor = map[l] ^ map[r]
                    if xor & (xor - 1) != 0:
                        break
                    smudge += 1
                l -= 1
                r += 1
            if not skip:
                res += i + 1
            if smudge == 1:
                smudge_res += i + 1
        return res, smudge_res

    def solve(self) -> None:
        for grid in self.data:
            parsed_grid = grid.split()
            h_map, v_map = self.get_map(parsed_grid)

            h_score, smudge_h_score = self.score_map(h_map)
            v_score, smudge_v_score = self.score_map(v_map)
            self.sol1 += 100 * h_score
            self.sol1 += v_score
            self.sol2 += 100 * smudge_h_score
            self.sol2 += smudge_v_score

    def get_sol(self) -> None:
        print(f"Solutions\na {self.sol1}\nb {self.sol2}")


solution = Solution()
solution.solve()
solution.get_sol()
