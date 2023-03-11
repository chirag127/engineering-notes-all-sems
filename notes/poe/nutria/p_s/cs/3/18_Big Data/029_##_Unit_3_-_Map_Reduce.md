
## Unit 3 - Map Reduce
Map Reduce is a programming model used to process large datasets on a distributed system. It is commonly used in big data analytics, where large datasets must be processed in parallel across multiple machines. Map Reduce was developed by Google in 2004 and has since become an industry standard for processing large datasets.

The Map Reduce model consists of two phases:

**Map Phase**: The Map phase is responsible for reading the input data, processing it, and producing a set of intermediate key-value pairs. The data is then sorted and partitioned into multiple parts.

**Reduce Phase**: The Reduce phase is responsible for taking the intermediate key-value pairs produced in the Map phase and aggregating them into a final output. This output is then written to a file or database.

Advantages of Map Reduce:
- High scalability: Map Reduce is designed to scale horizontally, meaning that more machines can be added to the cluster to increase the amount of data processed. 
- Fault tolerance: Map Reduce is designed to be fault tolerant, meaning that if one of the machines in the cluster fails, the data processing will still continue on the other machines.
- Cost effective: Map Reduce is cost effective because it allows for the use of commodity hardware and does not require specialized infrastructure.

Disadvantages of Map Reduce:
- Complexity: Map Reduce is a complex programming model and requires a good understanding of distributed computing to use effectively.
- Limited programming capabilities: Map Reduce is limited in its programming capabilities and does not support complex operations such as joins.
- Performance: Map Reduce can be slow for certain types of operations, such as sorting or searching.

Examples of Map Reduce:
- Google uses Map Reduce to process large datasets for its search engine.
- Amazon uses Map Reduce to process large datasets for its recommendation system.
- Facebook uses Map Reduce to process large datasets for its social network.

Applications of Map Reduce:
- Data Mining: Map Reduce can be used to process large datasets to find useful patterns and insights.
- Machine Learning: Map Reduce can be used to process large datasets to train machine learning models.
- Image Processing: Map Reduce can be used to process large datasets of images to detect objects or faces.