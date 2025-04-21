'''
Time complexity --> O(3^L), as discussed in the class.
Space Complexity --> O(L) recursive stack space, which is also equal to length of the word.

1. Took fine out of time to figure out the solution, may be more than 2 hours.
2. I got stuck in finding the proper returning statement.
3. After lot of console statements, found out the way!
4. Hoping practice would make me better at these!
5. major issues, returning true in self.helper function
6. Decrementing the count, if the count doesn't match.
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        counter=0
        curr=''

        for i in range(len(board)):
            for j in range(len(board[0])):

                if(board[i][j]==word[counter]):
                    temp = board[i][j]
                    board[i][j]='#'

                    curr+=board[i][j]

                    value = self.helper(board, i, j, counter+1, word)
                    if value:
                        return value
                    board[i][j] = temp

        return False


    def helper(self, board,i,j ,counter, word):

        # print(counter,i,j)

        if(counter ==len(word)):
            return  True

        directions =[[0,1],[0,-1],[1,0],[-1,0]]

        for dr, dc in directions:
            ur = i+dr
            uc = j+dc
            # print("ur and uc are", ur,uc)




            if ur in range(len(board)) and uc in range(len(board[0])) and counter<len(word):

                # print("inside directions",ur,uc, board[ur][uc])

                if board[ur][uc]==word[counter]:
                    temp = board[ur][uc]
                    counter+=1
                    board[ur][uc]='#'
                    if self.helper( board,ur,uc, counter, word):
                        return True
                    board[ur][uc] = temp
                    counter-=1


