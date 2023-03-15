### Composite source model

- A composite source model is a way of describing a complex source of data using multiple simpler sources and a switch that selects one of them at a time.
- A composite source can be represented as a number of individual sources S i, each with its own model M i and a switch that selects a source S i with probability P i.
- A composite source model is useful for applications where a single model is not adequate to capture the characteristics of the data, such as text, speech, images, etc.
- A composite source model can be used to achieve better data compression by exploiting the correlations and redundancies among the different sources.
- A composite source model can be implemented using different techniques, such as:
  - Concatenating the outputs of the individual sources and encoding them as a single stream.
  - Encoding each source separately and transmitting them along with the switch information.
  - Using a universal code that can adapt to the changes in the source statistics.
- A composite source model can also be combined with other data reduction techniques, such as:
  - Import modeling, which involves loading the source data into memory and compressing it using the VertiPaq storage engine.
  - DirectQuery, which involves connecting to the source data without importing it and querying it on demand .
  - Composite modeling, which involves connecting to multiple sources with different modes (import or DirectQuery) and creating relationships among them .

: Data compression Interview Questions & Answers
: Data reduction techniques for Import modeling - Power BI
: Briefly explain Modeling and coding with respect to data compression
: Use composite models in Power BI Desktop - Power BI
: Composite Model in Power BI; DirectQuery and Import Data Combined