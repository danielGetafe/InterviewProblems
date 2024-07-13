class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word_length = 0
        string_to_splited_list = s.split(" ")
        index = len(string_to_splited_list) - 1
        while last_word_length == 0:
            if string_to_splited_list[index] != "":
                last_word_length = len(string_to_splited_list[index])
            index -= 1
        return last_word_length
