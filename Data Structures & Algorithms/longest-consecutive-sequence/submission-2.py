class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums: return 0
        # max_ele = max(nums)
        # freq_arr = [False for _ in range(max_ele + 1)]
        # for ele in nums:
        #     freq_arr[ele] = True
        
        # max_count = -float('inf')
        # i, j = 0, 0
        # while i < len(freq_arr) and j < len(freq_arr):
        #     if freq_arr[j]:
        #         if i == j: max_count = max(max_count, 1)
        #         else:
        #             max_count = max(max_count, (j-i)+1)
        #         j+=1
        #     else:
        #         while j < len(freq_arr) and not freq_arr[j]:
        #             j+=1
        #         i = j
        # return max_count


        numSet = set(nums)
        longest_sequence = 0
        for ele in nums:
            # checking if element can be the start of the sequence
            if not (ele-1) in numSet:
                length = 1
                while (ele + length) in numSet:
                    length += 1
                longest_sequence = max(longest_sequence, length)
        return longest_sequence




        