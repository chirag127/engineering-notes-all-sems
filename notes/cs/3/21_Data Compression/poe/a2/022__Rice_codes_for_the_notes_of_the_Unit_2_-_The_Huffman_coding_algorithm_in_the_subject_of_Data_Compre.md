 Here is the content in Markdown format without any emojis or external links:

### Rice codes for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

1. Rice codes are a type of entropy encoding used for lossless data compression.
2. They are a variant of Golomb coding and are parametrized by a nonnegative integer k.
3. The coding works as follows:
 - Divide the input integer n by k and take the quotient q and remainder r.
 - Emit r as the first part of the code.
 - Emit the unary representation of q.
4. The efficiency of Rice codes depends on the choice of the parameter k. The optimal k is the one that minimizes the harmonic mean of the code lengths.
5. Rice codes are simple to implement and understand but often do not compress as well as more advanced entropy coders like Huffman coding or arithmetic coding.
6. They are still useful in some applications where simplicity is more important than maximum compression.

The content is written in a formal tone with points and no emojis or external links as instructed. Please let me know if you would like me to modify or expand the content in any way.