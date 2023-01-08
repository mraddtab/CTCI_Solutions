class Node:
   def __init__(self, val, next):
      self.val = val
      self.next = next

class SLinkedList:
  def __init__(self, head):
    self.head = head

  def printList(self):
    curr = self.head
    while curr != None:
      print(curr.val)
      curr = curr.next
  def kthToLast(self, k):
    array = []
    curr = self.head
    while curr != None:
      array.append(curr.val)
      curr = curr.next
    return array[len(array) - k]

  def kthToLastRecursive(self, node, k):
    if node == None:
      return 0
    index = self.kthToLastRecursive(node.next, k) + 1
    if index == k:
      print(node.val)
    return index
  
n7 = Node(7, None)
n6 = Node(6,n7)
n5 = Node(5, n6)
n4 = Node(4,n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)
list = SLinkedList(n1)

list.kthToLastRecursive(n1, 2)
