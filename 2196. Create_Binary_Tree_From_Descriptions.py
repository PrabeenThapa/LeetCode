# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node_map = defaultdict(TreeNode)
        children_set = set()
        potential_roots = set()

        for parent, child, is_left in descriptions:
            children_set.add(child)
            potential_roots.discard(child)

            if parent not in children_set:
                potential_roots.add(parent)
            
            if parent not in node_map:
                node_map[parent] = TreeNode(val=parent)
            if child not in node_map:
                node_map[child] = TreeNode(val=child)
                
            if is_left:
                node_map[parent].left = node_map[child]
            else:
                node_map[parent].right = node_map[child]

        root_val = potential_roots.pop()
        return node_map[root_val]
