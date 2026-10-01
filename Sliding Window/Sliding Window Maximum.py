"""
Sliding Window Maximum
You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge of the array. The window slides one position to the right until it reaches the right edge of the array.

Return a list that contains the maximum element in the window at each step.

Example 1:

Input: nums = [1,2,1,0,4,2,6], k = 3

Output: [2,2,4,4,6]
"""
class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        output = []
        q = collections.deque()

        left = right = 0

        while right < len(nums):

            # Remove smaller elements from the right
            while q and nums[right] >= nums[q[-1]]:
                q.pop()

            # Add current index
            q.append(right)

            # Move left if window is too large
            if right - left + 1 > k:
                left += 1

            # Remove elements outside the window
            if q[0] < left:
                q.popleft()

            # Window is ready
            if right - left + 1 == k:
                output.append(nums[q[0]])

            right += 1

        return output