### Skip List

A skip list is a probabilistic data structure that allows for efficient search, insertion, and deletion operations. It is an alternative to balanced binary search trees such as red-black trees and AVL trees.

Here are some key points to remember about skip lists:

- A skip list is composed of multiple layers of linked lists.
- Each layer is a subset of the layer below it, with the bottom layer containing all the elements in the list.
- The higher the layer, the fewer elements it contains, and the larger the gaps between the elements.
- The top layer contains only a few elements, which allows for fast search operations.
- Elements are inserted into the skip list by randomly choosing the number of layers in which the element will appear.
- The probability of an element appearing in a higher layer decreases exponentially as the layer number increases.
- The expected number of layers in a skip list is logarithmic in the number of elements in the list.
- The expected time complexity for search, insertion, and deletion operations in a skip list is O(log n), where n is the number of elements in the list.
