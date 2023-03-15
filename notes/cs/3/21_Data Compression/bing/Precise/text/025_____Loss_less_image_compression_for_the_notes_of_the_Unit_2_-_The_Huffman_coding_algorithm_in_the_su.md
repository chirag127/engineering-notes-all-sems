### Lossless Image Compression using Huffman Coding Algorithm

- **Image compression** is the technique that deals with the problem of reducing the amount of data required to represent a digital image.
- Image compression is achieved by removal of one or three basic data redundancies: (1) coding redundancy, (2) spatial redundancy, (3) irrelevant information.
- **Huffman coding** is a particular type of optimal prefix code that is commonly used for lossless data compression.
- Prefix code means that the code assigned to one character is not a prefix of code assigned to any other character.
- The idea is to assign variable-length codes to input characters, lengths of assign codes are based on the frequencies of corresponding characters.
- The most frequent occurring character gets the smallest input code and the most occurring character gets the largest code.
- Huffman coding has application in fields where it is important that the original and decompressed data be identical, like in zip file format and is often used as a component within lossy data compression techniques like mp3 encoder and other lossy audio encoder.
- The result from Huffman’s algorithm is viewed as a variable code table. This algorithm derives the table from an estimated probability or frequency of occurrence (weight) for each possible value of source symbol.
- Huffman coding is the base of JPEG image compression.
- An algorithm is created in Delphi to implement Huffman coding method that removes redundant codes from the image and compresses a BMP image file (especially grayscale image) and it is successfully reconstructed and an exact representation of the original because it is lossless compression technique.
- Huffman coding and arithmetic coding both are well-recognized lossless entropy coding algorithms.