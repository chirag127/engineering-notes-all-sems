# Tries

- A trie is a tree-based data structure used for storing and retrieving collections of strings .
- The word trie comes from the word re**TRIE**val which means to find or get something back.
- A trie is also called a digital tree or a prefix tree.
- A trie is a type of k-ary search tree, where each node has at most k children, and each child corresponds to a character of the alphabet.
- A trie can store any string over a finite alphabet, such as the English alphabet, ASCII characters, or binary digits.
- A trie can perform the following operations efficiently:
  - Insertion: To insert a string into a trie, we start from the root and follow the path corresponding to the characters of the string. If the path does not exist, we create new nodes along the way. We mark the last node as the end of the string.
  - Search: To search for a string in a trie, we start from the root and follow the path corresponding to the characters of the string. If the path exists and the last node is marked as the end of the string, we return true. Otherwise, we return false.
  - Prefix search: To search for all the strings that have a given prefix in a trie, we start from the root and follow the path corresponding to the prefix. If the path exists, we traverse the subtree rooted at the last node and collect all the strings that end at a marked node.
- A trie has the following advantages over a hash table:
  - A trie can handle collisions better than a hash table, as there is no need for hashing or rehashing.
  - A trie can support prefix search and pattern matching, which are not possible with a hash table.
  - A trie can save space by sharing common prefixes among strings, whereas a hash table requires a separate entry for each string.
- A trie has the following disadvantages compared to a hash table:
  - A trie may require more space than a hash table if the strings have few common prefixes or the alphabet is large.
  - A trie may require more time than a hash table to access a string if the string is long or the trie is deep.
  - A trie may be more complex to implement than a hash table.