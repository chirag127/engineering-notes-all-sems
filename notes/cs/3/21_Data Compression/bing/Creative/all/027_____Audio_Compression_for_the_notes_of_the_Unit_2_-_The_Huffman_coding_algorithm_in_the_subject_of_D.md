# Audio Compression for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Audio compression is the process of reducing the size of an audio file by removing or encoding redundant or irrelevant information.
- Audio compression can be lossless or lossy, depending on whether the original data can be perfectly reconstructed or not.
- Lossless audio compression techniques preserve the exact quality and information of the original audio signal, but achieve a lower compression ratio than lossy techniques.
- Lossy audio compression techniques discard some information from the original audio signal, but achieve a higher compression ratio than lossless techniques.
- Huffman coding is a lossless audio compression technique that assigns variable-length codes to the symbols in the audio data, based on their frequencies of occurrence.
- Huffman coding works by creating a binary tree that represents the symbols and their frequencies, where the most frequent symbols are assigned the shortest codes and the least frequent symbols are assigned the longest codes.
- Huffman coding is optimal for a given set of symbols and frequencies, meaning that no other lossless coding scheme can achieve a lower average code length.
- Huffman coding can be static or dynamic, depending on whether the code tree is fixed or updated for each block of data.
- Static Huffman coding uses a predefined code tree that is known to both the encoder and the decoder, and does not change during the compression process.
- Dynamic Huffman coding adapts the code tree to the data as it is processed, and transmits the code tree along with the compressed data.
- Huffman coding is used in many audio compression standards, such as JPEG, MPEG-2, MP3, and FLAC.