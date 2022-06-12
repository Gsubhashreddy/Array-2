
#T(N)=O(M*N)
#S(N)=O(1)

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ar=[[0,-1],[0,1],[-1,0],[1,0],[-1,-1],[-1,1],[1,-1],[1,1]]
        
        m=len(board)
        n=len(board[0])
        for i in range(m):
            for  j in range(n):
                count=0
                for ele in ar:
                    x=i+ele[0]
                    y=j+ele[1]
                    if x>=0 and x<m and y>=0 and y<n:
                        if board[x][y]==1 or board[x][y]==-1:
                            count+=1
                if count<2 and board[i][j]==1:
                    board[i][j]=-1
                elif (count==2 or count==3) and board[i][j]==1:
                    board[i][j]=1
                elif count>3 and board[i][j]==1:
                    board[i][j]=-1
                elif count==3 and board[i][j]==0:
                    board[i][j]=2
        for i in range(m):
            for  j in range(n):
                if board[i][j]==-1:
                    board[i][j]=0
                elif board[i][j]==2:
                    board[i][j]=1
                    
                        
        