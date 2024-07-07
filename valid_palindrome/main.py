class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(ch for ch in s if ch.isalnum())
        for index in range(int((len(s) / 2))):
            if s[index] != s[-(index + 1)]:
                return False
        return True


if __name__ == "__main__":
    s = "race a car"
    assert Solution().isPalindrome(s) is False
    s = "A man, a plan, a canal: Panama"
    assert Solution().isPalindrome(s)
    s = " "
    assert Solution().isPalindrome(s)
    print("All tests passed!")
