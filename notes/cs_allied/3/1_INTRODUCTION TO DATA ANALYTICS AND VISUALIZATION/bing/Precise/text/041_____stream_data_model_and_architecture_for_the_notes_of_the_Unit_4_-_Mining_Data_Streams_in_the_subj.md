### Stream Data Model and Architecture

- A **streaming data architecture** is an information technology framework that focuses on processing data in motion and treats extract-transform-load (ETL) batch processing as just one more event in a continuous stream of events .
- This type of architecture has three basic components:
  1. An **aggregator** that gathers event streams and batch files from a variety of data sources.
  2. A **broker** that makes data available for consumption.
  3. An **analytics engine** that analyzes the data, correlates values, and performs other processing tasks .
- Streaming data is becoming a core component of enterprise data architecture due to the explosive growth of data from non-traditional sources such as IoT sensors, security logs, and web applications .
- In a stream data model, data arrives in a stream or streams, and if it is not processed immediately or stored, then it is lost forever. The data arrives so rapidly that it is not feasible to store it all in active storage (i.e., in a conventional database), and then interact with it at the time of our choosing .
- The main benefit of stream processing is real-time insight .