class Solution:
    def isPalindrome(self, s: str) -> bool:
        #two pointer method

        left=0
        right=len(s)-1
            
        while left<right:
            while left<right and not self.alphanums(s[left]):
                left+=1
            while left<right and not self.alphanums(s[right]):
                right-=1
            if s[left].lower()!=s[right].lower():
                return False
            
            left+=1
            right-=1
        return True
    def alphanums(self,c):
            return  ( ord('a')<=ord(c.lower())<=ord('z') or
            ord('0')<=ord(c)<=ord('9') )
