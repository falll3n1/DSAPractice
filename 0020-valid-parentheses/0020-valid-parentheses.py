class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        pair = {')' :'(','}' :  '{',']' : '['}

        for ch in s:
            if ch in pair:
                if not st or st[-1] != pair[ch]:
                    return False
                st.pop()
            else:
                st.append(ch)

        return len(st) == 0
