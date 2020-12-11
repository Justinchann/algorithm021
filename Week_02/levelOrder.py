"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
import collections


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = []
        deque = collections.deque([root])
        while deque:
            tmp = []
            for i in range(len(deque)):
                root = deque.popleft()
                tmp.append(root.val)
                for c in root.children:
                    deque.append(c)
            res.append(tmp)
        return res


        # def tra(root,level):
        #     if len(res)==level:
        #         res.append([])
        #     res[level].append(root.val)
        #     for c in root.children:
        #         tra(c,level+1)
        # res = []
        # if not root:
        #     return []
        # tra(root,0)
        # return res