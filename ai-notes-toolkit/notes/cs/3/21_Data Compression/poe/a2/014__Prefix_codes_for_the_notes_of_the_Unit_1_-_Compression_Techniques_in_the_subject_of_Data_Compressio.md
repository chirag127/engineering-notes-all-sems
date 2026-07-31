 Here is the content in markdown format without any emojis or external links:

### Prefix codes for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression:

1. Prefix codes are a type of universal code in which no codeword is a prefix of another codeword.
2. Huffman coding is a prefix code and is an example of entropy encoding.
3. The key advantage of prefix codes is that the decoding process can be unambiguous and instantaneous. As soon as the decoder sees a codeword, it knows exactly how long the codeword is and can immediately decode it without needing to look ahead at the next bits.
4. Canonical Huffman code is a prefix code which produces the minimum average number of bits required to represent symbols from a given alphabet with a given probability distribution.
5. The key steps to generate a Huffman code are:
	- Count the occurrence of each symbol in the input.
	- Build a min heap of symbols based on their frequency.
	- Repeatedly take two smallest frequency symbols and create a new internal node with these two symbols as children and with a frequency equal to the sum of the two symbols' frequencies.
	- Continue step#3 until only one node left.
	- Assign 0s and 1s to each bit based on the path from root to the node to get the code for that symbol.

The above content is written in a formal tone without any feelings or friendliness while following the points mentioned - written in markdown format inside the requested header with the topic of prefix codes for the notes of Unit 1 - Compression Techniques as asked. Please let me know if you would like me to modify or expand the content in any way.