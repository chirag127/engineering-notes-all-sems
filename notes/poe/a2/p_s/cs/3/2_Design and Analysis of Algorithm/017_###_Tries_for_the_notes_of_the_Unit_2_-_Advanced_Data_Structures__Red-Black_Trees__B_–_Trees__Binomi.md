 Here are the notes for the topic **Tries** for the Unit 2 - Advanced Data Structures:

### Tries

- A Trie is an efficient information reTrieval data structure.
- It is a tree-like structure in which each branch represents a character of the string.
- It is mainly used to store strings and retrieve them.
- It is also known as a prefix tree as it stores the strings in a tree structure based on the prefixes.

**Structure:**

- A Trie consists of:
- Nodes: Each node represents a character of the string.
- Edges: Edges connect the nodes and are labeled with characters.
- Root: The root is the first node of the Trie.

**Insertion:**

- To insert a string into a Trie, we start at the root and traverse downwards based on the characters of the string.
- If the path doesn't exist, we create new nodes.
- Once the string is fully inserted, we mark the last node as the end of the string.

**Searching:**

- To search for a string, we start at the root and traverse downwards based on the characters of the string.
- If we reach a node whose path does not match the string, we return false.
- If we reach the end of the string, we check if the last node is marked as the end of the string. If so, the string exists in the Trie, else it doesn't.

**Advantages:**

- Tries have an efficient lookup time of O(k) where k is the length of the key (string).
- Tries dynamically allocate memory and do not have inefficient space utilization as in binary search trees.
- Tries can be used to store strings with common prefixes and search strings with a common prefix efficiently.

**Disadvantages:**

- Tries require a lot of memory as each character of the string is stored in a node.
- Insertion and deletion are more complex compared to binary search trees.

**Applications:**

- Tries are commonly used to:
- Check if a word exists in a dictionary.
- Autocomplete features.
- Spell checkers.
- IP routing lookups.
- Finding similar strings.