 Here is the content in markdown format for the topic -

### Dictionary Techniques

Dictionaries are a useful technique for data compression as they can store information using shorter codes. Some dictionary compression techniques are -

1. Static Dictionary - In this, a fixed dictionary of common words and their codes is used. When encoding, the dictionary is searched for a match and the code is used. Eg - LZW algorithm. Advantage - Fast. Disadvantage - Limited to specific types of data.
2. Adaptive Dictionary - The dictionary is built as the data is being encoded. New words are added to the dictionary if they do not exist. Eg - Gzip. Advantage - More efficient on varying data. Disadvantage - Slower than static dictionary.
3. Semi-Adaptive Dictionary - Combines advantages of static and adaptive dictionary. Some pre-defined common words in dictionary and new words added as required.

Applications - Used in file compression tools like WinZip and Gzip. Achieves higher compression than statistical techniques.

Examples -

*Static Dictionary*

Word: Code

hello: 100
world: 200

*Adaptive Dictionary*

Word added: Code

hello: 100
world: 200
dictionary: 300

Advantages: Higher compression, handles varying data.
Disadvantages: Slower than static dictionary.

[Include diagrams/images if required]

The content can be studied and referred to for understanding dictionary techniques for data compression and their types, examples, applications, advantages and disadvantages. Please let me know if you would like me to elaborate on any part of the answer.