### Facsimile Encoding

- Facsimile encoding is a technique for compressing binary images, such as scanned documents, maps, or photographs, that consist of black and white pixels.
- Facsimile encoding is based on the observation that most binary images have large regions of uniform color, and the transitions between black and white pixels occur along horizontal lines.
- Facsimile encoding exploits this redundancy by encoding the lengths of consecutive runs of black or white pixels, rather than the individual pixel values.
- Facsimile encoding can be classified into two types: one-dimensional and two-dimensional.
- One-dimensional facsimile encoding, also known as run-length encoding, encodes each row of pixels independently, by alternating the run lengths of black and white pixels, starting from a fixed color (usually white).
- Two-dimensional facsimile encoding, also known as differential encoding, encodes each row of pixels relative to the previous row, by using a reference line and a coding line, and encoding the differences between them.
- Two-dimensional facsimile encoding can achieve higher compression ratios than one-dimensional facsimile encoding, by exploiting the correlation between adjacent rows of pixels.
- Two-dimensional facsimile encoding can be further divided into two modes: line-by-line and block-by-block.
- Line-by-line mode encodes each row of pixels as a sequence of codes that indicate the horizontal displacement of the coding line from the reference line, and the color of the next pixel.
- Block-by-block mode encodes each block of pixels as a two-dimensional array of codes that indicate the vertical and horizontal displacement of the coding line from the reference line, and the color of the next pixel.
- Facsimile encoding can use different coding schemes to represent the run lengths or the displacements, such as Huffman coding, arithmetic coding, or Golomb-Rice coding.
- Facsimile encoding is widely used in fax machines, document scanners, and image compression standards, such as CCITT Group 3 and 4, JBIG, and TIFF.