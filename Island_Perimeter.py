class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        grid.append([0]*len(grid[0]))
        grid.insert(0,[0]*len(grid[0]))
        grid = [x + [0] for x in grid]
        grid = [[0] + x for x in grid]

        #return grid[2]            
        perimeter = 0
        for i in range(len(grid)-1):
            for j in range(len(grid[i])-1):                      
                perimeter += grid[i][j] ^ grid[i+1][j]
                perimeter += grid[i][j] ^ grid[i][j+1]
        
        return perimeter