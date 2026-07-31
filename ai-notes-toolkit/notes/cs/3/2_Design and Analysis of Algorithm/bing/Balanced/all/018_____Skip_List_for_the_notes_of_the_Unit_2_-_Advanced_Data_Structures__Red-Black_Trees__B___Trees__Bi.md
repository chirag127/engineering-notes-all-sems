# Skip List

A skip list is a data structure that allows for efficient search, insertion and deletion of elements in a sorted list. It is a probabilistic data structure, meaning that its average time complexity is determined through a probabilistic analysis .

## Basic Idea

- A skip list is composed of several layers of linked lists, with each layer having a smaller number of elements than the previous one.
- The lowest layer contains all the elements of the sorted list, and is called the base list.
- The higher layers contain a subset of the elements of the lower layers, and are called the skip lists.
- Each element in a skip list has a pointer to the next element in the same layer, and a pointer to the element below it in the lower layer.
- The highest layer contains only one element, called the head, which points to the first element of each layer.
- To search for an element in a skip list, we start from the head and follow the pointers in the highest layer until we find an element that is larger than or equal to the target element. Then, we move down to the lower layer and repeat the process until we reach the base list. If we find the target element in the base list, we return it. Otherwise, we return null.
- To insert an element in a skip list, we first search for the position where it should be inserted in the base list. Then, we insert it in the base list and randomly decide whether to promote it to the higher layer. If we promote it, we repeat the process until we reach the highest layer or we decide not to promote it. We also update the pointers of the elements around the inserted element accordingly.
- To delete an element from a skip list, we first search for it in the base list. If we find it, we delete it from the base list and all the higher layers where it appears. We also update the pointers of the elements around the deleted element accordingly.

## Complexity Analysis

- The expected time complexity of search, insertion and deletion in a skip list is O(log n), where n is the number of elements in the base list. This is because the expected number of elements in each layer is half of the number of elements in the lower layer, and the expected number of layers is O(log n).
- The expected space complexity of a skip list is O(n), where n is the number of elements in the base list. This is because the expected number of elements in all the layers is O(n).
- The worst-case time complexity of search, insertion and deletion in a skip list is O(n), where n is the number of elements in the base list. This is because the worst-case number of elements in each layer is n, and the worst-case number of layers is n.
- The worst-case space complexity of a skip list is O(n^2), where n is the number of elements in the base list. This is because the worst-case number of elements in all the layers is O(n^2).

## Advantages and Disadvantages

- Some advantages of skip lists are:
  - They are simpler to implement than balanced trees, such as red-black trees or B-trees.
  - They are faster and use less space than balanced trees in practice.
  - They are easy to parallelize and support concurrent operations.
- Some disadvantages of skip lists are:
  - They are probabilistic and have a high variance in performance.
  - They require random number generation, which may be costly or insecure.
  - They are not widely supported by standard libraries or languages.