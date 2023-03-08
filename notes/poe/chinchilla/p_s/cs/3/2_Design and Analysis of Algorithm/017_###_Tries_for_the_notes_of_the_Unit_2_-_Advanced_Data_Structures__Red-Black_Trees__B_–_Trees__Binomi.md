## Tries

Trie, also known as a prefix tree, is a tree-like data structure that is used to store a dynamic set or associative array where the keys are usually strings. It was invented by Edward Fredkin in 1960.

### Structure

A trie is a rooted tree, where each node represents a single character. The root node represents an empty string, and the children of each node represent the possible characters that can come after the character represented by that node. The nodes that represent the end of a string are marked as terminal nodes.

### Insertion

To insert a string into a trie, we start at the root node and traverse the tree, one character at a time. If a node representing a character does not exist, we create a new node for that character. After we have inserted all the characters of the string, we mark the last node as a terminal node.

### Searching

To search for a string in a trie, we start at the root node and traverse the tree, one character at a time. If we reach a node that does not represent a character in the string, the string is not in the trie. If we reach a terminal node, the string is in the trie.

### Advantages

- Tries have a very fast search time since we only need to traverse the tree once, regardless of the size of the trie or the length of the string being searched for.
- Tries are useful for problems that involve searching for strings with a common prefix, such as autocomplete or spell-checking.

### Disadvantages

- Tries can use a lot of memory since each node represents a single character.
- Tries can be slower than hash tables for some operations.

### Applications

- Autocomplete
- Spell-checking
- IP routing
- Dictionary lookup

### Example

Suppose we want to store the following strings in a trie: "cat", "car", "cart", "dog", "doll", "dork".

```
          root
        /  |   \
       c   d    o
      / \   \    \
     a   a   g    l
    /     \   \
   t       r   o
  / \       \
 e   r       k
        \
         t
```

### Code

Here is an example implementation of a trie in Python:

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_terminal = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_terminal = True

    def search(self, word: str) -> bool:
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.is_terminal
```