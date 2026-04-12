class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numofIslands = 0

        # Loop through grid
        for row in range(len(grid)):
            for col in range(len(grid[0])):

        # When you hit a 1 one, increment counter and start BFS
                if grid[row][col] == "1":
                    numofIslands += 1
                    self.bfs(grid, row, col)

        return numofIslands

    # BFS helper: use queue, check up/down/left/right turn 1s to 0
    def bfs(self, grid, row, col):
        queue = collections.deque()
        grid[row][col] = "0"
        queue.append((row,col))

            
        while queue:
        # pull a cell of the queue
            r, c = queue.popleft()
                
            # check its 4 neighbors
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr = r + dr
                nc = c + dc
                # check if neighbors are within grid dimensions
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    # if a neighbor is a 1, turn it to 0 and add it to the queue
                    if grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        queue.append((nr, nc))

        
            


        