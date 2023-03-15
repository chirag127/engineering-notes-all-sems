

#### Output Formats in Map Reduce

- **Text Output Format**: This is the default output format used in MapReduce. It writes the key-value pairs in plain text format, with the key and value separated by a tab character. 
- **SequenceFile Output Format**: This output format writes the key-value pairs to files in the Hadoop SequenceFile format. This format is more efficient than text output format, as it compresses the data and is splittable. 
- **KeyValueTextOutputFormat**: This output format is similar to Text Output Format, but it provides more control over the output. The key and value are separated by a user-defined separator. 
- **MultipleOutputs**: This output format allows the user to write to multiple outputs in the same MapReduce job. This is useful when the user needs to write to different output formats or to different locations. 
- **Avro Output Format**: This output format writes the key-value pairs to files in the Avro format. This format is splittable and provides better performance than text output format. 
- **Lazy Output Format**: This output format allows the user to write to files in a lazy manner. The data is written only when the MapReduce job is completed. This is useful when the user needs to write large datasets.
- **Mnemonics and Learning Tricks**: 
    - Text Output Format: TAB (Tabular)
    - SequenceFile Output Format: SQF (Sequence File)
    - KeyValueTextOutputFormat: KV (Key Value)
    - MultipleOutputs: MO (Multiple Outputs)
    - Avro Output Format: AOF (Avro Output Format)
    - Lazy Output Format: LOF (Lazy Output Format)