class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = y = 0
        
        for move in moves:
            if move == "U": y += 1
            elif move == "D": y -= 1
            elif move == "R": x += 1
            elif move == "L": x -= 1
        
        return x == y == 0



        vertical = 0
        horizontal = 0
        
        for move in moves:
            if move == "U":
                vertical += 1
            elif move == "D":
                vertical -= 1
            elif move == "R":
                horizontal += 1
            elif move == "L":
                horizontal -= 1
        
        return vertical == horizontal == 0