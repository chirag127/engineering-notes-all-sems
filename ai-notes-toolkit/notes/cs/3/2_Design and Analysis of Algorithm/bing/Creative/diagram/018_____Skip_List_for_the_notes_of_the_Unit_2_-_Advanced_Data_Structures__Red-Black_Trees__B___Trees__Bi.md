### Skip List

A skip list is a data structure that allows for efficient search, insertion and deletion of elements in a sorted list. It is a probabilistic data structure, meaning that its average time complexity is determined through a probabilistic analysis.  

- A skip list consists of multiple layers of linked lists, with each layer having a smaller number of elements than the previous one.
- The bottom layer contains all the elements of the sorted list, and the top layer contains only one element, the smallest one.
- Each element in a layer has a pointer to the next element in the same layer, and a pointer to the element below it in the lower layer.
- The elements in each layer are chosen randomly, with a fixed probability of being included or skipped.
- The probability of an element being included in a layer is usually 1/2, meaning that each layer has half the elements of the previous one on average.
- The number of layers in a skip list is also random, but it is bounded by log(n), where n is the number of elements in the bottom layer.
- The height of a skip list is the number of layers it has.

The following diagram illustrates the structure of a skip list:

```
+---+   +---+   +---+   +---+
| 1 |-->| 3 |-->| 7 |-->| 9 |
+---+   +---+   +---+   +---+
  |       |       |       |
  v       v       v       v
+---+   +---+   +---+   +---+   +---+   +---+   +---+   +---+   +---+
| 1 |-->| 2 |-->| 3 |-->| 4 |-->| 5 |-->| 6 |-->| 7 |-->| 8 |-->| 9 |
+---+   +---+   +---+   +---+   +---+   +---+   +---+   +---+   +---+
```

The main operations on a skip list are:

- Search: To search for an element x in a skip list, we start from the top left corner and follow the pointers until we find x or reach the end of the list. If the current element is smaller than x, we move to the next element in the same layer. If the current element is larger than x, we move to the element below it in the lower layer. If the current element is equal to x, we return it. The expected time complexity of search is O(log(n)).
- Insertion: To insert an element x in a skip list, we first search for x and find the position where it should be inserted. Then, we create a new node with x and insert it in the bottom layer. Next, we toss a coin and decide whether to insert x in the next layer or not. We repeat this process until we reach the top layer or the coin toss is negative. If we reach the top layer and the coin toss is positive, we create a new layer with x as the only element. The expected time complexity of insertion is O(log(n)).
- Deletion: To delete an element x from a skip list, we first search for x and find the node that contains it. Then, we delete the node from all the layers where it appears, and update the pointers accordingly. If the top layer becomes empty, we delete it as well. The expected time complexity of deletion is O(log(n)).   

Some advantages of skip lists are:

- They are simpler and faster than balanced trees, and use less space.
- They are easy to implement and modify, and can support concurrent operations.
- They can handle dynamic insertion and deletion of elements without rebalancing.
- They can be used to implement other data structures, such as dictionaries, sets, and priority queues.   

Some disadvantages of skip lists are:

- They are probabilistic, meaning that their performance is not guaranteed in the worst case.
- They require extra space for storing the pointers and the random numbers.
- They are sensitive to the choice of the probability parameter, which affects the height and the balance of the list.