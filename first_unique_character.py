
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return -1
        if len(s) == 1:
            return 0
        
        seen = set(s[0])
        unique = s[0]
        index = 0
        i = 1
        while i < len(s):
            if index != -1:
                if unique in s[i:]:
                    index = -1
                else:
                    return index
                
            while s[i] in seen and i < len(s) - 1:
                    i += 1
                    
            if i != len(s) - 1:
                seen.add(s[i])
                unique = s[i]
                index = i
            else:
                if s[i] not in s[:i]:
                    return i
            i += 1
                
        return index 
          
                
 