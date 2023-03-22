 Here is the formal notes on the topic "Move-to-front coding for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression" in Markdown format:

### Move-to-front coding

1. Move-to-front coding is a data compression technique for sequences.
2. In this technique, each unique symbol in the input is assigned a unique index.
3. The encoding of a symbol is the index of that symbol in the symbol list.
4. During encoding, when a symbol is encountered, it is moved to the front of the symbol list and the new index is output.
5. This technique capitalizes on the locality of references in sequences - recently referenced symbols are more likely to be referenced again.
6. Move-to-front coding works best when the input symbols are uniformly distributed and the sequences have high locality of reference.
7. The decoding is simply reverting the symbol list to the original ordering and using the indices as the encoding to reproduce the original sequence.
8. Move-to-front coding can achieve compression when the locality of reference in sequences is high. The amount of compression depends on the characteristics of the input sequence.

The above notes cover the key points about Move-to-front coding for sequences. The content is written in a formal tone with points and without any emojis or external links as instructed. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.