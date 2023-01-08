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
  
n7 = Node(7, None)
n6 = Node(6,n7)
n5 = Node(5, n6)
n4 = Node(4,n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)
list = SLinkedList(n1)
list.removeNode(n2)
list.printList()
