class Solution:
    """
    We assume that both nums1 and nums2
    are numeric sorted lists
    nums1 --> List[int]
    nums2 --> List[int]
    return value --> float
    """

    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums1Len, nums2Len = len(nums1), len(nums2)
        maxLenMergedList = (nums1Len + nums2Len) // 2 + 1
        index1, index2 = 0, 0
        lastNums1, lastNums2 = 0, 0

        if nums1Len + nums2Len == 0:
            return 0

        if (nums1Len + nums2Len) % 2 == 1:  # Sum is odd
            while (index1 + index2) < maxLenMergedList:
                if index1 < nums1Len and index2 < nums2Len:
                    if nums1[index1] <= nums2[index2]:
                        lastNums1 = nums1[index1]
                        index1 += 1

                    else:
                        lastNums1 = nums2[index2]
                        index2 += 1

                elif index1 < nums1Len:
                    lastNums1 = nums1[index1]
                    index1 += 1

                else:
                    lastNums1 = nums2[index2]
                    index2 += 1

            return lastNums1

        else:  # Sum is even
            while (index1 + index2) < maxLenMergedList:
                if index1 < nums1Len and index2 < nums2Len:
                    if nums1[index1] <= nums2[index2]:
                        lastNums1 = nums1[index1]
                        index1 += 1

                    else:
                        lastNums2 = nums2[index2]
                        index2 += 1

                elif index1 < nums1Len:
                    lastNums1 = nums1[index1]
                    index1 += 1

                else:
                    lastNums2 = nums2[index2]
                    index2 += 1

            return (lastNums1 + lastNums2) / 2


"""Tests examples"""


def main():
    a, b = [1, 3], [2]
    solution = Solution()
    print(solution.findMedianSortedArrays(a, b))


if __name__ == "__main__":
    main()
