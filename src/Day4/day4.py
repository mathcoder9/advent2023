class Solution:
    def __init__(self) -> None:
        self.sol1 = 0
        self.sol2 = 0
        with open("day4.txt") as file:
            self.data = file.read().split("\n")

    def matching_numbers_for_line(self, line: str) -> int:
        winning_section, guess_section = line.split(":")[1].split("|")

        winning_set = set(winning_section.split(" "))
        if winning_set:
            winning_set.discard("")

        guess_set = set(guess_section.split(" "))
        if guess_set:
            guess_set.discard("")

        matches = 0
        if winning_set:
            matches = len(winning_set.intersection(guess_set))

        return matches

    def solve_one(self) -> None:
        for line in self.data:
            matches = self.matching_numbers_for_line(line)
            self.sol1 += 1 << (matches - 1) if matches > 0 else 0

    def solve_two(self) -> None:
        counts = [1 for _ in range(len(self.data))]

        for idx, line in enumerate(self.data):
            matches = self.matching_numbers_for_line(line)
            for i in range(idx + 1, idx + 1 + matches):
                if i >= len(self.data):
                    break
                counts[i] += counts[idx]

        self.sol2 = sum(counts)

    def get_sol(self) -> None:
        print(f"Solutions\na {self.sol1}\nb {self.sol2}")


solution = Solution()
solution.solve_one()
solution.solve_two()
solution.get_sol()
