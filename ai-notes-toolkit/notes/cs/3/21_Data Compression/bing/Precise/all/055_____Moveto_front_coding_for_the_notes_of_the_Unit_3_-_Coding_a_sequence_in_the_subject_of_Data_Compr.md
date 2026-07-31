### Move-to-front coding

Move-to-front (MTF) coding is a type of adaptive coding used in data compression. It is used to transform the input sequence into a sequence that is more easily compressible. It is often used in combination with other compression techniques, such as Huffman coding or arithmetic coding.

Here are some key points to remember about MTF coding:

1. MTF coding is an adaptive coding technique, meaning that it adjusts to the data being compressed.
2. It works by maintaining a list of symbols in the order of their most recent occurrence.
3. When a symbol is encountered in the input sequence, its index in the list is output and the symbol is moved to the front of the list.
4. This has the effect of assigning smaller codes to symbols that occur more frequently, making the sequence more easily compressible.
5. MTF coding is often used in combination with other compression techniques, such as Huffman coding or arithmetic coding, to achieve better compression ratios.
