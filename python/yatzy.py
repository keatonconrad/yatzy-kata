class Yatzy:

    def __init__(self, d1, d2, d3, d4, d5):
        self.dice = list(locals().values())
        self.dice.pop(0)
        self.unique_dice = list(set(self.dice))

    def chance(self):
        return sum(self.dice)

    def yatzy(self):
        if all(d == self.dice[0] for d in self.dice):
            return 50
        return 0

    def ones(self):
        return sum(1 for d in self.dice if d == 1)

    def twos(self):
        return sum(2 for d in self.dice if d == 2)

    def threes(self):
        return sum(3 for d in self.dice if d == 3)

    def fours(self):
        return sum(4 for d in self.dice if d == 4)

    def fives(self):
        return sum(5 for d in self.dice if d == 5)

    def sixes(self):
        return sum(6 for d in self.dice if d == 6)

    def pair(self):
        dice_with_pairs = [d for d in self.unique_dice if self.dice.count(d) >= 2]
        if len(self.unique_dice) <= 4 and len(dice_with_pairs) >= 1:
            return sum(d * 2 for d in self.unique_dice
                       if self.dice.count(d) >= 2 and
                       d == max(dice_with_pairs))
        return 0

    def two_pair(self):
        if (len(self.unique_dice) in [2, 3] and
                any(self.dice.count(d) in [1, 2] for d in self.unique_dice)):
            return sum(d * 2 for d in self.unique_dice
                       if self.dice.count(d) >= 2)
        return 0

    def three_of_a_kind(self):
        if (len(self.unique_dice) <= 3 and
                any(self.dice.count(d) >= 3 for d in self.unique_dice)):
            return sum(d * 3 for d in self.unique_dice
                       if self.dice.count(d) >= 3)
        return 0

    def four_of_a_kind(self):
        if (len(self.unique_dice) <= 2 and
                any(self.dice.count(d) >= 4 for d in self.unique_dice)):
            return sum(d * 4 for d in self.unique_dice
                       if self.dice.count(d) >= 4)
        return 0

    def _get_num_sequential_dice(self):
        count = 1  # There will always be at least one die "in a row"
        last_d = self.dice[0]
        for d in self.dice:
            if d == last_d + 1:
                count += 1
            last_d = d
        return count

    def small_straight(self):
        count = self._get_num_sequential_dice()
        if count >= 4:
            return 30
        return 0

    def large_straight(self):
        count = self._get_num_sequential_dice()
        if count >= 5:
            return 40
        return 0

    def full_house(self):
        if (len(self.unique_dice) == 2 and
                all(self.dice.count(d) in [2, 3] for d in self.unique_dice)):
            return 25
        return 0
