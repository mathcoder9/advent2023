from typing import Tuple


class Solution:
    def __init__(self) -> None:
        self.sol1 = 0
        self.sol2 = 0
        with open("day2.txt") as file:
            self.data = file.read().split("\n")

    # parses a line and returns ID, max_red, max_green, max_blue
    def parseLine(self, line: str) -> Tuple[int, int, int, int]:
        id_data, game_data = line.split(":")
        game_id = int(id_data.split(" ")[1])
        max_red, max_green, max_blue = 0, 0, 0
        for round_data in game_data.split(";"):
            for colour_data in round_data.split(","):
                _, count, colour = colour_data.split(" ")
                if colour[0] == "r":
                    max_red = max(max_red, int(count))
                elif colour[0] == "g":
                    max_green = max(max_green, int(count))
                elif colour[0] == "b":
                    max_blue = max(max_blue, int(count))
        return game_id, max_red, max_green, max_blue

    def solve(self) -> None:
        for line in self.data:
            game_id, max_red, max_green, max_blue = self.parseLine(line)
            if max_red <= 12 and max_green <= 13 and max_blue <= 14:
                self.sol1 += game_id
            self.sol2 += max_red * max_green * max_blue

    def getSol(self) -> None:
        print(f"Solutions\na {self.sol1}\nb {self.sol2}")


solution = Solution()
solution.solve()
solution.getSol()
