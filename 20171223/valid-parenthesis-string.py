class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        (*)( ---- The * changes to )
                  which could not close the last (
        ()(* ---- valid
        """
        l = 0
        r = 0
        star = 0
        starr = 0
        for i, c in enumerate(s):
            if c == '(':
                l += 1
            elif c == ')':
                if l <= r + starr and starr:
                    starr -= 1
                    star  += 1
                r += 1
            elif l > r + starr: # Convert * to ) to close (
                starr += 1
            else:
                star += 1
                
            if r > l:
                star -= (r - l)
                l = r
                if star < 0:
                    return False
        return l == r + starr