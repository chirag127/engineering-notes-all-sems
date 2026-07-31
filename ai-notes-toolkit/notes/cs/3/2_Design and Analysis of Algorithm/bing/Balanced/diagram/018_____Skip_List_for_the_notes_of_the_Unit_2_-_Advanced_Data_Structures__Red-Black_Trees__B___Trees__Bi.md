### Skip List

A skip list is a data structure that allows for efficient search, insertion and deletion of elements in a sorted list. It is a probabilistic data structure, meaning that its average time complexity is determined through a probabilistic analysis .

- A skip list consists of multiple layers of linked lists, with each layer having a smaller number of elements than the previous one.
- The lowest layer contains all the elements of the list in sorted order, and is called the base list.
- The higher layers contain a subset of the elements of the lower layers, chosen randomly with some probability.
- Each element in a layer has a pointer to the next element in the same layer, and a pointer to the corresponding element in the lower layer.
- The highest layer contains only one element, called the head, which points to the first element of the base list.
- The skip list also has a tail element, which points to the last element of the base list.

![Skip list example](https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Skip_list.svg/800px-Skip_list.svg.png)

- The main advantage of a skip list is that it allows for fast search, insertion and deletion operations, with an expected time complexity of O(log n), where n is the number of elements in the base list.
- The search operation starts from the head element and follows the pointers in the highest layer until it reaches an element that is larger than or equal to the target element, or the tail element.
- Then, it moves down to the lower layer and repeats the process until it reaches the base list, where it either finds the target element or determines that it does not exist in the list.
- The insertion operation first searches for the position where the new element should be inserted in the base list, and then randomly decides whether to insert it in the higher layers as well, with some probability.
- The deletion operation first searches for the element to be deleted in the base list, and then removes it from all the layers where it appears, updating the pointers accordingly.

- The main disadvantage of a skip list is that it requires extra space to store the pointers in the higher layers, and that it is sensitive to the choice of the probability parameter, which affects the balance and performance of the structure.
- The skip list is a probabilistic data structure that seems likely to supplant balanced trees as the implementation method of choice for many applications. Skip list algorithms have the same asymptotic expected time bounds as balanced trees and are simpler, faster and use less space.