# Facsimile Encoding

- Facsimile encoding is a form of lossless data compression that is often used for document imaging and fax transmission .
- Facsimile encoding is based on run-length encoding, which is a method of representing sequences of identical symbols by their length and value .
- For example, the sequence `000000111111000000` can be encoded as `6,0,6,1,6,0`, where the first number is the length and the second number is the value of the run.
- Facsimile encoding is especially suitable for binary images, such as text or line drawings, that have large areas of white or black pixels .
- Facsimile encoding can reduce the size of binary images by a factor of 10 to 20, depending on the image content and quality .
- Facsimile encoding can be further improved by using adaptive models, such as Huffman coding or arithmetic coding, that assign shorter codes to more frequent runs .
- For example, Huffman coding assigns variable-length codes to each run-length pair based on their probability of occurrence, while arithmetic coding encodes the entire sequence of run-length pairs as a single fraction.
- Facsimile encoding can be decompressed quickly for printing or viewing, as long as enough memory and CPU resources are available.