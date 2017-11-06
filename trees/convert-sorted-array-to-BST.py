"""
Goal : Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

Input : list[int] sorted - ascending

Output : A Tree

Questions : can there be repeats? Maybe ?
Example : 1 2 3 4 5 6 7 8            |  -1 -1 0 2 4

    -find the mid, mid = len(mid)/2 is len(mid) % 2 == 1 else (len(mid)/2 - 1)
    -pick the middle element, i.e arr[mid]
    -make the middle element the root? then proceed in a binary search way, left get's added to the left and right get's added to the right.
    -then insert elements that are not in the tree. (keep track of indices that are accounted for and skip them, while doing an insert.)

  4
2   6
      8

w.r.t original : 3 1 5       |  2 0 3
own scopes:      3 1 1       |  2 0 0

there always has to be a +1 in RHS
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        if not nums:
            return

        mid = len(nums)//2

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root
