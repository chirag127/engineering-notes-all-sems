### Static Dictionary for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

In data compression, static dictionary helps in reducing the size of the information being transmitted or stored. It is a predefined set of words or phrases that are commonly used in the data being compressed. Here are some important points to understand about static dictionary:

- A static dictionary is fixed and pre-determined. It is created based on the type of data being compressed.
- The dictionary contains a set of words or phrases that are frequently used in the data being compressed. These words or phrases are assigned a unique code or symbol.
- The code assigned to each word or phrase in the dictionary is shorter than the original word or phrase. This helps in reducing the size of the data being compressed.
- During compression, the dictionary is used to replace the frequently occurring words or phrases with their respective codes. This process is known as dictionary coding.
- Dictionary coding is performed in two phases - encoding and decoding. In the encoding phase, the words or phrases are replaced with their respective codes. In the decoding phase, the codes are replaced with their respective words or phrases to retrieve the original data.
- The advantage of using a static dictionary is that it does not need to be transmitted along with the compressed data. It is assumed that the receiver already has the same dictionary as the sender.
- However, the disadvantage of using a static dictionary is that it may not be efficient for compressing data with unique or uncommon words or phrases. In such cases, dynamic dictionary may be more effective.

In conclusion, static dictionary is a predefined set of words or phrases that are commonly used in the data being compressed. It helps in reducing the size of the information being transmitted or stored by assigning unique codes to frequently occurring words or phrases. While it is efficient for compressing data with common words or phrases, it may not be effective for data with unique or uncommon content.