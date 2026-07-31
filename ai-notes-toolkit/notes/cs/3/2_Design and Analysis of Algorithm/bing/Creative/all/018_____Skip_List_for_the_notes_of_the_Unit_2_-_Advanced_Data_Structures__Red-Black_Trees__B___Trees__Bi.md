# Skip List

A skip list is a data structure that allows for efficient search, insertion and deletion of elements in a sorted list. It is a probabilistic data structure, meaning that its average time complexity is determined through a probabilistic analysis.  

## Basic Idea

- A skip list is composed of multiple layers of linked lists, with each layer having a smaller number of elements than the previous one.
- The bottom layer contains all the elements of the sorted list, and the top layer contains only a few elements that act as shortcuts or entry points to the lower layers.
- Each element in a layer has a pointer to the next element in the same layer, and a pointer to the element below it in the lower layer.
- To search for an element in a skip list, we start from the top layer and follow the pointers until we find an element that is larger than or equal to the target element. Then, we move down to the lower layer and repeat the process until we reach the bottom layer, where we can find the exact element or determine that it does not exist in the list.
- To insert an element in a skip list, we first search for its position in the bottom layer, and then insert it there. Then, we toss a coin to decide whether to promote the element to the higher layer or not. If the coin lands on heads, we promote the element and repeat the coin toss for the next layer. If the coin lands on tails, we stop the promotion. This way, we ensure that each layer has a smaller number of elements than the previous one, and that the probability of an element being in a layer is inversely proportional to the layer number.
- To delete an element from a skip list, we first search for it in the bottom layer, and then delete it from there. Then, we delete it from all the higher layers where it appears, by updating the pointers of the previous and next elements in each layer.

## Advantages and Disadvantages

- Skip lists have the same asymptotic expected time complexity as balanced trees for search, insertion and deletion operations, which is O(log n), where n is the number of elements in the list.  
- Skip lists are simpler, faster and use less space than balanced trees, as they do not require any rotation or rebalancing operations. 
- Skip lists are easy to implement and modify, as they only require basic operations on linked lists. 
- Skip lists are suitable for concurrent applications, as they allow multiple threads to access and modify different parts of the list without locking or synchronization. 
- Skip lists are probabilistic data structures, meaning that their performance depends on the random choices made during insertion and promotion. This can lead to some worst-case scenarios, where the skip list becomes unbalanced or inefficient. However, these scenarios are very unlikely to occur, and can be avoided by using appropriate parameters and techniques.  
- Skip lists require extra space to store the pointers for each layer, which can be significant if the number of layers is large.  

## References

: Skip list - Wikipedia
: Skip List | Set 1 (Introduction) - GeeksforGeeks
: Skip List | Brilliant Math & Science Wiki
: The Skip List Data Structure | Baeldung on Computer Science