class Solution:
    def numSquares(self, n: int) -> int:
        if n == 0:
            return 0
        
        sqr = [[x*x,1] for x in reversed(range(1,int(pow(n,0.5))+1))]
        visited = set(sqr[:][0])
        frontier = sqr[:]
        while frontier:
            s = frontier.pop(0)
            if s[0] == n:
                return s[1]
           
            else:
                for sq in sqr:
                    new_sum = s[0] + sq[0]
                    if new_sum <= n and new_sum not in visited:
                        frontier.append([new_sum,sq[1]+s[1]])
                        visited.add(new_sum)
                    
                    
            
            
        