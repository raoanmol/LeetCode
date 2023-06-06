class Solution:
    def decodeString(self, s: str) -> str:
        res = []

        for i in range(len(s)):
            if s[i] != ']':
                res.append(s[i])
            else:
                substr = ""
                while res[-1] != '[':
                    substr = res.pop() + substr
                res.pop()

                num = ""
                while res and res[-1].isdigit():
                    num = res.pop() + num
                res.append(int(num) * substr)

        return "".join(res)
        
