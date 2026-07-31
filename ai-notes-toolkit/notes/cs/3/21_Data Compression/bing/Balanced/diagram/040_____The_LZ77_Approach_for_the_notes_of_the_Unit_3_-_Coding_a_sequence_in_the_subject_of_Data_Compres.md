### The LZ77 Approach

- LZ77 is a lossless data compression algorithm that was published by Abraham Lempel and Jacob Ziv in 1977.
- LZ77 achieves compression by replacing repeated occurrences of data with references to a single copy of that data existing earlier in the uncompressed data stream.
- LZ77 uses two buffers: a search buffer that contains a portion of the recently encoded sequence, and a look-ahead buffer that contains the next portion of the sequence to be encoded.
- LZ77 encodes each symbol in the look-ahead buffer as either a literal (the symbol itself) or a pointer (a pair of numbers that indicate the length and distance of a matching sequence in the search buffer).
- LZ77 tries to find the longest match between the look-ahead buffer and the search buffer, and encodes it as a pointer if it is longer than a certain threshold, otherwise it encodes it as a literal.
- LZ77 can achieve high compression ratios for data that contains many repeated patterns, such as natural language texts or images.
- LZ77 is the basis for many variations and improvements, such as LZSS, LZMA, DEFLATE, and others.