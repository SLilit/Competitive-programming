class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        
        A.sort()
        for i in range(len(A) - 3, -1, -1):
            if A[i] + A[i+1] > A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0
        

        if len(A) < 3:
            return 0
       
        A.sort()
        A = A[::-1]

        for i in range(len(A)):

            if i+2 >= len(A):
                return 0
            if A[i] < A[i+1] + A[i+2]:
                return sum(A[i:i+3])
            