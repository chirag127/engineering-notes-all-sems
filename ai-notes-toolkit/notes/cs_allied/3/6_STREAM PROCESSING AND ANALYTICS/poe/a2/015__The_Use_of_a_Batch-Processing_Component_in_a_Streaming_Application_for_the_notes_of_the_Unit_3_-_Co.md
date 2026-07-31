 Here are the points I have noted for the given topic:

### The Use of a Batch-Processing Component in a Streaming Application

1. Batch processing can be used in a streaming application for certain types of processing that are more efficient in batch mode.
2. Batch processing may be better suited for machine learning model training or complex analytics that require iterating over a large amount of data.
3. The batch processing component can receive data from the streaming application's streaming inputs, perform the batch processing, and then output results back to the streaming application.
4. The outputs from the batch processing may be used to update models or parameters in the streaming application, or may be processed as a special type of event.
5. Care must be taken to ensure that the batch processing can keep up with the rate of data incoming to the streaming application so that it does not become a bottleneck. The batch window size and frequency of batch executions need to be tuned for performance.
6. Using a combination of streaming and batch processing in this way allows leveraging the advantages of both approaches and can enable more sophisticated processing than streaming alone.

The points are written in a formal tone with no emojis or external links as per the given instructions. The content is written in Markdown format with headings and points. Please let me know if you would like me to modify or expand the answer.