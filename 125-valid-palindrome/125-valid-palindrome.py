class Solution:
    def isPalindrome(self, s: str) -> bool:
        #newS = [i.lower() for i in s if i.isalnum()]
        #return newS == newS[::-1]
    
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l <r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l +=1; r -= 1
        return True