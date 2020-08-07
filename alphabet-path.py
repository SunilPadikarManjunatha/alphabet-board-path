class Solution:
    
    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]    
        
        i,j=0,0
        moves = ""
        coords = []
        start, end = 0,0

        for c in list(target):
            for i, row in enumerate(board):
                if c not in list(row): continue
                ind = list(row).index(c)
                if ind >=0:
                    coords.append([i,ind])
                    break

        j = 0
        while(j < len(coords)):
            row = coords[j]
            while(start != row[0] or end != row[1]):
                print(row)
                if row[0] > start:
                    for i in range(start, row[0]):
                        if self.isValid(board,i+1, end):
                            moves += "D"
                            start += 1
                    
                elif row[0] < start:
                    for i in range(row[0], start):
                        if self.isValid(board,i, end):
                            moves += "U"
                            start -= 1

                if row[1] > end:
                    for i in range(0,row[1]-end):
                        if self.isValid(board,start, i):
                            moves += "R"
                            end += 1
                elif row[1] < end:
                    for i in range(row[1], end):
                        if self.isValid(board,start, i):
                            moves += "L"
                            end -=1
            moves += "!"

            j+=1

        print(moves, coords)
        return moves
        
    def isValid(self,board, i,j):
        if i >= len(board) or j >= len(board[i]):
            return False

        return j < len(board[i])

sol = Solution()
print(sol.alphabetBoardPath("zdz"))
