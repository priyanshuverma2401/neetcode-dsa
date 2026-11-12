class Solution:
    def merge(self, arr, LEFT, MID, RIGHT):
        left_copy, right_copy = arr[LEFT:MID+1], arr[MID+1: RIGHT+1]
        i, j, k = LEFT, 0, 0
        while j < len(left_copy) and k < len(right_copy):
            if left_copy[j] < right_copy[k]:
                arr[i] = left_copy[j]
                j+=1
            else:
                arr[i] = right_copy[k]
                k+=1
            i+=1
        
        while j < len(left_copy):
            arr[i] = left_copy[j]
            j+=1
            i+=1
        
        while k < len(right_copy):
            arr[i] = right_copy[k]
            k+=1
            i+=1
        
        return arr


    def mergeSort(self, arr, left, right):
        if left == right: return arr
        
        mid = (left + right) // 2
        self.mergeSort(arr, left, mid)
        self.mergeSort(arr, mid+1, right)
        self.merge(arr, left, mid, right)
        return arr

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums, 0, len(nums)-1)
        