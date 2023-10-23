class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        c = 0 
        for x in range(len(piles)//3, len(piles), 2):
            c += piles[x]

        return c
