"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.
Inorder (Left -> Root -> Right)

Preorder (root -> left -> right)



Algorithm Inorder(tree)
   1. Traverse the left subtree, i.e., call Inorder(left-subtree)
   2. Visit the root.
   3. Traverse the right subtree, i.e., call Inorder(right-subtree)


A complete discuss about inOrder, PreOrder, PostOrder is given in:
https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/713539/Python-3-All-Iterative-Traversals-InOrder-PreOrder-PostOrder-Similar-Solutions

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):  # recursively
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)

    # Complexity Analysis
    #
    # Time complexity : O(n). The time complexity is O(n) because the recursive function is
    # T(n) = 2 T(n/2)+1T(n)=2⋅T(n/2)+1.
    #
    # Space complexity : The worst case space required is O(n), and in the average case it's O(logn)
    # where n is number of nodes.

    # # iteratively
    def inorderTraversal_1(self, root):
        res, stack = [], []
        while stack or root:
            if root:  # travel to each node's left child, till reach the leftmost leaf
                stack.append(root)
                root = root.left

            # this node has no left child
            else:
                tmpNode = stack.pop()

                # so let's append the node value
                res.append(tmpNode.val)

                # visit its right child --> if it has left child ?
                # append left and left.val, otherwise append node.val, then visit right child again... cur = node.right
                root = tmpNode.right
        return res

    #
    # Time complexity : O(n)O(n).
    #
    # Space complexity : O(n)O(n).

    def inorderTraversal_2(self, root):
        stack = [(False, root)]
        res = []
        while stack:
            visited, node = stack.pop()
            if node:
                # In the loop: If we get a node with flag false, we add children in correct order and set them to false.
                #  because they have to be processed (for their children). And we set flag of current node to true.

                if not visited:  # in inOrder, the order should be: left -> root -> right
                    stack.append((False, node.right))
                    stack.append((True, node))
                    stack.append((False, node.left))

                # If we get node with flag set to true we simply print its value (add to acc).
                else:
                    res.append(node.val)
        return res

    # In PostOrder, the order should be:
    # left -> right -> root
    def postOrderTraversal(self, root):
        """
        :param root: TreeNode
        :return: List[int]
        """
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()  # the last element
            if node:
                if visited:
                    res.append(node.val)
                else:  # postorder: left -> right -> root
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return res

    # In preOrder, the order should be: root -> left -> right
    def preOrderTraversal(self, root):
        """
        :param root: TreeNode
        :return: List[int]
        """
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()  # the last element
            if node:
                if visited:
                    res.append(node.val)
                else:  # preOrder: root -> left -> right
                    stack.append((node.right, False))
                    stack.append((node.left, False))
                    stack.append((node, True))
        return res


