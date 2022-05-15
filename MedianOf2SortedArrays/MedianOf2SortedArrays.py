class Solution:

    '''
    nums1 --> List[int]
    nums2 --> List[int]
    return value --> float
    '''
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        
        nums1Len, nums2Len = len(nums1), len(nums2)
        maxLenMergedList = (nums1Len + nums2Len) / 2 + 0.5
        index1, index2 = 0, 0
        mergedList = []
        done = False

        if nums1Len + nums2Len == 0:
            return 0

        while len(mergedList) < maxLenMergedList:

            if index1 < nums1Len and index2 < nums2Len:
                if nums1[index1] <= nums2[index2]:
                    mergedList.append(nums1[index1])
                    index1 += 1
                else:
                    mergedList.append(nums2[index2])
                    index2 += 1
            elif index1 < nums1Len:
                mergedList.append(nums1[index1])
                index1 += 1
            else:
                mergedList.append(nums2[index2])
                index2 += 1



        if (nums1Len + nums2Len) % 2 == 0:
            return (mergedList[-1] + mergedList[-2]) / 2
        return mergedList[-1]

def main():
    a, b = [1, 3], [2]
    solution = Solution()
    print(solution.findMedianSortedArrays(a, b))

if __name__ == "__main__":
    main()
