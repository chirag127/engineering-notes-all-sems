##### Compression in Hadoop io

- Compression is a technique to reduce the size of data by encoding it in a different format that uses fewer bits.
- Compression is useful in Hadoop for saving storage space, reducing network bandwidth, and improving performance of mapreduce jobs.
- Hadoop supports various compression codecs, such as DEFLATE, gzip, bzip2, LZO, LZ4, and Snappy. Each codec has different characteristics in terms of compression ratio, speed, and splittability.
- Splittability means the ability to split a compressed file into smaller chunks that can be processed independently by different map tasks. This is important for parallel processing and load balancing in Hadoop.
- Only bzip2 is splittable among the standard codecs, but it is also the slowest and most CPU-intensive. LZO, LZ4, and Snappy are fast and lightweight, but not splittable. DEFLATE and gzip are somewhere in between, but gzip is more widely supported and compatible.
- Hadoop provides a CodecFactory class that can detect the compression format of an input file based on its extension, and return the appropriate CompressionCodec object. For example:

```java
CompressionCodecFactory factory = new CompressionCodecFactory(new Configuration());
CompressionCodec codec = factory.getCodec(inputPath); //inputPath is a Path object
```

- Hadoop also provides a CompressionInputStream and a CompressionOutputStream class that can be used to read and write compressed data from and to HDFS. For example:

```java
//To read a compressed file
CompressionCodec codec = ... //get the codec as above
CompressionInputStream in = codec.createInputStream(fs.open(inputPath)); //fs is a FileSystem object
//To write a compressed file
CompressionCodec codec = ... //get the codec as above
CompressionOutputStream out = codec.createOutputStream(fs.create(outputPath)); //fs is a FileSystem object
```

- Hadoop allows users to configure the compression codec and format for map output and reduce output. This can be done by setting the following properties in the Configuration object:

```java
//To enable map output compression
conf.setBoolean("mapreduce.map.output.compress", true);
//To specify the map output compression codec
conf.setClass("mapreduce.map.output.compress.codec", codecClass, CompressionCodec.class); //codecClass is the class name of the codec, such as org.apache.hadoop.io.compress.GzipCodec
//To enable reduce output compression
conf.setBoolean("mapreduce.output.fileoutputformat.compress", true);
//To specify the reduce output compression codec
conf.setClass("mapreduce.output.fileoutputformat.compress.codec", codecClass, CompressionCodec.class); //codecClass is the class name of the codec, such as org.apache.hadoop.io.compress.GzipCodec
//To specify the reduce output compression type
conf.set("mapreduce.output.fileoutputformat.compress.type", type); //type is either NONE, RECORD, or BLOCK
```

- A possible mnemonic to remember the compression codecs in Hadoop is: **Big Dogs Go Lick Lazy Snakes** (bzip2, DEFLATE, gzip, LZO, LZ4, Snappy).
- A possible learning trick to understand the trade-offs between compression codecs is: **The more you squeeze, the harder it gets** (higher compression ratio means slower speed and lower splittability).