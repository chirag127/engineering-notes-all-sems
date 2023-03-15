### Tries

A trie, also known as a digital tree or prefix tree, is a type of search tree that is used to store a dynamic set or associative array where the keys are usually strings. Tries are commonly used for tasks such as autocomplete and spell checking.

Here are some key points to remember about tries:

1. Each node in a trie represents a prefix of the keys that are stored in the subtree rooted at that node.
2. The root node represents an empty string.
3. Each edge in the trie is labeled with a character.
4. The children of a node are ordered lexicographically by the characters on the edges connecting them to their parent.
5. A node is marked as a terminal node if it represents the end of a key.
6. Searching for a key in a trie involves following a path from the root to a terminal node, where each edge on the path corresponds to a character in the key.
7. Inserting a key into a trie involves following the path for the key and creating new nodes as necessary.
8. Deleting a key from a trie involves following the path for the key and removing nodes that are no longer needed.

Tries are particularly useful when dealing with large sets of keys that share common prefixes, as they can be used to efficiently search for and retrieve keys that match a given prefix. They are also useful for implementing algorithms that require fast access to the set of keys with a given prefix, such as autocomplete and spell checking algorithms.