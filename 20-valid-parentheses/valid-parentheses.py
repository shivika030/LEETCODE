class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dic={'(': ')', '{': '}', '[' : ']'}
        for i in range(len(s)):

            if s[i] in dic.keys():
                stack.append(s[i])

            elif s[i] in dic.values():
                if not stack:
                    return False

                if dic[stack[-1]]==s[i]:
                    stack.pop()
                else:
                    return False
            else:
                return False

        return True if not stack else False                  
        