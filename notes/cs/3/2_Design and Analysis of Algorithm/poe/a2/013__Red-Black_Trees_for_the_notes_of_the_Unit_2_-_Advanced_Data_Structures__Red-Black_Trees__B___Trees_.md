 Here are the notes on Red-Black Trees in a formal style:

### Red-Black Trees

- Red-Black Trees are self-balancing binary search trees.
- They have the following properties:
    - Every node is either red or black.
    - The root is always black.
    - Every red node must have two black child nodes.
    - Every path from a given node to its descendant leaves contains the same number of black nodes.
- The properties ensure that the tree remains balanced, as the longest path cannot exceed twice the length of the shortest path. This leads to O(log n) time for insertion, deletion and search, similar to a binary search tree.
- To insert a node:
    - Insert the node as in a binary search tree.
    - If the inserted node is red and its parent is also red, repaint the parent black and grandparent red (if the grandparent exists). Repeat until the root or a black node is reached. This ensures the properties are maintained.
- To delete a node:
    - First swap values with the node's successor and delete the successor.
    - Then, if the node to be deleted was black and its successor was red, repaint the successor black and perform rotations/repaints as required to maintain the properties.
- Overall, the trick is to ensure the properties are maintained after every insertion/deletion through a series of rotations and repaints. This ensures the tree remains balanced leading to logarithmic time complexities for all operations.