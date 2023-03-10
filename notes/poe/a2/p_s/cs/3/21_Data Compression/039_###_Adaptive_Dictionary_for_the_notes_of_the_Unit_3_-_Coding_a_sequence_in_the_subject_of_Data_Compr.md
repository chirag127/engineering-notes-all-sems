 Here is the content written in markdown format for the topic -

### Adaptive Dictionary for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- An adaptive dictionary is a dictionary which gets updated dynamically as the compression progresses.
- It starts with an initial dictionary which contains some common words and their codes.
- As the compression progresses and new words are encountered, the dictionary is updated with these new words and their codes.
- This leads to higher compression as the dictionary contains words which actually occur in the data and not just common words.
- The decoder also needs to be adaptive in this case and update its dictionary as and when it receives new codes for new words.
- Examples of algorithms using adaptive dictionaries are LZ77, LZ78.
- Advantages - Higher compression ratio as the dictionary is tailored to the actual data.
- Disadvantages - Complexity of updating the dictionary and synchronization between encoder and decoder.
- Applications - Used in gzip, png etc.

[Diagrams and examples can be added here to aid understanding]

The content is written in points in a formal tone as requested. Markdown formatting is used for headers and lists. Please let me know if you would like me to elaborate on any of the points or add more details and examples.