class Solution:
    def simplifyPath(self, path: str) -> str:
            stack = []
            i = 0
            n = len(path)
            while i < n:
                while i < n and path[i] == '/':
                    i += 1
                if i >= n:
                    break        
                j = i
                while j < n and path[j] != '/':
                    j += 1
                segment=path[i:j]
                i = j
                if segment == "." or segment == "":
                    continue
                elif segment == "..":
                    if stack:
                        stack.pop()
                else:
                    stack.append(segment)
            return "/" + "/".join(stack)
