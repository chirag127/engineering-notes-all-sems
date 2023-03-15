### Facsimile Encoding

- Facsimile encoding is a form of lossless data compression that is often used for document imaging and fax transmission.
- Facsimile encoding exploits the fact that most documents have large areas of white or black pixels, and uses run-length coding to encode the lengths of consecutive runs of the same color.
- Run-length coding is a simple technique that replaces a sequence of identical symbols with a pair of the symbol and its count. For example, the sequence `WWWWWWWWWW` can be encoded as `(W,10)`.
- Facsimile encoding uses two types of run-length codes: white codes and black codes. White codes are used to encode runs of white pixels, and black codes are used to encode runs of black pixels.
- Facsimile encoding also uses two modes: horizontal mode and vertical mode. Horizontal mode encodes two consecutive runs of different colors on the same scan line. Vertical mode encodes the position of the first changing pixel on the next scan line relative to the current scan line.
- Facsimile encoding uses a variable-length codebook to assign binary codes to each run-length code or vertical mode code. The codebook is designed to minimize the average code length, and is based on the Huffman method or the arithmetic coding method.
- The Huffman method assigns shorter codes to more frequent symbols, and longer codes to less frequent symbols. The arithmetic coding method assigns codes to symbols based on their probabilities, and can achieve optimal compression.
- Facsimile encoding can reduce the transmission requirements of facsimile images while maintaining high intelligibility in mobile communications environments. Facsimile encoding can also be applied to the lossless compression of images with low color depth or high redundancy.