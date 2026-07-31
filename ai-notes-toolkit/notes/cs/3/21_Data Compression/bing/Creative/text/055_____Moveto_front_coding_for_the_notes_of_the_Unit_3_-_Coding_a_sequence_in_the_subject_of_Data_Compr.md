### Movetofront coding

- Movetofront coding is a data transformation algorithm that does not compress data by itself, but prepares it for better compression by entropy encoding techniques  .
- The basic idea of movetofront coding is to maintain a list of symbols (such as bytes or characters) that is updated dynamically as the input data is processed  .
- The list is initialized with all possible symbols in some order (such as alphabetical or numerical). For each input symbol, the output is the index of that symbol in the list, and then the symbol is moved to the front of the list  .
- The output is a sequence of numbers that represent the positions of the input symbols in the list. The numbers are usually smaller for more frequent symbols, which makes them more suitable for entropy encoding  .
- Movetofront coding is reversible, meaning that the original input can be recovered from the output and the list. The decoding algorithm is the same as the encoding algorithm, except that the output symbols are used to look up the input symbols in the list, and then the input symbols are moved to the front of the list  .
- Movetofront coding is often used as a preprocessing step in data compression algorithms, such as Burrows–Wheeler transform and arithmetic coding, to exploit the locality and redundancy of the input data .
- Movetofront coding is fast and simple to implement, and can improve the compression ratio and speed of entropy encoding techniques  .