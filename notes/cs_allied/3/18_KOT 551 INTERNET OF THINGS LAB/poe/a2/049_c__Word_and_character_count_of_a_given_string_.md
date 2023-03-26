 Here is the formal content on the given topic:

c) Word and character count of a given string:

I. Introduction
- Counting the number of words and characters in a given string is a common requirement in many text processing tasks.
- This can be useful to get statistics about the string such as average word length, most frequent words etc.

II. Algorithm
- Split the string into words using str.split() method.
- Count the number of words using len() function on the split string. This gives the word count.
- Count the number of characters using a for loop. Initialize a count variable to 0. Iterate over each character in the string and increment the count variable.
- At the end of the loop, the count variable will contain the total character count.

III. Example
- String: "Hello World"
- Split into words: ["Hello", "World"]
- Word count: 2
- Character count: 11

IV. Applications
- Text summarization - Finding keywords and salient phrases
- Sentiment analysis - Counting positive and negative words
- Spelling correction - Suggesting probable correct spellings based on word length
- Readability analysis - Calculating readability scores using word and sentence length

V. Conclusion
- Calculating word and character counts of a given string is a simple task with inbuilt Python functions and loops.
- This can be extended to compute various metrics and statistics on the string to gain insights into its content and structure.