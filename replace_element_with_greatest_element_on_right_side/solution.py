class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        reverse_result = []
        max_number = -1
        for index in range(len(arr) - 1, 0, -1):
            if arr[index] > max_number:
                max_number = arr[index]
            reverse_result.append(max_number)
        reverse_result.reverse()
        reverse_result.append(-1)
        return reverse_result
