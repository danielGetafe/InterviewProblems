 
from asyncio.windows_events import NULL


class Solution2:

    '''Return the median of the list'''
    def getMedianOfLists(self, inputList, inputListSize):

        if inputListSize == 0:
            return 0

        if inputListSize % 2 == 0: #lenght is even
            return (inputList[inputListSize // 2] + \
                inputList[(inputListSize + 1) // 2]) / 2

        else: #lenght is odd
            return inputList[inputListSize] / 2

    '''
    We assume that both nums1 and nums2
    are numeric sorted lists
    nums1 --> List[int]
    nums2 --> List[int]
    return value --> float
    '''
    def findMedianSortedLists(self, nums1, nums2) -> float:

        #nums1 must be the smallest one
        if len(nums1) > len(nums2):
            auxiliarList = list(nums1)
            nums1 = list(nums2)
            nums2 = auxiliarList

        nums1Size = len(nums1)
        nums2Size = len(nums2)
        done = False

        #Handle empty input parameters
        if nums1Size == 0:
            return self.getMedianOfLists(nums2, nums2Size)

        if nums2Size == 0:
            return self.getMedianOfLists(nums1, nums1Size)

        #Split the lists in 2 parts
        indexBiggestLeft = (nums1Size + 1) // 2
        indexSmallestRight = (nums1Size + 1) // 2 + 1

        #TODO --> calculate min of left part or max of the right one


'''Tests examples'''
def main():

    a, b = [1, 3], [2]
    solution = Solution2()
    print(solution.findMedianSortedLists(a, b))

if __name__ == "__main__":
    main()
