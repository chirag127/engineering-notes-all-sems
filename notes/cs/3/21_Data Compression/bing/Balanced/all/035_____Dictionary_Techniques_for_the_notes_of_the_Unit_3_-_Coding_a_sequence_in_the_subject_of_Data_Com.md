# Dictionary Techniques for Data Compression

- Dictionary techniques are a class of lossless data compression algorithms that operate by searching for matches between the text to be compressed and a set of strings contained in a data structure called the dictionary.
- The dictionary can be either static or adaptive, depending on whether it is fixed or updated during the compression process.
- The basic idea of dictionary techniques is to replace repeated occurrences of strings with shorter codes that point to the dictionary entries where the original strings are stored.
- Dictionary techniques can achieve high compression ratios for texts that have a lot of redundancy or repetition.
- Some examples of dictionary techniques are:

  - Non-adaptive dictionary compression: This technique uses a predefined dictionary that is known to both the encoder and the decoder. The dictionary can be based on the frequency or the length of the strings, or on some other criteria. A simple example of this technique is text compression using 4-bit coding, where each character is represented by a 4-bit code that corresponds to its position in the dictionary.
  - Adaptive dictionary compression: This technique builds and updates the dictionary dynamically during the compression process. The dictionary starts with a set of basic symbols (such as individual characters) and grows as new strings are encountered. The encoder and the decoder synchronize their dictionaries by sending the new entries along with the compressed data. A common example of this technique is the family of LZ algorithms, which use a sliding window to find matches between the current string and the previous text. Some variants of LZ algorithms are LZ77, LZ78, LZW, LZSS, LZJB, LZ4, etc.