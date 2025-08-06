#todo

#delete all instances of a value
#doubly linked list or circular list

class Node:
    def __init__ (self,data):
        #a node holds data and a pointer to the next node
        self.data = data
        self.next = None

class Linked_List:
    def __init__ (self):
        #A pointer to the first item in the list called the head.
        self.head = None
        #A pointer to the last item in the list makes adding a new node to the end O(1) instead of O(n) complexity.
        self.tail = None
    
    def add_new_node (self,data):
        #if it's the start of the list
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
            return
        
        #if there are already items on the list
        new = Node(data)
        self.tail.next = new
        self.tail = new
        
    def add_node_to_head (self,data):
        #if it's the start of the list
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
            return
        #if there are already items on the list
        new = Node(data)
        new.next = self.head
        self.head = new
        
    def delete_node (self,target): #deletes first instance found
        if self.head is None: #if list is empty 
            return False
        if self.head.data == target: #if target is first node
            if self.head.next: #handle list is longer than one
                self.head = self.head.next #unreference the old self.head
            else: #or list is only one element
                self.head = None #reset list
                self.tail = None
            return True
        else: #if target is not first node 
            previous = self.head
            current = self.head.next
            while current: #traverse list
                if current.data == target: #match found
                    if not current.next: #if match is last in the list
                        self.tail = previous #reset tail
                        previous.next = None 
                        return True
                    previous.next = current.next #skip over current (match)
                    return True
                previous = current #keep track of previous
                current = current.next #move on to the next one
            return False#no match found   

    def search_for_value (self, target): #return true or false if it exists
        if self.head is None: #if list is empty 
            return False
        if self.head.data == target: #if first node is match
            return True
        if self.head.next: #if second node exists
            current = self.head.next
        else:
            return False
        while current: #traverse list
            if current.data == target:
                return True
        return False
        

    def print_list (self):
        #traverse the list starting with the head
        current = self.head
        #keep going until there is no current
        while current:
            print (current.data)
            current = current.next

        

x = Linked_List()




