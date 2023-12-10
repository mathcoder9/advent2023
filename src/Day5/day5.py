from typing import List, Tuple


class Solution:
    def __init__(self) -> None:
        self.sol1 = float("inf")
        self.sol2 = 0
        with open("day5.txt") as file:
            self.seed_data, conversion_data = file.read().split("\n\n", 1)
        self.conversions = [
            [
                [int(val) for val in item.split(" ")]
                for item in mapping_data.split("\n")[1:]
            ]
            for mapping_data in conversion_data.split("\n\n")
        ]

    def get_seeds(self) -> List[Tuple[int, int]]:
        return list(map(int, self.seed_data.split(" ")[1:]))

    def solve_one(self) -> None:
        seeds = self.get_seeds()
        for seed in seeds:
            for conversion_data in self.conversions:
                for target, start, size in conversion_data:
                    if seed >= start and seed < start + size:
                        seed += target - start
                        break
            self.sol1 = min(seed, self.sol1)

    # tuple represents seed intervals as [start, end)
    def get_seed_ranges(self) -> List[Tuple[int, int]]:
        seeds = self.get_seeds()
        seed_ranges = [
            (seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)
        ]
        return seed_ranges

    def apply_conversion(
        self,
        seed_ranges: List[Tuple[int, int]],
        conversion_data: List[Tuple[int, int, int]],
    ) -> List[Tuple[int, int]]:
        processed_ranges = []
        for target, start, size in conversion_data:
            new_ranges = []
            conversion_start = start
            conversion_end = start + size
            while seed_ranges:
                range_start, range_end = seed_ranges.pop()

                overlap_start = max(range_start, conversion_start)
                overlap_end = min(range_end, conversion_end)

                if overlap_start < overlap_end:
                    processed_ranges.append(
                        (overlap_start + target - start, overlap_end + target - start)
                    )
                    if range_end > overlap_end:
                        new_ranges.append((overlap_end, range_end))
                    if range_start < overlap_start:
                        new_ranges.append((range_start, overlap_start))
                else:
                    new_ranges.append((range_start, range_end))
            seed_ranges = new_ranges

        return seed_ranges + processed_ranges

    def solve_two(self) -> None:
        seed_ranges = self.get_seed_ranges()
        for conversion_data in self.conversions:
            seed_ranges = self.apply_conversion(seed_ranges, conversion_data)

        self.sol2 = min(seed_ranges, key=lambda x: x[0])[0]

    def get_sol(self) -> None:
        print(f"Solutions\na {self.sol1}\nb {self.sol2}")


solution = Solution()
solution.solve_one()
solution.solve_two()
solution.get_sol()
