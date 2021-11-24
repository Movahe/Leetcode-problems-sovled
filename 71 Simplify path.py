class Solution:
    def simplifyPath(self, path: str) -> str:
        answer = ''
        to_go_back = 0
        # the number of directories to 'pop'
        path = path.split('/')
        print(path)
        for i in range(len(path) - 1, -1, -1):
            dir = path[i]
            if dir == '' or dir == '.':
                continue
            elif dir == '..':
                to_go_back += 1
            elif to_go_back:  # read: if this is a real directory and we have directories we still need to pop, pop it
                to_go_back -= 1
            else:
                answer = '/' + dir + answer

        return answer if answer else '/'  # if you're left with the empty string, return '/'

    def simplifyPath_stack(self, path: str) -> str:

        # Initialize a stack
        stack = []

        # Split the input string on "/" as the delimiter
        # and process each portion one by one
        print(path.split("/"))
        for portion in path.split("/"):

            # If the current component is a "..", then
            # we pop an entry from the stack if it's non-empty
            if portion == "..":
                if stack:
                    stack.pop()
            elif portion == "." or not portion:
                # A no-op for a "." or an empty string
                continue
            else:
                # Finally, a legitimate directory name, so we add it
                # to our stack
                stack.append(portion)

        # Stich together all the directory names together
        final_str = "/" + "/".join(stack)
        return final_str

    # Time complexity: O(N)
    # Space complexity: O(N)


path = "/a/./b/..//c/"
res = Solution().simplifyPath_stack(path)
print(res)