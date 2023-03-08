 Here is the content in markdown format for the given topic:

### Data structure for symbols tables for the notes of the Unit 4 - Symbol Tables in the subject of Compiler Design

The following are the common data structures used to implement symbol tables in compilers:

1. Linear/Sequential list:
- In this, the symbols are stored sequentially in a list.
- Searching is done sequentially by comparing each symbol with the input.
- The advantage is simplicity. The disadvantage is that the search time increases linearly with the number of symbols.
- This data structure is suitable for a small number of symbols.

2. Hash Table:
- In this, each symbol is hashed to a bucket/chain using a hash function.
- Searching is done by applying the hash function to the input and checking only the corresponding bucket/chain.
- The advantage is faster search time which is independent of the number of symbols. The disadvantage is that collision resolution is required when two symbols hash to the same location.
- This data structure is suitable for a large number of symbols.

3. Binary Search Tree:
- In this, the symbols are stored in a binary tree structure based on some ordering (alphabetic, numeric, etc).
- Searching is done by traversing the tree which takes logarithmic time.
- The advantage is the fast logn search time. The disadvantage is that insertion/deletion may take longer time and the tree can become unbalanced.
- This data structure is suitable for a sorted set of symbols.

[Include diagrams, examples, codes, advantages, disadvantages, applications, etc if any to help learn the topic]

The choice of data structure depends on the number of symbols, whether the symbols are sorted or not, search time requirements, insertion/deletion time requirements, etc. The compiler designer can choose an appropriate data structure based on the conditions and requirements of the application.