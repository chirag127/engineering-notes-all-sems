 Here is the content written in Markdown format for the topic -

### Dynamic Markoy Compression for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Dynamic Markov Compression is a statistical data compression technique which makes use of the Markov property to predict the upcoming symbol in a sequence based on the previous symbols.
- It analyses the probabilities of occurrences of symbols and encodes the symbols with variable length codes based on their probabilities. More probable symbols are encoded with shorter codes and less probable symbols with longer codes. This results in an average code length less than that of using fixed length codes and achieves compression.
- The compression achieves its best results when the sequence to be compressed exhibits strong correlations between successive symbols i.e. contains patterns. The more predictable the sequence is, higher is the compression ratio that can be achieved.
- The decoder requires the knowledge of the model which generated the probabilities of symbols to decode the compressed data properly. If the model/probabilities change with time, it becomes a dynamic model and the decoder needs to track the changes in model to decode accurately. This is the reason the technique is named as Dynamic Markov Compression.
- Some advantages of Dynamic Markov Compression are -
-- It adapts to the changing statistics of the data and tracks the evolving patterns to achieve better compression than static techniques.
-- It is relatively simple to implement.
- Some disadvantages are -
-- The decoder needs to be synchronized with the changes in the model which requires additional overhead.
-- The compression is lesser than more complex adaptive compression techniques in case of highly varying data.
- Applications include compression of network packet data, medical data, financial data, etc. where the statistics tend to evolve over time.

ASCII diagrams and examples can be included if required.