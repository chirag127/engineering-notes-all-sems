### Tries

- A trie is a tree-based data structure used for storing and retrieving collections of strings .
- The word trie comes from the word re**trie**val which means to find or get something back.
- A trie is also called a digital tree or a prefix tree.
- A trie is a type of k-ary search tree, where each node has k children, one for each character in the alphabet.
- A trie can store strings that have a common prefix in a shared subtree, which saves space and allows fast search operations .
- A trie can support the following operations:
  - Insert: To add a new string to the trie, we start from the root and follow the path of the characters in the string. If a node for a character does not exist, we create a new node and link it to the parent. We mark the last node as the end of the word.
  - Search: To search for a string in the trie, we start from the root and follow the path of the characters in the string. If we reach a node that is marked as the end of the word, we return true. If we reach a node that does not exist or is not marked as the end of the word, we return false.
  - Delete: To delete a string from the trie, we start from the root and follow the path of the characters in the string. If we reach a node that is marked as the end of the word, we unmark it. If the node has no children, we delete it and recursively delete its parent if it has no other children.
- A trie can be used for various applications, such as:
  - Autocomplete: A trie can store a dictionary of words and suggest possible completions for a given prefix.
  - Spell check: A trie can check if a given word is in the dictionary or suggest corrections for misspelled words.
  - Pattern matching: A trie can match a pattern with a set of strings and find all the occurrences of the pattern.
  - IP routing: A trie can store IP addresses and find the longest prefix match for a given address.
  - Word games: A trie can generate valid words from a given set of letters or find words that match a given pattern.