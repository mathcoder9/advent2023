from collections import Counter


class Solution:
    def __init__(self) -> None:
        self.sol1 = 0
        self.sol2 = 0
        with open("day7.txt") as file:
            self.data = file.read()
        self.conv_dict = dict()
        self.init_conv_dict()

    def init_conv_dict(self) -> None:
        self.conv_dict["A"] = 14
        self.conv_dict["K"] = 13
        self.conv_dict["Q"] = 12
        self.conv_dict["J"] = 11
        self.conv_dict["T"] = 10
        for i in range(2, 10):
            self.conv_dict[str(i)] = i

    # score card values only
    def score_cards(self, hand: str, joker: bool) -> int:
        score = 0
        for val in hand:
            score *= 100
            if val == "J" and joker:
                score += 1
                continue
            score += self.conv_dict[val]
        return score

    # score hand combo
    def score_combo(self, hand: str, joker: bool) -> int:
        score = 0
        count = Counter(hand)
        max_cards = 0
        card_count = len(count)
        if joker:
            max_cards = (
                max([val for key, val in count.items() if key != "J"], default=0)
                + count["J"]
            )
            if card_count > 1 and count["J"] > 0:
                card_count -= 1
        else:
            max_cards = max(count.values())

        if card_count == 1:
            score += 10**15
        elif card_count == 2:
            if max_cards == 4:
                score += 10**14
            elif max_cards == 3:
                score += 10**13
        elif card_count == 3:
            if max_cards == 3:
                score += 10**12
            elif max_cards == 2:
                score += 10**11
        elif card_count == 4:
            score += 10**10

        return score

    def score_hand(self, hand: str, joker: bool) -> int:
        return self.score_cards(hand, joker) + self.score_combo(hand, joker)

    def solve(self) -> None:
        hands = []
        for line in self.data.split("\n"):
            hand, val = line.split()
            hands.append((hand, val))

        sorted_list_one = sorted(
            hands,
            key=lambda x: self.score_hand(x[0], False),
        )
        sorted_list_two = sorted(
            hands,
            key=lambda x: self.score_hand(x[0], True),
        )
        for idx in range(len(sorted_list_one)):
            self.sol1 += int(sorted_list_one[idx][1]) * (idx + 1)
            self.sol2 += int(sorted_list_two[idx][1]) * (idx + 1)

    def get_sol(self) -> None:
        print(f"Solutions\na {self.sol1}\nb {self.sol2}")


solution = Solution()
solution.solve()
solution.get_sol()
