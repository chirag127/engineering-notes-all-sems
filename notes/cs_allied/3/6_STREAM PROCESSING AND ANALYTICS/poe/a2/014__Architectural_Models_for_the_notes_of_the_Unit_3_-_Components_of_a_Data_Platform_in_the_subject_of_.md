 Here is the content in Markdown format without any emojis or external links and in a formal tone:

### Architectural Models for the notes of the Unit 3 - Components of a Data Platform in the subject of STREAM PROCESSING AND ANALYTICS

1. Lambda Architecture:
- Divides the system into 3 layers: Batch layer, Speed layer and Serving layer
- Batch layer: Handle complex, long running computations on all data
- Speed layer: Performs fast but simple computations on recent data
- Serving layer: Indexes and serves results from batch and speed layers
- Pros: fault tolerance, handles both batch and real-time computation
- Cons: More complex, requires maintaining multiple systems

2. Kappa Architecture:
- A single layer that handles both batch and real-time data using a unified stream processing system
- Pros: Simplicity, avoids the complexity of running and coordinating multiple separate systems
- Cons: Difficulty in implementing complex, long running batch tasks with low latency constraints

3. Streaming Only Architecture:
- Focuses on processing data continuously as streams
- Pros: Natural fit for data that is inherently continuous like sensor data or web interaction data
- Cons: Requires conversion of batch data and tasks to streaming equivalents which may not always be straightforward

The above points summarize the key Architectural Models for handling both batch and real-time data processing requirements. The selection of a suitable model depends on the nature of the data and use cases. A streaming only model may be sufficient for continuous data while a Lambda architecture could be more appropriate for a mix of long running batch tasks and real-time requirements.