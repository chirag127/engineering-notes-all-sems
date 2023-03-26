 Here is the content in Markdown format with formal tone and without emojis or external links:

## Unit 2 - Stream-Processing Model

1. Introduction
- A stream-processing model treats data as a continuous flow of information to be processed in real-time.
- Data is received and processed sequentially rather than being stored in its entirety before processing.
- This model is useful for applications that require low-latency processing of unbounded data streams.

2. Applications
- Real-time analytics on user activity streams, server logs, etc.
- Fraud detection on financial transactions
- Monitoring network activity for security threats
- Processing IoT data streams for alerts or control systems

3. Components
- Data source - Produces a continuous stream of data
- Processor - Performs transformations or analysis on data streams
- Sink - Consumes output of processors, could be storage or another processor

4. Characteristics
- Unbounded data - Potentially infinite streams with no defined end
- Low latency - Processes data quickly as it is received with limited delay
- Scalability - Able to handle growth in data volume and number of streams
- Fault tolerance - Must continue operating correctly even with component failures or delays

5. Technologies
- Apache Kafka - Popular open-source stream-processing platform using publish-subscribe model
- Apache Flink - Open-source stream-processing framework with low latency and high throughput
- Apache Spark Streaming - Extension of Spark for streaming analytics on data streams
- AWS Kinesis - Managed cloud service to process and analyze streaming data