### Skip List

A skip list is a data structure that allows for efficient search, insertion and deletion of elements in a sorted list. It is a probabilistic data structure, meaning that its average time complexity is determined through a probabilistic analysis .

- A skip list consists of multiple layers of linked lists, with each layer having a smaller number of elements than the previous one.
- The bottom layer contains all the elements of the sorted list, and the top layer contains only a few elements that act as shortcuts for faster traversal.
- Each element in a layer has a pointer to the next element in the same layer, and a pointer to the element below it in the lower layer.
- The elements in the higher layers are chosen randomly with some probability, such that the expected number of elements in each layer is half of the previous one.
- The skip list has a special element called the head, which is present in all the layers and points to the first element of each layer. It also has a special element called the tail, which is present in all the layers and points to null.
- The skip list also has a variable called the level, which stores the current number of layers in the skip list.

The following image shows an example of a skip list with four layers:

![skip list example](https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Skip_list.svg/800px-Skip_list.svg.png)

- To search for an element in a skip list, we start from the head of the top layer and compare the element with the next element in the same layer. If the element is smaller, we move to the next element. If the element is larger, we move down to the lower layer and repeat the process. If the element is equal, we have found the element. If we reach the bottom layer and the element is not found, we conclude that the element is not in the list.
- To insert an element in a skip list, we first search for the element and find the position where it should be inserted in the bottom layer. Then, we create a new node with the element and insert it in the bottom layer. Next, we toss a coin and decide whether to insert the element in the next higher layer or not. If the coin is heads, we insert the element in the next higher layer and repeat the coin toss. If the coin is tails, we stop the insertion. If we reach the top layer and the coin is still heads, we create a new layer and insert the element in it, and update the level of the skip list.
- To delete an element from a skip list, we first search for the element and find all the nodes that contain it in different layers. Then, we remove all the nodes that contain the element and update the pointers of the previous and next nodes. If the top layer becomes empty after the deletion, we remove the top layer and update the level of the skip list.

The following are some advantages and disadvantages of skip lists:

- Advantages:
  - Skip lists are simpler to implement than balanced trees, and use less space.
  - Skip lists can handle dynamic insertion and deletion of elements without rebalancing the structure.
  - Skip lists can support range queries and ordered operations efficiently.
- Disadvantages:
  - Skip lists are probabilistic, meaning that their performance is not guaranteed in the worst case.
  - Skip lists require extra space for storing the pointers and the random number generator.
  - Skip lists are sensitive to the choice of the probability parameter, which affects the balance and the height of the structure.

The following are some applications and variations of skip lists:

- Applications:
  - Skip lists can be used to implement sorted sets and maps, which support fast lookup, insertion and deletion of key-value pairs.
  - Skip lists can be used to implement priority queues, which support fast insertion and extraction of elements with different priorities.
  - Skip lists can be used to implement concurrent data structures, which allow multiple threads to access and modify the structure without locking.
- Variations:
  - Deterministic skip lists, which use a deterministic rule to decide the height of each element, instead of a random coin toss.
  - Indexable skip lists, which allow fast access to the element at a given rank or position in the sorted list.
  - Multi-level skip lists, which use multiple skip lists with different probability parameters to achieve better performance.
  - Skip graphs, which extend skip lists to support distributed and dynamic data structures.

: Skip list - Wikipedia
: Skip List | Set 1 (Introduction) -