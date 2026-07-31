### Facsimile Encoding

- Facsimile encoding is a form of lossless data compression that is often used for document imaging and fax transmission.
- Facsimile encoding reduces the amount of data needed to represent a binary image, such as a scanned document or a fax page, by exploiting the spatial redundancy and the bi-level nature of the image .
- Facsimile encoding is based on the idea of run-length coding, which is a simple method of compressing a sequence of identical symbols by replacing them with a single symbol and a count of its repetitions .
- For example, the sequence 0000001111100000 can be compressed as 6,0,5,1,4,0 using run-length coding, where the first number is the length of the run and the second number is the symbol in the run.
- Facsimile encoding uses two types of run-length codes: white codes and black codes, which correspond to the runs of white and black pixels in the image, respectively .
- Facsimile encoding also uses a special code called EOL (end of line) to mark the end of each scan line in the image .
- Facsimile encoding assigns variable-length codes to the run-length codes, using a technique called Huffman coding, which is a method of assigning shorter codes to more frequent symbols and longer codes to less frequent symbols .
- For example, the white code 64, which represents a run of 64 white pixels, is assigned the code 11011, while the white code 1792, which represents a run of 1792 white pixels, is assigned the code 0000000110010010111.
- Facsimile encoding uses a standard set of Huffman codes, defined by the CCITT (now ITU-T) Group 3 and Group 4 recommendations, which are widely adopted by many facsimile and document imaging file formats .
- Facsimile encoding can achieve high compression ratios, especially for images that contain large areas of white or black pixels, such as text documents or drawings .
- Facsimile encoding can also be adapted to different transmission rates and channel conditions, by using different modes of operation, such as one-dimensional, two-dimensional, or mixed modes .
- Facsimile encoding can be decompressed quickly and easily, by using a table lookup or a tree traversal method to decode the Huffman codes and reconstruct the run-length codes and the image pixels .