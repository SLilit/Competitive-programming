class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        v = []
        new_s = list(s)
        for i in range(len(s)):

            if s[i] in vowels:
                v.append(i)
        
        for j in range(int((len(v) + 1)/2)):
            new_s[v[j]], new_s[v[~j]] = new_s[v[~j]], new_s[v[j]]
            
            
        return ''.join(new_s)





        vowels = set('aeuioAEUIO')
        new_s = list(s)
        l,r = 0, len(s) - 1
        while l < r:
            while l < r and new_s[l] not in vowels: l += 1
            while l < r and new_s[r] not in vowels: r -= 1
            if l == r:
                break
            new_s[l], new_s[r] = new_s[r], new_s[l]
            l += 1
            r -= 1
           
        return ''.join(new_s)