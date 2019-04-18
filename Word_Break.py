        word = [0]*(len(s)+1)
        word[0] = 1
        
        for i in range(len(s)):
            for j in range(len(s[:i+1])):
                if word[j] == 1 and s[j:i+1] in wordDict:
                    print (s[j:i+1])
                    word[i+1] = 1
                    break
                    
        if word[-1]:
            return True
        return False