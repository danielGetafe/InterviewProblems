class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        return self.rec_parenthesis(n)

    def rec_parenthesis(self, n: int, item: str = "", opened: int = 0, closed: int = 0) -> list[str]:
        if opened == closed == n:
            return [item]
        open_added, closed_added = [], []
        if opened < n:
            open_added = self.rec_parenthesis(n, f"{item}(", opened+1, closed)
        if opened > closed:
            closed_added = self.rec_parenthesis(n, f"{item})", opened, closed+1)
        open_added.extend(closed_added)
        return open_added
