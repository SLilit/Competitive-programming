class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        
        #open_p = set(['(','{','['])
        p_pairs = {")": "(", "}": "{", "]": "[" }
        seen_p = []
        for p in s:
            if p not in p_pairs:
                seen_p.append(p)
            elif seen_p == []:
                return False
            else:
                p_pair = seen_p.pop()
                if p_pair != p_pairs[p]:
                    return False
        
        return not seen_p
                
                
        