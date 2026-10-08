class Solution(object):
    def mergeAlternately(self, word1, word2):
        final=""
        i, j = 0, 0
        length = max(len(word1), len(word2))
        while(length):
            if i < len(word1):
                final += word1[i]
                i += 1

            if j < len(word2):
                final += word2[j]
                j += 1

            length -= 1
        return final 
        
