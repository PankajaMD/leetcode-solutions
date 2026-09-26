class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        ans = [0] * len(temperatures)
        stack.append(0)
        i = 1
        while i < len(temperatures):
            a = stack.pop()
            while temperatures[a] < temperatures[i]:
                ans[a] = i - a
                if stack:
                    a = stack.pop()
                else:
                    a = None
                    break
            if a is not None:
                stack.append(a)
            stack.append(i)
            i += 1
        return ans           

