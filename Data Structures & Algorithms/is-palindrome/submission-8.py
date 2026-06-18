# A 2 pointer Solution has a variable pointing
#  at the front and another at the end
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s))
        s = s.lower()
        first = 0
        last = len(s) - 1
        while first < last:
            if(s[first] == s[last]):
                first = first + 1
                last = last - 1
                continue
            elif(s[first] != s[last]):
                return False
        return True