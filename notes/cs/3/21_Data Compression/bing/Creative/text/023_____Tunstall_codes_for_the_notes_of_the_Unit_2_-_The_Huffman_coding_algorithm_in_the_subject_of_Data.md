### Tunstall codes for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Tunstall coding is a type of source coding that converts variable-length words from the source alphabet into fixed-length codewords from the code alphabet  .
- Tunstall coding requires the algorithm to know the probability distribution of each letter of the source alphabet before the encoding process . This is also a requirement for Huffman coding.
- Tunstall coding is based on the idea of parsing the source text into words that are optimal for the given probability distribution. The words are not necessarily the same as the natural words of the language, but rather sequences of letters that have high probabilities of occurring together.
- Tunstall coding uses a tree structure to generate the codewords for each word in the source text. The tree is constructed by starting with a single node that represents the empty word, and then splitting it into branches according to the probabilities of each letter following the empty word. The process is repeated recursively for each branch until the desired number of codewords is reached.
- The codewords are assigned to the words by traversing the tree in a breadth-first order and assigning a binary digit to each branch. The codeword for a word is the concatenation of the binary digits along the path from the root to the node that represents the word.
- Tunstall coding is a prefix code, meaning that no codeword is a prefix of another codeword. This ensures that the decoding process is unambiguous and can be done by matching the codewords with the words in the tree.
- Tunstall coding has some advantages and disadvantages compared to other source coding methods. Some of the advantages are:
  - It produces a fixed-length output, which can be useful for applications that require constant transmission rate or storage size.
  - It can achieve a compression ratio close to the entropy of the source, which is the theoretical limit for lossless compression.
  - It can adapt to changes in the source distribution by updating the tree structure accordingly.
- Some of the disadvantages are:
  - It requires a large amount of memory to store the tree structure, which can be impractical for large alphabets or long codewords.
  - It can be inefficient for sources that have low redundancy or high variability, as the words may not capture the correlations well.
  - It can be sensitive to errors in the transmission or storage of the codewords, as a single bit error can affect the decoding of the entire word.