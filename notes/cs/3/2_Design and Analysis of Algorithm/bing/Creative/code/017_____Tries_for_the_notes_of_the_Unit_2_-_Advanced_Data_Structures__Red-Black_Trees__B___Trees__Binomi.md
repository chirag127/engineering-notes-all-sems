Hello, I am Sydney, your AI assistant. I will help you with your query. Here are some notes on the topic of tries data structure:

### Tries

- A trie is a tree-based data structure used for storing and retrieving collections of strings over an alphabet  .
- The word trie comes from the word re**TRIE**val which means to find or get something back .
- A trie is also called a prefix tree because every node in the trie represents a common prefix of the strings that belong to its subtree  .
- A trie has the following properties  :
  - The root node is associated with an empty string.
  - Each edge is labeled with a character from the alphabet.
  - Each node, except the root, is associated with the string formed by concatenating the characters along the path from the root to that node.
  - No two edges out of a node can have the same character.
  - A node is a terminal node if it represents the end of a string in the collection.
- A trie can support the following operations  :
  - Insert: To insert a string into the trie, we start from the root and follow the path corresponding to the characters of the string. If the path does not exist, we create new nodes and edges as needed. We mark the last node as a terminal node.
  - Search: To search for a string in the trie, we start from the root and follow the path corresponding to the characters of the string. If the path exists and the last node is a terminal node, we return true. Otherwise, we return false.
  - Delete: To delete a string from the trie, we first search for the string. If the string is not present, we do nothing. If the string is present, we mark the last node as a non-terminal node. Then, we delete any nodes and edges that are not part of any other string in the trie.
- A trie can be used for various applications, such as:
  - Predictive text or autocomplete dictionaries
  - Approximate matching algorithms
  - Spell checking and hyphenation applications
  - Longest prefix match algorithms
- A trie has some advantages over a hash table, such as :
  - Faster searches
  - Less space, especially when the set contains large number of short strings
  - No collisions or hashing functions required
  - Easy to find and sort strings by prefix
- A trie also has some disadvantages, such as :
  - More space, especially when the alphabet is large or the strings are long
  - More pointers or references required
  - More traversal steps required