class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome(x):
            l,r=0,len(x)-1
            while l<r:
                if x[l]!=x[r]:
                    return False
                l+=1
                r-=1
            return True
        x=""
        for i in range(len(s)):
            for j in range(len(s)):
                substring=s[i:j+1]
                if palindrome(substring) and len(substring)>len(x):
                    x=substring
        return x            
                




        