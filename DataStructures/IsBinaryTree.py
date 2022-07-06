""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""

def inorderTrav(root, output):
    if root:
        inorderTrav(root.left, output)
        output.append(root.data)   
        inorderTrav(root.right, output)
    return output

def check_binary_search_tree_(root):
    # print(root.left.data, root.data, root.right.data)
    x = inorderTrav(root, [])
    for i in range(1, len(x)):
        if x[i-1] >= x[i]:
            return False
    return True