import copy
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # once visited, replace with .
        r = len(board) # 3
        c = len(board[0]) # 4
        def search(y, x, count):
            if count == len(word):
                # print("returns true")
                return 1

            res = 0
            continues = False
            temp = board[y][x]
            board[y][x] = "."
            # print(board, "currently on", x, y, "count", count)
            if x-1 >= 0 and board[y][x-1] == word[count]: #left
                    # print("l")
                    res += search(y,x-1, count+1)
                    continues = True

            if x+1 < c and board[y][x+1] == word[count]: #right
                    # print("r")
                    res +=  search( y,x+1, count+1)
                    continues = True

            if y-1 >= 0 and board[y-1][x] == word[count]: #up
                    # print("u")
                    res +=  search( y-1,x, count+1)
                    continues = True

            if y+1 < r and board[y+1][x] == word[count]: #down
                    # print("d")
                    res += search(y+1,x, count+1)
                    continues = True

            board[y][x] = temp

            if not continues:
                # print("returns false")
                return 0

            return res



        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0]:
                    # print(i, j, "is a start")
                    if (search(i, j, 1)):
                        return True

        return False
