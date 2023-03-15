### Sequential Search

Sequential search, also known as linear search, is a method of searching for a target value within a list. It sequentially checks each element of the list for the target value until a match is found or until all the elements have been searched.

The steps involved in a sequential search are as follows:
1. Start from the first element of the list.
2. Compare the current element with the target value.
3. If the current element matches the target value, return the index of the current element.
4. If the current element does not match the target value, move to the next element and repeat step 2.
5. If the end of the list is reached and the target value is not found, return -1 to indicate that the target value is not present in the list.

The time complexity of sequential search is O(n) in the worst case, where n is the number of elements in the list. This means that the time taken to search for a target value increases linearly with the size of the list.

Sequential search is a simple and intuitive search algorithm, but it is not efficient for large lists. Other search algorithms, such as binary search and hash-based search, can be more efficient for large lists. However, sequential search can be useful in certain situations, such as when the list is small or when the list is not sorted and cannot be sorted easily.