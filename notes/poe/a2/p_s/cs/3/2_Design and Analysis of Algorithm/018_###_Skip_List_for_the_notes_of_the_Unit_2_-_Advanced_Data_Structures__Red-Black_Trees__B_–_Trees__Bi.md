 Here are the notes for Skip List in markdown format:

### Skip List

- A skip list is a data structure that consists of several layers of lists. 
- Each layer contains the same elements, but reorganized to speed up searching. 
- Elements are inserted and deleted at the same cost as in a regular linked list. 
- However, search has an expected logarithmic complexity, much faster than a regular linked list which has linear complexity.

Advantages:
- Faster search than a regular linked list with expected O(log n) time complexity.
- Simple and efficient implementation. Insertion and deletion have O(log n) time complexity.
- Dynamic – can grow and shrink efficiently.

Disadvantages:
- Wastes more space than a regular linked list since elements are present in multiple lists.
- Search time is not guaranteed – only has an expected logarithmic time complexity. In the worst case, search can degenerate to O(n) time.

How it works:
- A skip list consists of layers of sorted linked lists. 
- The bottom-most layer contains all elements. Higher layers contain subsets of elements from the layer below.
- Each layer uses a randomized algorithm to determine if an element should be included in that layer. Elements at higher layers are more "sparse".
- Search starts at the top layer and proceeds downwards. If the element is not found in a layer, the next layer down is searched. This leads to the expected logarithmic complexity.

Diagrams and codes can be included here to help understand the concept better. Applications of skip lists include database indexes and cache optimization.