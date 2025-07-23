#todo
#search for value
#delete a note

class Node:
    def __init__ (self,data):
        #a node holds data and a pointer to the next node
        self.data = data
        self.next = None


class Linked_List:
    def __init__ (self):
        #Linked list stores a pointer to the first item in the list called the head.
        self.head = None
        #storing a pointer to the last item in the list makes adding a new node to the end O(1) instead of O(n) complexity.
        self.tail = None
    
    def add_new_node (self,data):
        #if it's the first item in the list
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
            return
        
        #if there are already items on the list
        new = Node(data)
        self.tail.next = new
        self.tail = new
        
    def add_node_to_head (self,data):
        #if it's the first item in the list.
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
            return
        #if there are already items on the list
        new = Node(data)
        new.next = self.head
        self.head = new
        
    def delete_node (self,target): #delete the first instance found
        if self.head.data == target: #if target is first node - edge case
            if self.head.next: #and list is longer than one
                self.head = self.head.next #send old self.head to garbage collector.
            else: #or list is only one element
                self.head = None #reset list
        
        else: #target is not first node - main case
            previous = self.head
            current = self.head.next
            while current:
                if current.data == target:
                    if not current.next : self.tail = current
                    previous.next = current.next
                    return
                previous = current
                
                
        
       
        
    
            
    
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

x.add_node_to_head(6)

x.print_list()




