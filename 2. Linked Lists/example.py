class Node:
    def __init__ (self,data):
        #a node holds data and a pointer to the next node
        self.data = data
        self.next = None


class Linked_List:
    def __init__ (self):
        #Linked list stores a pointer to the first item in the list called the head.
        self.head = None
        #storing a pointer to the last item in the list makes adding a new node O(1) instead of O(n) complexity.
        self.tail = None
    
    def add_new_node (self,data):
        #if it's the first item in the list.
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
            return
        
        new = Node(data)
        #if there's already a tail
        self.tail.next = new
        self.tail = new
    
    def print_list (self):
        #traverse the list starting with the head
        current = self.head
        #keep going until there is no current
        while current:
            print (current.data)
            current = current.next

        

x = Linked_List()
x.add_new_node(8)
x.add_new_node(7)
x.add_new_node(9)
x.print_list()




