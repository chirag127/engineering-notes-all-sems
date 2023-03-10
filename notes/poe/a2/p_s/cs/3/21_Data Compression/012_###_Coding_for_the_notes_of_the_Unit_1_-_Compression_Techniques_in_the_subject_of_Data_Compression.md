 Here is the content in markdown format for the topic -

### Coding for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

1. Coding refers to the process of converting the input data into another form or representation that reduces the number of bits needed to represent the data. This is done by exploiting the redundancy present in the input data.
    - Examples of coding techniques:
        - Variable-length coding: Assigns codes of variable lengths to input symbols based on their probabilities of occurrence. More probable symbols get shorter codes and less probable symbols get longer codes. Example - Huffman coding.
        - Dictionary coding: Maintains a dictionary of (input symbol, codeword) pairs. If input symbol is found in dictionary, its codeword is used. If not, new entry is added to dictionary. Example - Lempel-Ziv coding.
        - Fixed-length coding: Assigns codes of fixed lengths to input symbols. Examples - Ascii, Unicode, etc.
2. The key advantages of coding are:
    - Reduces the number of bits needed to represent the data and hence compresses the data.
    - Increases the speed of transmission/storage as fewer bits need to be processed.
3. The disadvantages of coding are:
    - Additional processing is required to encode and decode the data which can increase time complexity.
    - The decoder must know the coding scheme used to decode the data. This requires transmission of coding scheme information also, though a small amount.
4. Coding is used in various applications like:
    - Image compression - JPEG, PNG
    - Audio compression - MP3, AAC
    - Video compression - MP4, MPEG
    - File compression - ZIP, RAR

[Detailed diagrams, examples, and other points can be added here as per the instructions.]