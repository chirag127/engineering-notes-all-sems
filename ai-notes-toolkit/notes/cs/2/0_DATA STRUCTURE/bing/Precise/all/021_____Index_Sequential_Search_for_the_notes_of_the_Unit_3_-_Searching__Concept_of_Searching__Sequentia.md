### Index Sequential Search

Index Sequential Search is a search algorithm that combines the principles of a sequential search and an index search. It is used to search for a specific element in a large, ordered list of elements. The algorithm works by dividing the list into smaller sublists, each of which is indexed. The index is used to determine the sublist in which the desired element is likely to be found. Once the sublist is identified, a sequential search is performed within that sublist to locate the desired element.

The steps involved in an Index Sequential Search are as follows:

1. Create an index for the list by dividing it into smaller sublists and storing the first element of each sublist in the index.
2. Use the index to determine the sublist in which the desired element is likely to be found.
3. Perform a sequential search within the identified sublist to locate the desired element.

Index Sequential Search is more efficient than a simple sequential search as it reduces the number of elements that need to be searched. However, it is less efficient than a binary search, which has a lower time complexity.