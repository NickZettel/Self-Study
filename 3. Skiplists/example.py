class skiplist:
    def __init__ (self):
        self.heads = [] #stores the heads of all layers, starting from highest

class linked_list:
    def __init__ (self):
        self.start = None
        self.tail = None
        self.contents = []
        
class quad_node:
    def __init__ (self):
        self.next = None
        self.previous = None
        self.above = None #above link is optional, but speeds up fast removals from a known node
        self.below = None
        