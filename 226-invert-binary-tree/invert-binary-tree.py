# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque()
        newRoot = root

        if root == None:
            return root
        
        queue.append(newRoot)

        while len(queue) > 0:
            newRoot = queue.pop()
            print(newRoot.val)
            # if newRoot.left != None and newRoot.right != None:
            #     queue.append(newRoot.left)
            #     queue.append(newRoot.right)
            newRoot.right, newRoot.left = newRoot.left, newRoot.right
            if newRoot.left != None:
                # newRoot.right = newRoot.left
                # newRoot.left = None
                queue.append(newRoot.left)
                # queue.append(newRoot.right)
            if newRoot.right != None:
                # newRoot.left = newRoot.right
                # newRoot.right = None
                # queue.append(newRoot.left)
                queue.append(newRoot.right)

            # elif newRoot.left != None and newRoot.right == None:
            #     newRoot.right = newRoot.left
            #     newRoot.left = None
            # elif newRoot.right != None and newRoot.left == None:
                # newRoot.left = newRoot.right
                # newRoot.right = None
            # newRoot = newRoot.left


        # while newRoot != None:
        #     newRoot.left, newRoot.right = newRoot.right, newRoot.left
        #     newRoot = newRoot.left
            # if newRoot.left == None and root.right != None:
            #     newRoot = root.right
        
        return root

    # def recursionInverting(node)    