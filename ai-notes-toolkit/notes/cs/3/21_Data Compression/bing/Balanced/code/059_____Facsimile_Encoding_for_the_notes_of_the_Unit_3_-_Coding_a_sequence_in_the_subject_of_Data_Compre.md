### Facsimile Encoding

- Facsimile encoding is a form of lossless data compression that is often used for document imaging and fax transmission.
- Facsimile encoding exploits the fact that most documents have large areas of white or black pixels, and uses run-length coding to encode the lengths of consecutive runs of the same color.
- Run-length coding is a simple technique that replaces a sequence of identical symbols with a pair of the symbol and its count. For example, the sequence `WWWWWWWWWW` can be encoded as `(W,10)`.
- Facsimile encoding uses two types of run-length codes: white codes and black codes. White codes are used to encode runs of white pixels, and black codes are used to encode runs of black pixels.
- Facsimile encoding also uses two modes: horizontal mode and vertical mode. Horizontal mode encodes two consecutive runs of different colors on the same scan line. Vertical mode encodes a single run of pixels that differs from the corresponding run on the previous scan line by one pixel.
- Facsimile encoding uses a variable-length codebook to assign codes to different run lengths. The codebook is designed to assign shorter codes to more frequent run lengths, and longer codes to less frequent run lengths. This is similar to Huffman coding, which is another form of lossless data compression.
- Facsimile encoding can reduce the transmission requirements of fax images while maintaining high intelligibility in mobile communications environments. Facsimile encoding can also be applied to the lossless compression of images with 8-bit per pixel or higher.