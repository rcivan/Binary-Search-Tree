class BinarySearchTree:

    def __init__(self):
        self.root = None

    # Insert something into the tree.
    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self.root.insert(val)

    # Check if a value is in the tree.
    def contains(self, val):
        if self.root is None:
            return False
        else:
            return self.root.contains(val)

    # Return all the items in the tree as a sorted list.
    def toList(self):
        if self.root is None:
            return []
        else:
            return self.root.toList()

    def largest(self):
      if self.root is None:
          return None
      else:
          return self.root.largest()

    def depth(self):
      if self.root is None:
        return 0
      else:
        return self.root.depth()


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def getVal(self):
        return self.val

    def setVal(self, newVal):
        self.val = newVal

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setLeft(self, newLeft):
        self.left = newLeft

    def setRight(self, newRight):
        self.right = newRight

    # Insert something into the tree.
    def insert(self, val):
        if self.val is None:
            self.val = val
            return

        if val < self.val:
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = Node(val)
            else:
                self.right.insert(val)

    def contains(self, val):
        if self.val == val:
            return True
        if val < self.val:
            if self.left is None:
              return False
            else:
              return self.left.contains(val)
        if val > self.val:
            if self.right is None:
              return False
            else:
              return self.right.contains(val)

    def largest(self):
      if self.right is None:
        return self.val
      else:
        return self.right.largest()

  
    # Return all the items in the tree as a sorted list.
    def toList(self):
      if self.left is None:
        leftList = []
      else:
        leftList = self.left.toList()
        
      if self.right is None:
        rightList = []
      else:
        rightList = self.right.toList()
        
      return leftList + [self.val] + rightList

    def depth(self):
      if self.val is None:
        return 0
      elif self.left is None and self.right is not None:
        return 1 + self.right.depth()
      elif self.right is None and self.left is not None:
        return 1 + self.left.depth()
      elif self.right is None and self.left is None:
        return 1
      else:
        return 1 + max(self.right.depth(), self.left.depth())


def main():
  s = input("Enter a list of numbers, seperated by spaces: ")
  lst = s.split()

  tree = BinarySearchTree()
  for x in lst:
    tree.insert(float(x))

  print(tree.toList())
  print(tree.contains(7))
  print(tree.largest())
  print(tree.depth())
  

if __name__ == "__main__":
    main()