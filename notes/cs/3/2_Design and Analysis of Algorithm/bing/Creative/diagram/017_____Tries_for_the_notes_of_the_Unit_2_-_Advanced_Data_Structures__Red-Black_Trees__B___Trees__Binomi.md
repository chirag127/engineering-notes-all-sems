### Tries

- A trie is a tree-based data structure used for storing and retrieving collections of strings .
- The word trie comes from the word re**TRIE**val which means to find or get something back.
- A trie is also called a digital tree or a prefix tree.
- A trie is a type of k-ary search tree, where each node has k children, one for each character in the alphabet.
- A trie can store any string that can be constructed from the alphabet.
- A trie can perform the following operations efficiently  :
  - Insert: To add a new string to the trie, we start from the root and follow the path corresponding to the characters of the string. If the path does not exist, we create new nodes along the way. We mark the last node as the end of the string.
  - Search: To search for a string in the trie, we start from the root and follow the path corresponding to the characters of the string. If the path exists and the last node is marked as the end of the string, we return true. Otherwise, we return false.
  - Delete: To delete a string from the trie, we first search for the string. If the string is not found, we do nothing. If the string is found, we unmark the last node as the end of the string. Then, we delete the nodes from the bottom up, until we reach a node that has more than one child or is the root.
  - Prefix Matching: To find all the strings that have a given prefix, we start from the root and follow the path corresponding to the prefix. If the path exists, we traverse the subtree rooted at the last node of the prefix and collect all the strings that are marked as the end of the string.
- A trie has the following advantages over a hash table :
  - A trie can handle collisions better than a hash table, as there is no need for a hash function or a chaining mechanism.
  - A trie can support prefix matching, which is not possible with a hash table.
  - A trie can save space by sharing common prefixes among the strings, whereas a hash table requires a separate entry for each string.
- A trie has the following disadvantages over a hash table :
  - A trie can consume more space than a hash table, as it requires a node for each character in the alphabet, even if the node is not used.
  - A trie can be slower than a hash table, as it requires traversing multiple nodes to perform an operation, whereas a hash table can access an entry in constant time.