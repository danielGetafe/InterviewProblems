class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        return self.rec_parenthesis(n)

    def rec_parenthesis(
        self, n: int, item: str = "", opened: int = 0, closed: int = 0
    ) -> list[str]:
        if opened == closed == n:
            return [item]
        result_list = []
        if opened < n:
            result_list.extend(self.rec_parenthesis(n, f"{item}(", opened + 1, closed))
        if opened > closed:
            result_list.extend(self.rec_parenthesis(n, f"{item})", opened, closed + 1))
        return result_list
