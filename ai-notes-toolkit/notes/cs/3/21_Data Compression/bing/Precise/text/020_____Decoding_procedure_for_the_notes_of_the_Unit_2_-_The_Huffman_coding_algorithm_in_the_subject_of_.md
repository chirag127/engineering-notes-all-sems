### Decoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

1. Huffman coding is a lossless data compression algorithm.
2. The idea is to assign variable-length codes to input characters, lengths of the assigned codes are based on the frequencies of corresponding characters.
3. The most frequent character gets the smallest code and the least frequent character gets the largest code.
4. The variable-length codes assigned to input characters are Prefix Codes, means the codes (bit sequences) are assigned in such a way that the code assigned to one character is not the prefix of code assigned to any other character. This is how Huffman Coding makes sure that there is no ambiguity when decoding the generated bitstream.
5. Let us understand the algorithm with an example:

    - Consider the string `ABRACADABRA`. The frequencies of characters in the string are:

        - A: 5
        - B: 2
        - R: 2
        - C: 1
        - D: 1

    - The Huffman tree for the given string is as follows:

        ```
             /\ 
            /  \
           A   /\
             /  \
            B   /\
              /  \
             R   /\
               /  \
              C   D
        ```

    - The codes for the characters are as follows:

        - A: 0
        - B: 10
        - R: 110
        - C: 1110
        - D: 1111

    - The encoded string is `0110111010001010110111100`.

6. To decode the encoded string, we need to traverse the Huffman tree from the root and for each `0`, we move to the left child and for each `1`, we move to the right child. When we reach a leaf node, we print the character and start traversing the tree from the root again.

7. The decoded string is `ABRACADABRA`.

8. The time complexity of the Huffman coding algorithm is `O(nlogn)` where `n` is the number of unique characters in the input string.

9. The space complexity of the Huffman coding algorithm is `O(n)` where `n` is the number of unique characters in the input string.

10. Huffman coding is widely used in data compression applications such as file compression, image compression, and video compression. It is also used in the implementation of the DEFLATE algorithm which is used in the popular data compression formats such as ZIP and GZIP.