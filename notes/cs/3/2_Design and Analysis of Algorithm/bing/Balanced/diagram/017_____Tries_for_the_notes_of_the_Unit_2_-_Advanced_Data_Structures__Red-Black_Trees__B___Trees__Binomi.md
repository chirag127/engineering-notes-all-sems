### Tries

- A trie is a tree-based data structure used for storing and retrieving collections of strings .
- The word trie comes from the word re**TRIE**val which means to find or get something back.
- A trie is also called a digital tree or a prefix tree.
- A trie is a type of k-ary search tree, where each node has k children, one for each character in the alphabet.
- If two strings have a common prefix, then they will have the same ancestor in the trie.
- The root node of the trie represents an empty string.
- Each node in the trie has two fields: a value and an array of pointers to its children.
- The value field can store any data associated with the string represented by the node.
- The array of pointers has a fixed size equal to the size of the alphabet.
- Each pointer in the array corresponds to a character in the alphabet.
- If a node has a child for a character, then the pointer at that index is not null.
- If a node does not have a child for a character, then the pointer at that index is null.
- A node is a leaf node if all its pointers are null.
- A node is a terminal node if it represents the end of a string.
- A terminal node may or may not be a leaf node.
- A trie can support two main operations: insert and search.
- To insert a string into a trie, we start from the root node and follow the pointers corresponding to the characters in the string.
- If a pointer is null, we create a new node and link it to the parent node.
- If a pointer is not null, we move to the next node and repeat the process.
- When we reach the end of the string, we mark the last node as a terminal node and optionally store some value in it.
- To search for a string in a trie, we start from the root node and follow the pointers corresponding to the characters in the string.
- If a pointer is null, we return false, as the string is not in the trie.
- If a pointer is not null, we move to the next node and repeat the process.
- When we reach the end of the string, we check if the last node is a terminal node.
- If the last node is a terminal node, we return true, as the string is in the trie.
- If the last node is not a terminal node, we return false, as the string is a prefix of some other string in the trie.
- The time complexity of both insert and search operations is O(m), where m is the length of the string.
- The space complexity of a trie is O(nk), where n is the number of strings and k is the size of the alphabet.
- A trie can be used for various applications, such as autocomplete, spell checking, prefix matching, word search, etc  .

Here is an example of a trie that stores the strings "allot", "alone", "ant", "and", "are", "bat", and "bad":

```
    root
    /  \
   a    b
  / \    \
 l   n    a
/ \   \    \
l  o   t    t
|  |   |   / \
o  n   *  a   d
|  |      |   |
t  d      r   *
|  |      |  
*  *      e
         |
         *
```

The asterisks (*) denote the terminal nodes. The value field of each node is omitted for simplicity.