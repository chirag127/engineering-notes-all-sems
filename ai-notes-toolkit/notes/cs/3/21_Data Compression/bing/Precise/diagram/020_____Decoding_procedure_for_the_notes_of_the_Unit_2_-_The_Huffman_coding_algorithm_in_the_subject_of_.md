### Decoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

1. Huffman coding is a lossless data compression algorithm.
2. The idea is to assign variable-length codes to input characters, lengths of the assigned codes are based on the frequencies of corresponding characters.
3. The most frequent character gets the smallest code and the least frequent character gets the largest code.
4. The variable-length codes assigned to input characters are Prefix Codes, means the codes (bit sequences) are assigned in such a way that the code assigned to one character is not the prefix of code assigned to any other character. This is how Huffman Coding makes sure that there is no ambiguity when decoding the generated bitstream.
5. Let us understand the algorithm with an example:

    - Consider the string `ABRACADABRA`. The frequencies of characters in the string are:

        ```
        A - 5
        B - 2
        R - 2
        C - 1
        D - 1
        ```

    - The Huffman tree for the given string is as follows:

        ```
              /\  
             /  \  
            A    /\  
                /  \  
               R   /\  
                  /  \  
                 B   /\  
                    /  \  
                   C   D
        ```

    - The codes for the characters are as follows:

        ```
        A - 0
        B - 100
        R - 101
        C - 1100
        D - 1101
        ```

    - The encoded bitstream for the given string is `0100100110101100101000`.
    - To decode the bitstream, we start from the root of the Huffman tree and move left if the current bit is 0 and move right if the current bit is 1. When we reach a leaf node, we print the character and start from the root again. For the given bitstream, the decoded string is `ABRACADABRA`.

6. The time complexity of the Huffman coding algorithm is O(nlogn) where n is the number of unique characters in the input string.
7. Huffman coding is widely used in data compression applications such as file compression and image compression.