from LinkedList import LinkedList

class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)


  def create_arr(self, size):
    """ Creates an array (list) of a given size 
    and populates each of its elements with a LinkedList object """
        
    array = []
    
    for i in range(size): 
      new_ll = LinkedList()
      array.append(new_ll)
    
    return array



  def hash_func(self, key):
    """ Hash functions are a function that turns each of these keys 
    into an word_len value that we can use to decide where in our list 
    each key:value pair should be stored. """

    hash_key = hash(key)
    index = (hash_key * 21) % self.size

    return index



  def insert(self, key, value):
    hash_key = self.hash_func(key)
    new_ll = self.arr[hash_key].find_update(key)

    item = (key, value)
    
    if new_ll == -1:
      self.arr[hash_key].append(item)



  def print_key_values(self):
    for ll in self.arr: 
      ll.print_nodes()
    
    print('Traverse finished')