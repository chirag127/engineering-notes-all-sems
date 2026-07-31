# Prediction with Partial Match (PPM) for Data Compression

- Prediction by partial matching (PPM) is an adaptive statistical data compression technique based on context modeling and prediction  .
- PPM models use a set of previous symbols in the uncompressed symbol stream to predict the next symbol in the stream  .
- PPM algorithms can also be used to cluster data into predicted groupings in cluster analysis  .
- PPM works by maintaining a variable-length history of the most recent symbols, called the context, and using it to look up the probability distribution of the next symbol in a table .
- The table is updated dynamically as new symbols are encountered, and the context is adjusted accordingly .
- PPM can achieve high compression ratios by exploiting the redundancy and regularity in natural language and other data sources .
- PPM has several variants, such as PPM-A, PPM-B, PPM-C, PPM-D, PPM-Z, etc., that differ in how they handle the cases when the context is not found in the table or when the predicted symbol is not in the distribution .
- PPM is a generalization of the Markov model and the arithmetic coding techniques .