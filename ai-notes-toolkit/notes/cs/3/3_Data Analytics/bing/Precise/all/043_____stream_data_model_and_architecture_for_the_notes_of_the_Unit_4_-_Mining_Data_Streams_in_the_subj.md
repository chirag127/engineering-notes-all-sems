# Stream Data Model and Architecture

### Introduction
- Stream data model and architecture is a framework that focuses on processing data in motion.
- It treats extract-transform-load (ETL) batch processing as just one more event in a continuous stream of events .
- Streaming data is becoming a core component of enterprise data architecture due to the explosive growth of data from non-traditional sources such as IoT sensors, security logs, and web applications.

### Components
- A streaming data architecture has three basic components:
  1. An aggregator that gathers event streams and batch files from a variety of data sources.
  2. A broker that makes data available for consumption.
  3. An analytics engine that analyzes the data, correlates values, and performs other tasks.

### Benefits
- The main benefit of stream processing is real-time insight.
- Data arrives in a stream or streams, and if it is not processed immediately or stored, then it is lost forever.
- The data arrives so rapidly that it is not feasible to store it all in active storage (i.e., in a conventional database), and then interact with it at the time of our choosing.

### Conclusion
- Stream data model and architecture is an important framework for processing data in motion.
- It has three basic components: an aggregator, a broker, and an analytics engine.
- The main benefit of stream processing is real-time insight.