# The LZ77 Approach

- LZ77 is a lossless data compression algorithm published by Abraham Lempel and Jacob Ziv in 1977  .
- It is a dictionary coder and maintains a sliding window during compression  .
- The sliding window contains a fixed-size buffer of recently processed data, divided into two parts: the search buffer and the look-ahead buffer .
- The search buffer contains the data that has already been encoded, and the look-ahead buffer contains the data that is yet to be encoded .
- The algorithm scans the look-ahead buffer for the longest match with any string in the search buffer .
- If a match is found, the algorithm outputs a triple of the form (offset, length, next symbol), where offset is the distance from the current position to the start of the matching string, length is the number of matching symbols, and next symbol is the symbol following the match in the look-ahead buffer .
- If no match is found, the algorithm outputs a special symbol indicating a literal, followed by the first symbol in the look-ahead buffer .
- The algorithm then slides the window by one or more symbols, depending on the length of the match or the literal, and repeats the process until the end of the input data .
- The output of the algorithm is a sequence of triples and literals that can be decoded by reversing the process .
- The algorithm achieves compression by replacing repeated occurrences of data with references to previous occurrences .
- The compression ratio depends on the size of the sliding window, the characteristics of the input data, and the encoding scheme for the output .
- The algorithm is simple, fast, and widely used in various applications, such as ZIP, gzip, PNG, and others.