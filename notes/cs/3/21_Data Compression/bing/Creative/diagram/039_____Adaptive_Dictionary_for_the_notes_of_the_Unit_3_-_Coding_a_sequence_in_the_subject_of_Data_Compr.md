### Adaptive Dictionary for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Adaptive dictionary is a technique of data compression that uses a dynamic dictionary that is updated during the compression and decompression processes .
- Adaptive dictionary allows the compression algorithm to adapt to the characteristics of the data and achieve better compression ratios .
- Adaptive dictionary can be implemented using different methods, such as LZ77, LZ78, and LZW, which are named after their inventors Ziv and Lempel .
- LZ77 is a method that uses a sliding window to store the most recent data and searches for matches with the current data in the window. If a match is found, the current data is replaced by a pointer to the location and length of the match in the window .
- LZ78 is a method that builds a dictionary of phrases from the input data and assigns a code to each phrase. The input data is then replaced by the codes of the corresponding phrases in the dictionary. The dictionary is updated with new phrases as they are encountered in the input data .
- LZW is a method that is based on LZ78, but uses a variable-length code for the phrases in the dictionary. The code length increases as the dictionary grows, allowing more phrases to be stored. LZW also uses a special code to indicate when the dictionary needs to be cleared and rebuilt .
- Adaptive dictionary is widely used in applications such as text, image, audio, and video compression, as well as data transmission and storage  .