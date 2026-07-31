### Skip List

- A skip list is a **probabilistic data structure** that allows for efficient search, insertion and deletion of elements in a **sorted list** .
- A skip list consists of multiple **layers** of linked lists, with each layer having a smaller number of elements than the previous one .
- The lowest layer contains all the elements of the sorted list, and the highest layer contains only one element, the **head** .
- Each element in a skip list has a **key** and a **value**, and a variable number of **forward pointers** to the next elements in the same or higher layers .
- The number of forward pointers of each element is determined randomly by a **coin toss** or a **geometric distribution**, such that the expected number of elements in each layer is half of the previous one .
- To search for an element in a skip list, we start from the head in the highest layer, and follow the forward pointers until we find a key that is larger than or equal to the target key .
- Then, we move down to the next lower layer, and repeat the process until we reach the lowest layer .
- If we find the target key in the lowest layer, we return the corresponding value, otherwise we return null .
- The expected time complexity of search in a skip list is **O(log n)**, where n is the number of elements in the sorted list .
- To insert an element in a skip list, we first search for the position where the element should be inserted in the lowest layer, and then insert it there .
- Then, we toss a coin to decide whether to insert the element in the next higher layer as well .
- We repeat this process until the coin toss returns tails or we reach the highest layer .
- The expected time complexity of insertion in a skip list is also **O(log n)** .
- To delete an element from a skip list, we first search for the element in the lowest layer, and then delete it from there .
- Then, we move up to the next higher layer, and delete the element from there if it exists .
- We repeat this process until we reach the highest layer or the element does not exist in the current layer .
- The expected time complexity of deletion in a skip list is also **O(log n)** .
- Skip lists are a simple, fast and space-efficient alternative to balanced trees for implementing ordered sequences .
- Skip lists can also support concurrent operations by using **locks** or **atomic operations** on the forward pointers .
- Skip lists can also be extended to support **range queries**, **multidimensional data**, **approximate queries**, and other applications .

: Skip list - Wikipedia
: Skip List | Set 1 (Introduction) - GeeksforGeeks
: Skip List | Brilliant Math & Science Wiki
: The Skip List Data Structure | Baeldung on Computer Science