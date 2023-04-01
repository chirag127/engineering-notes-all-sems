

### c) Word and Character Count of a Given String

1. A string is a sequence of characters. 
2. To count the number of words in a string, we must first separate the individual words. This can be done by using the `split()` function. 
3. To count the number of characters in a string, we must use the `len()` function. 
4. We can combine these two functions to count both the words and characters in a string. 
5. For example, if we have the following string: `"Hello, World!"`, we can count the words and characters as follows:

```
words = "Hello, World!".split()
word_count = len(words)
character_count = len("Hello, World!")

print("Word count:", word_count)
print("Character count:", character_count)
```

This will print out:

```
Word count: 2
Character count: 13
```