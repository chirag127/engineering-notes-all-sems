### Skip List

A skip list is a probabilistic data structure that allows for efficient search, insertion, and deletion operations. It is an alternative to balanced binary search trees, such as red-black trees and AVL trees.

Here are some key points to remember about skip lists:

1. A skip list is composed of multiple layers of linked lists, with each layer containing a subset of the elements in the layer below it.
2. The bottom layer contains all the elements in the skip list, in sorted order.
3. Each element in the skip list has a certain number of "towers" or "levels" that point to elements further along in the list.
4. The number of levels for each element is determined randomly, with the probability of an element having k levels being 1/2^k.
5. To search for an element in a skip list, we start at the top level and move along the list until we find an element that is greater than or equal to the target element. We then move down one level and repeat the process until we reach the bottom level, where we can find the target element if it exists in the list.
6. Insertion and deletion operations are performed in a similar manner, by first searching for the position where the element should be inserted or deleted, and then updating the pointers in the levels above it.

Skip lists have an average-case time complexity of O(log n) for search, insertion, and deletion operations, making them an efficient choice for many applications. They are also relatively simple to implement and can be easily adapted to support additional operations such as range queries and order statistics. However, their performance can vary due to their probabilistic nature, and they may not always provide the same level of performance as balanced binary search trees.