### Linked Lists

A data structure that uses layers of linked lists stacked on top of each other. The bottom layer contains all nodes in the list. For each of these nodes, a coinflip is performed, and if the result is heads the node is added to the layer above. If it is tails, it is not. This is repeated for all the layers above, resulting in a pyramid shaped structure.
