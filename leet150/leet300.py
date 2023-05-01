class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        piles = []

        for card in nums:
            # If there is no existing pile, create the first pile
            if not piles:
                piles.append(card)
                continue  # Go to next "i" w/o executing below code.

            card_dealed = False  # Track if card "i" has been dealed.
            for i in range(0, len(piles)):
                # If there is a pile where the number should be placed
                # (because the number is less than equal to the last
                # number in the pile)
                if piles[i] >= card:
                    piles[i] = card
                    card_dealed = True
                    break

            if not card_dealed:
                piles.append(card)

        return len(piles)