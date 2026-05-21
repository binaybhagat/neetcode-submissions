class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time=0
        q = collections.deque()
        fresh=0
        direction=[[0,1],[0,-1],[1,0],[-1,0]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append((i,j))
                if grid[i][j]==1:
                    fresh +=1
        while fresh > 0 and len(q)>0:
            for i in range(len(q)):
                i,j = q.popleft()
                for dr,dc in direction:
                    row,col = dr +i, dc+j
                    if row<0 or col < 0 or row >(len(grid) -1) or col> (len(grid[0])-1) :
                        continue
                    else:
                        if grid[row][col]==1:
                            grid[row][col]=2
                            q.append((row,col))
                            fresh -=1
            time+=1
        return time if fresh ==0 else -1
