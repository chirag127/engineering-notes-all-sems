##### Compression in Hadoop io

- Compression is the process of reducing the size of data by applying a compression algorithm or codec.
- Compression can save disk space, network bandwidth, and processing time in Hadoop.
- Hadoop supports various compression codecs, such as DEFLATE, gzip, bzip2, LZO, LZ4, and Snappy.
- Compression can be applied at different levels in Hadoop, such as input, output, intermediate, and shuffle.
- Input compression refers to compressing the input files before loading them into HDFS. This can reduce the disk space and network transfer required to store and load the files. However, not all compression codecs are splittable, meaning that they can be processed in parallel by multiple map tasks. Only bzip2 is splittable among the standard codecs. Splittable codecs can improve the performance and scalability of mapreduce jobs.
- Output compression refers to compressing the output files after the mapreduce job is completed. This can reduce the disk space and network transfer required to store and retrieve the output files. Output compression can be enabled by setting the property `mapreduce.output.fileoutputformat.compress` to `true` and specifying the compression codec in `mapreduce.output.fileoutputformat.compress.codec`.
- Intermediate compression refers to compressing the intermediate output of the map tasks before sending them to the reduce tasks. This can reduce the network transfer and disk I/O required for the shuffle phase. Intermediate compression can be enabled by setting the property `mapreduce.map.output.compress` to `true` and specifying the compression codec in `mapreduce.map.output.compress.codec`.
- Shuffle compression refers to compressing the data transferred between the map and reduce tasks during the shuffle phase. This can reduce the network bandwidth and disk I/O required for the shuffle phase. Shuffle compression can be enabled by setting the property `mapreduce.reduce.shuffle.input.buffer.percent` to a value less than 1.0 and specifying the compression codec in `mapreduce.reduce.shuffle.compress.codec`.
- Hadoop provides a `CompressionCodecFactory` class that can detect the compression format of a file based on its extension and provide the appropriate `CompressionCodec`. For example, the following code snippet can be used to get the compression codec for a file:

```java
CompressionCodecFactory factory = new CompressionCodecFactory(new Configuration());
CompressionCodec codec = factory.getCodec(inputPath); //inputPath is a Path object
```

- Hadoop also provides a `FileOutputFormat` class that can automatically compress the output files based on the configuration properties. For example, the following code snippet can be used to set the output format and compression codec for a mapreduce job:

```java
job.setOutputFormatClass(TextOutputFormat.class); //set the output format
FileOutputFormat.setCompressOutput(job, true); //enable output compression
FileOutputFormat.setOutputCompressorClass(job, GzipCodec.class); //set the compression codec
```

- Compression can have trade-offs between space, time, and CPU usage. Different compression codecs have different compression ratios, compression speeds, and decompression speeds. Generally, higher compression ratios mean lower compression and decompression speeds, and higher CPU usage. Therefore, choosing the appropriate compression codec depends on the use case and the data characteristics.
- A mnemonic to remember the standard compression codecs in Hadoop is **D**on't **G**et **B**ored, **L**et's **L**earn **S**omething:

  - **D**EFLATE
  - **G**zip
  - **B**zip2
  - **L**ZO
  - **L**Z4
  - **S**nappy

- A learning trick to compare the compression codecs in Hadoop is to use the following table:

| Codec   | Compression ratio | Compression speed | Decompression speed | Splittable | CPU usage |
|---------|-------------------|-------------------|---------------------|------------|-----------|
| DEFLATE | Medium            | Medium            | Medium              | No         | Medium    |
| gzip    | High              | Low               | Medium              | No         | High      |
| bzip2   | Very high         | Very low          | Low                 | Yes        | Very high |
| LZO     | Low               | High              | High                | No*        | Low       |
| LZ4     | Low               | Very high         | Very high           | No         | Very low  |
| Snappy  | Low