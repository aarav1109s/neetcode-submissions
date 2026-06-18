class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count = [0] * 26
        window_size = len(s1)
        for i in range(window_size):
            count[ord(s1[i]) - ord("a")] += 1
            count[ord(s2[i]) - ord("a")] -= 1
        
        if count == [0] * 26:
            return True
        
        for right in range(window_size, len(s2)):
            left = right - window_size
            count[ord(s2[right]) - ord("a")] -= 1
            count[ord(s2[left]) - ord("a")] += 1
        
            if count == [0] * 26:
                return True
    
        return False
        

