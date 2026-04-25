class Solution:
    def countSubstrings(self, s: str) -> int:
        def palindrome(x: str) -> int:
            if len(x) == 1:
                return 1
            l, r = 0, len(x) - 1
            while l < r:
                if x[l] != x[r]:
                    return 0
                l += 1
                r -= 1
            return 1

        count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j+1]
                if palindrome(substring) == 1:
                    count += 1
        return count
