class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''j=0
        max_val=[]
        for i in range(len(nums)):
            j=i+1
            while j-i < k:
                j+=1'''

        '''max_val = []

        for i in range(len(nums) - k + 1):
            max_val.append(max(nums[i:i+k]))

        return max_val '''   
        output = []
        q = deque()  # index
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output