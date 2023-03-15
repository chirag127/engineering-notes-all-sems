# Movetofront coding

- Movetofront coding is a data transformation algorithm that does not compress data by itself, but prepares it for better compression by entropy encoding techniques  .
- The basic idea of movetofront coding is to maintain a list of symbols (such as bytes or characters) and output the index of each symbol in the input sequence, while moving the symbol to the front of the list  .
- This way, symbols that occur frequently in the input sequence will have smaller indices and can be encoded with fewer bits by entropy encoding techniques such as Huffman coding or arithmetic coding  .
- Movetofront coding is an invertible transformation, meaning that the original input sequence can be recovered from the output sequence and the list of symbols  .
- Movetofront coding is used as a sub-step in several data compression algorithms, such as bzip2 and Burrows–Wheeler transform .
- Movetofront coding can improve the compression ratio of data that has long runs of identical symbols or symbols that appear in clusters .