# 栈
class Solution:
    def isValid(self, s: str) -> bool:
        # TODO: 在这里写你的代码
        stack = []
        mapping = {')':'(', '}':'{', ']':'['}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping:
                if stack and stack[-1] == mapping[char]:
                    stack.pop()
                else:
                    return False  # 错误
        return True  # 正确


if __name__ == "__main__":
    # 示例 1
    s = "()"
    print(Solution().isValid(s))  # 期望输出: True

    # 示例 2
    s = "()[]{}"
    print(Solution().isValid(s))  # 期望输出: True

    # 示例 3
    s = "(]"
    print(Solution().isValid(s))  # 期望输出: False

    # 示例 4
    s = "([)]"
    print(Solution().isValid(s))  # 期望输出: False

    # 示例 5
    s = "{[]}"
    print(Solution().isValid(s))  # 期望输出: True