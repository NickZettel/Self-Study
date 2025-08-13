### Linked Lists

A data structure where each element has two parts, the content and a pointer to the next element in the list. Unlike arrays they don't require contiguous memory.

### Core Operations

Insert at head O(1)
Insert at tail O(1)/O(n)
Insert at index O(n)
Search O(n)
Delete Node O(n)

### Summary
Scatters elements about in chunks of memory which may be useful if memory is fragmented. Not ideal when random access is needed since accessing a specific index requires traversing the list. Inserting at the tail is O(n) complexity if you don't have a pointer to that. If you do have a pointer it's O(1)