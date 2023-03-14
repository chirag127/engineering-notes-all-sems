Data compression is the function of presentation layer in OSI reference model. Compression is often used to maximize the use of bandwidth across a network or to optimize disk space when saving data. Data compression deals with taking a string of bytes and compressing it down to a smaller set of bytes, whereby it takes either less bandwidth to transmit the string or to store it to disk. The compressed string is then re-inflated by the receiving side or application.

### Data compression in application layer

The application layer is the topmost layer in the OSI model. It provides several ways for manipulating the data (information) which actually enables any type of user to access network with ease. The application layer also makes a request to its bottom layer, which is presentation layer for receiving various types of information from it. The application layer interface directly interacts with application and provides common web application services.

The application layer can use data compression to reduce the size of the data that it sends or receives from the presentation layer. This can improve the performance and efficiency of the communication process. The application layer can use different compression algorithms depending on the type of data and the desired compression ratio. Some examples of compression algorithms are:

- Huffman coding: A lossless compression algorithm that assigns variable-length codes to symbols based on their frequency of occurrence.
- Run-length encoding: A lossless compression algorithm that replaces sequences of repeated symbols with a single symbol and a count.
- Lempel-Ziv-Welch (LZW): A lossless compression algorithm that builds a dictionary of common substrings and replaces them with codes.
- JPEG: A lossy compression algorithm that reduces the size of images by discarding some information that is not perceptible to the human eye.
- MP3: A lossy compression algorithm that reduces the size of audio files by discarding some information that is not audible to the human ear.

The following diagram illustrates the basic architecture of data compression in application layer using ASCII art:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Application    |     |  Application    |     |  Application    |
|    Layer        |     |    Layer        |     |    Layer        |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Compression    |     |  Compression    |     |  Compression    |
|    Module       |     |    Module       |     |    Module       |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Presentation   |     |  Presentation   |     |  Presentation   |
|    Layer        |     |    Layer        |     |    Layer        |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Session Layer  |     |  Session Layer  |     |  Session Layer  |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Transport      |     |  Transport      |     |  Transport      |
|    Layer        |     |    Layer        |     |    Layer        |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Network Layer  |     |  Network Layer  |     |  Network Layer  |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Data Link      |     |  Data Link      |     |  Data Link      |
|    Layer        |     |    Layer        |     |    Layer        |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Physical Layer |     |  Physical Layer |     |  Physical Layer |
|                 |     |                 |     |                 |