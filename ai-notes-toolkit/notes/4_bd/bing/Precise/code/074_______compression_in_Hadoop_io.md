##### Compression in Hadoop IO

Hadoop provides support for various compression codecs and formats. Here is an example of how to compress and decompress data using the `GzipCodec` in Hadoop:

```java
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IOUtils;
import org.apache.hadoop.io.compress.CompressionCodec;
import org.apache.hadoop.io.compress.CompressionCodecFactory;
import org.apache.hadoop.io.compress.GzipCodec;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.OutputStream;

public class CompressionExample {
    public static void main(String[] args) throws Exception {
        String inputPath = args[0];
        String outputPath = args[1];

        Configuration conf = new Configuration();
        CompressionCodecFactory factory = new CompressionCodecFactory(conf);
        CompressionCodec codec = factory.getCodec(new Path(outputPath));
        if (codec == null) {
            System.err.println("No codec found for " + outputPath);
            System.exit(1);
        }

        InputStream in = null;
        OutputStream out = null;
        try {
            in = new FileInputStream(inputPath);
            out = codec.createOutputStream(new FileOutputStream(outputPath));
            IOUtils.copyBytes(in, out, conf);
        } finally {
            IOUtils.closeStream(in);
            IOUtils.closeStream(out);
        }
    }
}
```

This code reads data from the input path, compresses it using the `GzipCodec`, and writes the compressed data to the output path. To decompress the data, you can use the `createInputStream` method of the codec instead of the `createOutputStream` method.