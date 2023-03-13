 Here is the content in markdown format on the topic #### input formats in map reduce:

##### Input Formats in MapReduce

**TextInputFormat:**
<br>
- Reads input as lines of text.
- Suitable for text files.
- Each line is a record/key-value pair with the line as value and its offset as key.
- Mnemonic: Think of text file input, each line is a record.

**KeyValueTextInputFormat:**
<br>
- Reads input as lines of text in key-value format.
- Key and value are separated by a delimiter (tab or space by default).
- Suitable for input files in key-value format where key and value are separated by delimiters.
- Mnemonic: Think of key-value input, where each line has a key and value separated by delimiter.

**NLineInputFormat:**
<br>
- Splits input into chunks/splits of N lines.
- Suitable when processing records/lines in batches of size N is more efficient.
- Mnemonic: Think of N-line inputs, processed in batches of N lines.

**SequenceFileInputFormat:**
<br>
- Reads data from SequenceFiles (binary file format for MapReduce).
- Suitable for SequenceFile outputs of previous jobs.
- Mnemonic: Think of input in SequenceFile format.

**DBInputFormat:**
<br>
- Reads input from a database.
- Suitable for processing database tables via MapReduce.
- Complex implementation using JDBC and splitting logic.
- Mnemonic: Think of database input to MapReduce.

Advantages and examples of usage can be included for each input format. Disadvantages/limitations and comparisons can also be discussed. Detailed diagrams and codes can be added to aid understanding.
Applications of different formats in real-world use cases can be discussed to emphasize their relevance.