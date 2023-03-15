### Diagram Coding for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Diagram coding is a technique for compressing a sequence of symbols by encoding it as a sequence of numbers.
- The idea is to use a dictionary that maps symbols or pairs of symbols to numbers, and update the dictionary as new symbols or pairs are encountered in the input sequence.
- The dictionary can be initialized with the symbols of the alphabet and their corresponding numbers, or it can be built dynamically from the input sequence.
- The output of the diagram coding is a sequence of numbers that can be decoded by using the same dictionary in reverse.
- Diagram coding can achieve better compression than simple symbol coding, because it can exploit the correlations or patterns between adjacent symbols in the input sequence.
- An example of diagram coding is the LZ77 algorithm, which uses a sliding window to store the most recent symbols of the input sequence, and encodes each symbol or pair as a reference to a previous occurrence in the window.