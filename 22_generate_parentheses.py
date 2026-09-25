class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        self.backtrack(ans, [], 0, 0, n)
        return ans

    def backtrack(self, ans: list[str], cur: list[str], open: int, close: int, max: int) -> None:
        if len(cur) == max * 2:
            ans.append("".join(cur))
            return
        
        if open < max:
            cur.append("(")
            self.backtrack(ans, cur, open+1, close, max)
            cur.pop()
        
        if close < open:
            cur.append(")")
            self.backtrack(ans, cur, open, close+1, max)
            cur.pop()
