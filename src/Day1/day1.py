class Solution:
    def __init__(self) -> None:
        self.sol1 = 0
        self.sol2 = 0
        with open("day1.txt") as file:
            self.data = file.read().split("\n")

    def solve1(self) -> None:
        for line in self.data:
            tens = 10
            digit = 0
            for i in range(len(line)):
                if line[i].isnumeric():
                    tens *= int(line[i])
                    break
            for i in range(len(line)-1, -1, -1):
                if line[i].isnumeric():
                    digit = int(line[i])
                    break
            self.sol1 += tens + digit

    # not the most efficient - could probably do something with tries/string matching algos
    def solve2(self) -> None:
        word_numbers = {3 : {"one", "two", "six"}, 4: {"four", "five", "nine"}, 5:{"three", "seven", "eight"}}
        convertToInt = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
        
        for line in self.data:
            tens = 0
            digit = 0
            for i in range(len(line)):
                if line[i].isnumeric():
                    if tens == 0:
                        tens = 10 * int(line[i])
                    digit = int(line[i])
                    continue

                for j in range(3, 6):
                    if i + j - 1 < len(line):
                        candidate = line[i:i+j]
                        if candidate in word_numbers[j]:
                            num = convertToInt[candidate]
                            if tens == 0:
                                tens = 10 * num
                            digit = num
                            continue

            self.sol2 += tens + digit

    def getSol(self) -> None:
        print(f"Solutions\na {self.sol1}\nb {self.sol2}")

solution = Solution()
solution.solve1()
solution.solve2()
solution.getSol()
