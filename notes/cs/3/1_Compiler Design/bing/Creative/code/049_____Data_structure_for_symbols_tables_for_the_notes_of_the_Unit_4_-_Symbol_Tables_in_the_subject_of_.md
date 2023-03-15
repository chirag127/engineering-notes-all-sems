### Data structure for symbol tables

- A symbol table is an important data structure created and maintained by compilers in order to store information about the occurrence of various entities such as variable names, function names, objects, classes, interfaces, etc. 
- A symbol table is used by both the analysis and the synthesis parts of a compiler. 
- A symbol table can be implemented using different data structures, such as linear lists, binary search trees, or hash tables. 
- The choice of data structure depends on various factors, such as the size of the symbol table, the frequency of insertions and deletions, the type of operations performed on the symbol table, and the complexity of the hashing function. 
- Some of the advantages and disadvantages of different data structures for symbol tables are:

  - Linear lists: They are the simplest and most straightforward method of implementing symbol tables. They use a single array to store names and their accompanying information. New names are added to the list in the order that they appear. 
    - Advantages: Easy to implement and understand. No need for a hashing function. 
    - Disadvantages: Slow search, insertion, and deletion operations. The list may grow too large and require resizing. The list may contain duplicate entries. 
  - Binary search trees: They are a type of ordered data structure that store names and their accompanying information in a tree-like structure. Each node of the tree has a key (the name) and a value (the information). The left subtree of a node contains nodes with keys smaller than the node's key, and the right subtree contains nodes with keys larger than the node's key. 
    - Advantages: Fast search, insertion, and deletion operations. No need for a hashing function. No duplicate entries. 
    - Disadvantages: Complex to implement and maintain. The tree may become unbalanced and degrade the performance. The tree may require a lot of memory. 
  - Hash tables: They are a type of unordered data structure that store names and their accompanying information in an array of buckets. Each bucket contains a list of entries with the same hash value. A hash value is a numerical representation of a name, computed by a hashing function. The hashing function maps names to buckets in a uniform and random manner. 
    - Advantages: Fast search, insertion, and deletion operations. Efficient use of memory. 
    - Disadvantages: Need for a good hashing function that minimizes collisions. Collisions occur when two or more names have the same hash value and are mapped to the same bucket. Collisions increase the search time and the size of the bucket lists.