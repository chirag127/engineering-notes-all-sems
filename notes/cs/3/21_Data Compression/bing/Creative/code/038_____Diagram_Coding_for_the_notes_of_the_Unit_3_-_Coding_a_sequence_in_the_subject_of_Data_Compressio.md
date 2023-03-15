Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of diagram coding for the notes of the unit 3 - coding a sequence in the subject of data compression.

### Diagram Coding

- Diagram coding is a method of data compression that encodes pairs of symbols instead of single symbols.
- The idea is to exploit the correlation between adjacent symbols in a sequence, and assign shorter codes to more frequent pairs.
- A diagram coder consists of two components: a codebook and a coder.
- A codebook is a table that maps each pair of symbols to a unique binary code. The codebook can be fixed or adaptive, depending on whether it is predefined or updated during the encoding process.
- A coder is a device that reads the input sequence symbol by symbol, and outputs the corresponding code for each pair of symbols. If the input sequence is odd-length, a special symbol can be appended to make it even-length.
- An example of a fixed codebook for the alphabet {a, b, c, d, e} is shown below:

| Pair | Code |
|------|------|
| aa   | 00   |
| ab   | 01   |
| ac   | 100  |
| ad   | 101  |
| ae   | 1100 |
| ba   | 1101 |
| bb   | 1110 |
| bc   | 1111 |
| bd   | 0100 |
| be   | 0101 |
| ca   | 0110 |
| cb   | 0111 |
| cc   | 0010 |
| cd   | 0011 |
| ce   | 0000 |
| da   | 0001 |
| db   | 1010 |
| dc   | 1011 |
| dd   | 1000 |
| de   | 1001 |
| ea   | 01100|
| eb   | 01101|
| ec   | 01110|
| ed   | 01111|
| ee   | 01000|

- An example of a diagram coder using the above codebook is shown below:

| Input sequence | Output code |
|----------------|-------------|
| abcd           | 0110110011  |
| eedcba         | 0100000110111101101 |
| aabbaa         | 000011100000 |