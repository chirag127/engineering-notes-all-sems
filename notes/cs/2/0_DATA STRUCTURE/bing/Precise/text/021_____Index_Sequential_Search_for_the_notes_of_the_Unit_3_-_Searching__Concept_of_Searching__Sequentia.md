### Index Sequential Search

Index Sequential Search is a search algorithm that combines the principles of a sequential search and an index search. It is used to search for a specific element in a large, ordered list of elements. The algorithm works by dividing the list into smaller sub-lists, each of which is indexed. The index is used to determine the sub-list in which the desired element is most likely to be found. Once the sub-list is identified, a sequential search is performed within that sub-list to locate the desired element.

The steps involved in an Index Sequential Search are as follows:

1. Create an index for the list, which is a smaller list containing the first element of each sub-list.
2. Use a binary search on the index to determine the sub-list in which the desired element is most likely to be found.
3. Perform a sequential search within the identified sub-list to locate the desired element.

Index Sequential Search is more efficient than a simple sequential search, as it reduces the number of elements that need to be searched. However, it is less efficient than a binary search, as it still involves a sequential search within the identified sub-list. The efficiency of an Index Sequential Search can be improved by choosing an appropriate size for the sub-lists and by keeping the index up-to-date as the list changes.