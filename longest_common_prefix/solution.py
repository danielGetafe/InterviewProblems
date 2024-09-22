class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        sorted_strs = sorted(strs, key=len)
        print(sorted_strs)
        prefix = sorted_strs[0]
        for word in sorted_strs:
            if prefix == "":
                return ""
            for index, letter in enumerate(prefix):
                if letter != word[index]:
                    prefix = prefix[0:index]
                    break
        return prefix
