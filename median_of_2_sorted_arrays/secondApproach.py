class Solution2:
    """
    We assume that both nums1 and nums2
    are numeric sorted lists
    nums1 --> List[int]
    nums2 --> List[int]
    return value --> float
    """

    def findMedianSortedLists(self, nums1, nums2) -> float:
        # nums1 must be the smallest one
        if len(nums1) > len(nums2):
            auxiliarList = list(nums1)
            nums1 = list(nums2)
            nums2 = auxiliarList

        nums1Size = len(nums1)
        nums2Size = len(nums2)

        # Handle empty input parameters
        if nums1Size == 0 and nums2Size == 0:
            return 0

        # TODO --> Binary search spliting each list in 2 halves
        # TODO --> calculate min of left part or max of the right one
        return 0


"""Tests examples"""


def main():
    solution = Solution2()

    a, b = [2], [1, 3]  # 2
    result = solution.findMedianSortedLists(a, b)
    print(
        "\033[1;32m" + "Test passed: result " + str(result)
    ) if result == 2 else print(
        "\033[1;91m" + "Test failed: result " + str(result) + " should be 2"
    )

    a, b = [1, 2, 3], [4, 5, 6]  # 3.5
    result = solution.findMedianSortedLists(a, b)
    print(
        "\033[1;32m" + "Test passed: result " + str(result)
    ) if result == 3.5 else print(
        "\033[1;91m" + "Test failed: result " + str(result) + " should be 3.5"
    )

    a, b = [4, 5, 6], [1, 2, 3]  # 3.5
    result = solution.findMedianSortedLists(a, b)
    print(
        "\033[1;32m" + "Test passed: result " + str(result)
    ) if result == 3.5 else print(
        "\033[1;91m" + "Test failed: result " + str(result) + " should be 3.5"
    )

    a, b = [1, 2, 3], [4, 5, 6, 7]  # 4
    result = solution.findMedianSortedLists(a, b)
    print(
        "\033[1;32m" + "Test passed: result " + str(result)
    ) if result == 4 else print(
        "\033[1;91m" + "Test failed: result " + str(result) + " should be 4"
    )

    a, b = [5, 6, 7], [1, 2, 3, 4]  # 4
    result = solution.findMedianSortedLists(a, b)
    print(
        "\033[1;32m" + "Test passed: result " + str(result)
    ) if result == 4 else print(
        "\033[1;91m" + "Test failed: result " + str(result) + " should be 4"
    )

    a, b = [2, 7], [1, 3, 5]  # 3
    result = solution.findMedianSortedLists(a, b)
    print(
        "\033[1;32m" + "Test passed: result " + str(result)
    ) if result == 3 else print(
        "\033[1;91m" + "Test failed: result " + str(result) + " should be 3"
    )


if __name__ == "__main__":
    main()
