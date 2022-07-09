class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        # mr = Mid Row, mc = Mid Col Element
        # COLUMN WISE BINARY SEARCH
        top, bot = 0, ROWS - 1
        while top <= bot:
            mr = (top + bot) // 2
            # TARGET > LAST ELEMENT IN COLUMN
            if target > matrix[mr][-1]:
                top = mr + 1         
            # TARGET < FIRST ELEMENT IN COLUMN
            elif target < matrix[mr][0]:
                bot = mr - 1
            else:
                break
        
        if not (top <= bot):
            return False
        
        # ROW WISE BINARY SEARCH
        mr = (top + bot) // 2 # -> CAN ELEMINATE THIS LINE; BUT INCREASES TIME
        l, r = 0, COLS - 1
        while l <= r:
            # TARGRET > LEFT
            mc = (l + r) // 2
            if target > matrix[mr][mc]:
                l = mc + 1
            # TARGET < RIGHT
            elif target < matrix[mr][mc]:
                r = mc - 1
            else:
                return True
        return False 