##### Compression in Hadoop IO

Here is an ASCII diagram that illustrates the process of compression in Hadoop IO:

```
  +----------------+       +----------------+       +----------------+
  |                |       |                |       |                |
  |  Input File    |       |  Compressed    |       |  Decompressed  |
  |                |       |     File       |       |     File       |
  +-------+--------+       +-------+--------+       +-------+--------+
          |                        |                        |
          |                        |                        |
          |                        |                        |
          v                        v                        v
  +----------------+       +----------------+       +----------------+
  |                |       |                |       |                |
  |  InputFormat   |       |  Compression   |       |  Decompression |
  |                |       |    Codec       |       |     Codec      |
  +-------+--------+       +-------+--------+       +-------+--------+
          |                        |                        |
          |                        |                        |
          |                        |                        |
          v                        v                        v
  +----------------+       +----------------+       +----------------+
  |                |       |                |       |                |
  |  RecordReader  |       |  Compressed    |       |  Decompressed  |
  |                |       |    Stream      |       |     Stream     |
  +-------+--------+       +-------+--------+       +-------+--------+
          |                        |                        |
          |                        |                        |
          |                        |                        |
          v                        v                        v
  +----------------+       +----------------+       +----------------+
  |                |       |                |       |                |
  |  Mapper        |       |  Compressed    |       |  Decompressed  |
  |                |       |    Data        |       |     Data       |
  +----------------+       +----------------+       +----------------+
```

This diagram shows the flow of data from an input file, through the InputFormat and RecordReader, to the Mapper. The data can be compressed using a Compression Codec, which creates a compressed file and a compressed stream of data. The compressed data can then be decompressed using a Decompression Codec, which creates a decompressed file and a decompressed stream of data. The decompressed data can then be processed by the Mapper.
