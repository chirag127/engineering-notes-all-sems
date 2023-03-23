 Here are the notes for Skip List in Markdown format:

### Skip List

- Skip lists are a data structure that can be used to implement an ordered list (like a binary search tree) with efficient search, insert, and delete operations that take O(log n) time.
- Skip lists are a probabilistic data structure, meaning that the efficiency of operations depends on a random choice (coin flips), but the expected efficiency is O(log n).
- A skip list consists of levels of lists. The bottom-most list contains all elements. Higher levels contain only selected elements (based on random coin flips), and elements at higher levels are less dense. This allows search operations to skip large portions of the list at higher levels, giving the data structure its name.
- Searching starts at the top level. If the search key is greater than the node at the current level, move down to the next level. Otherwise, move to the next node at the current level. This is repeated until a match is found or the bottom level is reached.
- Insertion is similar. The level at which an element is inserted is chosen randomly. If the coin flip is heads, the element is inserted at the current level. This is repeated until the bottom level is reached or a flip results in tails.
- Deletion is similar to search, removing elements at matching locations. If an element at a higher level is deleted, subsequent search and insert operations may be slightly less efficient due to the less dense higher levels.
- The expected efficiency of skip list operations is O(log n), but the constant factors are higher than for binary search trees. Skip lists are a simpler data structure, however, and may have better cache performance.