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
      
  def removeNode(self, node):
    if node != None or node.next != None:
      next = node.next
      node.next = next.next
      node.val = next.val
  
  def partition(self, x):
    R = self.head
    L = R
    while R.next:
      if R.next.val < x:
        newLeft = R.next
        R.next = R.next.next
        newLeft.next = L
        L = newLeft
      else:
        R = R.next
    self.head = L
    
    
  
n7 = Node(1, None)
n6 = Node(2,n7)
n5 = Node(10, n6)
n4 = Node(5,n5)
n3 = Node(8, n4)
n2 = Node(5, n3)
n1 = Node(3, n2)
list = SLinkedList(n1)
list.partition(5)
list.printList()
