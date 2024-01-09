class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        hash_map_solutions = {}
        index = 0
        numbers_length = len(numbers)
        while index < numbers_length:
            if index+1 < numbers_length and numbers[index] + numbers[index+1] == target:
                return [index+1, index+2]
            hash_map_solutions[target - numbers[index]] = index + 1
            index += 1
        index = 0
        while index < numbers_length:
            try:
                return [hash_map_solutions[target - numbers[index]], hash_map_solutions[numbers[index]]]
            except KeyError:
                index += 1
                continue

        
if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    assert Solution().twoSum(numbers, target) == [1, 2]

    numbers = [2, 3, 4]
    target = 6
    assert Solution().twoSum(numbers, target) == [1, 3]

    numbers = [-1, 0]
    target = -1
    assert Solution().twoSum(numbers, target) == [1, 2]

    numbers = [3, 3]
    target = 6
    assert Solution().twoSum(numbers, target) == [1, 2]

    number = [0,0,6,8]
    target = 0
    assert Solution().twoSum(number, target) == [1, 2]

    print("All tests passed!")
