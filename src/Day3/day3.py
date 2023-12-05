class Solution:
    def __init__(self) -> None:
        self.sol1 = 0
        self.sol2 = 0
        with open("day3.txt") as file:
            self.data = file.read().split("\n")
        self.cache = dict()

    def find_root_and_num(self, i: int, j: int):
        if (i, j) in self.cache:
            return self.cache[(i, j)]

        line = self.data[i]
        if not line[j].isnumeric():
            self.cache[(i, j)] = [-1, -1, 0]
            return self.cache[(i, j)]

        if j - 1 < 0 or not line[j - 1].isnumeric():
            end = j
            while end < len(line) and line[end].isnumeric():
                end += 1
            res = int(line[j:end])
            self.cache[(i, j)] = [i, j, res]
            return self.cache[(i, j)]
        else:
            self.cache[(i, j)] = self.find_root_and_num(i, j - 1)
            return self.find_root_and_num(i, j - 1)

    def valid(self, x: int, y: int) -> bool:
        return x >= 0 and y >= 0 and x < len(self.data) and y < len(self.data)

    def solve_one(self) -> None:
        processed = set()
        for i, line in enumerate(self.data):
            for j, char in enumerate(line):
                if char == "." or char.isnumeric():
                    continue
                for di, dj in [
                    (1, 0),
                    (1, 1),
                    (0, 1),
                    (-1, 0),
                    (-1, 1),
                    (1, -1),
                    (0, -1),
                    (-1, -1),
                ]:
                    x = i + di
                    y = j + dj

                    if not self.valid(x, y):
                        continue

                    loc_r, loc_c, part_num = self.find_root_and_num(x, y)
                    if (loc_r, loc_c) in processed:
                        continue
                    processed.add((loc_r, loc_c))
                    self.sol1 += part_num

    def solve_two(self) -> None:
        for i, line in enumerate(self.data):
            for j, char in enumerate(line):
                if char != "*":
                    continue
                processed = set()
                product = 1
                for di, dj in [
                    (1, 0),
                    (1, 1),
                    (0, 1),
                    (-1, 0),
                    (-1, 1),
                    (1, -1),
                    (0, -1),
                    (-1, -1),
                ]:
                    x = i + di
                    y = j + dj

                    if not self.valid(x, y):
                        continue

                    loc_r, loc_c, part_num = self.find_root_and_num(x, y)
                    if (loc_r, loc_c) in processed or loc_r == -1:
                        continue
                    processed.add((loc_r, loc_c))
                    product *= part_num

                    if len(processed) > 2:
                        break
                if len(processed) == 2:
                    self.sol2 += product

    def get_sol(self) -> None:
        print(f"Solutions\na {self.sol1}\nb {self.sol2}")


solution = Solution()
solution.solve_one()
solution.solve_two()
solution.get_sol()
