class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hash_row = set()
        hash_column = set()
        hash_3 = set()
        for row in range(9):
            for col in range(9):
                val = board[row][col]

                if val == ".":
                    continue
                if (row, val) not in hash_row:
                    hash_row.add((row, val))
                else:
                    return False
                if (col, val) not in hash_column:
                    hash_column.add((col, val))
                else:
                    return False
                index = (row//3) * 3 + (col//3)

                if (index, val) not in hash_3:
                    hash_3.add((index, val))
                else:
                    return False
        return True
                


                
            
        
        
        


        