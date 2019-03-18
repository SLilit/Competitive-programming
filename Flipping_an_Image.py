class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        
        for row in A:
            for j in range((len(row)+1)/2):
                row[j], row[~j] = row[~j] ^ 1, row[j] ^ 1 
        
        return A