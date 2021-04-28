from Node import Node

class LinkedList:

  def __init__(self):
    self.head = None


  def append(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node

  # Changed the find function so it finds and updates
  # Used this in the insert method
  def find_update(self,item):
    current = self.head
    found = False
    # counter = 0 (no need for counter bc we are updating)

    # While there are items to search in the Linked List, keep looping
    # or item has not been found, keep looping
    while current != None and not found:

      # If item is found at data[0]
      if current.data[0] == item:
        found = True
      # Else continue to next
      else:
        current = current.next

    # If it is found
    if found:
      # Increase the value by 1 and updated current
      value = current.data[1]
      current.data = (current.data[0], (value + 1))
    # Else return -1 to indicate it doesn't exist
    else:
      return -1



  def length(self):
    if self.head == None:
      return 0
    else:
      counter = 1
      current = self.head
      while(current.next):
        current = current.next
        counter +=1
      return counter


  def print_nodes(self):
    current = self.head
    
    if current == None:
      print('The linked list is empty.')
    else:
      for i in range(self.length()):
        print(f'{current.data[0]}: {current.data[1]}')
        current = current.next