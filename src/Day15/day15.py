from collections import defaultdict

class Solution:
    def __init__(self) -> None:
        self.sol1 = 0
        self.sol2 = 0
        with open("day15.txt") as file:
            self.data = file.read().split(",")

    def hash(self, word: str) -> int:
        val = 0
        for char in word:
            val += ord(char)
            val *= 17
            val %= 256
        return val

    def solve_1(self) -> None:
        for word in self.data:
            self.sol1 += self.hash(word)

    def solve_2(self) -> None:
        boxes = defaultdict(list)
        for word in self.data:
            if word[-1] == "-":
                label = word[:-1]
                box_number = self.hash(label)
                box = boxes[box_number]
                box = [(item, power) for item, power in box if item != label]
                boxes[box_number] = box
                continue

            label, power = word.split("=")
            box_number = self.hash(label)
            box = boxes[box_number]
            doAdd = True
            for index, item in enumerate(box):
                if item[0] == label:
                    box[index] = (label, int(power))
                    doAdd = False
            if doAdd:
                box.append((label, int(power)))

        for box_number, box in boxes.items():
            self.sol2 += (box_number + 1) * sum(
                [(index + 1) * item[1] for index, item in enumerate(box)]
            )

    def get_sol(self) -> None:
        print(f"Solutions\na {self.sol1}\nb {self.sol2}")


solution = Solution()
solution.solve_1()
solution.solve_2()
solution.get_sol()
