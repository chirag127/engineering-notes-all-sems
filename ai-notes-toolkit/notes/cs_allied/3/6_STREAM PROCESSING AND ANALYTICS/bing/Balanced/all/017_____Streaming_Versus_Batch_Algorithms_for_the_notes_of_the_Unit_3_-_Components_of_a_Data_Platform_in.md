# Streaming Versus Batch Algorithms

Streaming and batch algorithms are two different approaches to processing data in a data platform. They differ in how they handle the data, the latency, the scalability, and the use cases.

## How they handle the data

- Batch processing refers to processing of high volume of data in batch within a specific time span. It requires a set of data collected over time, then fed into an analytics system. It processes over all or most of the data.
- Stream processing refers to processing of continuous stream of data immediately as it is produced. It requires data to be fed into an analytics tool, often in micro-batches, and in real-time. It processes over data on a rolling window or most recent record.

## The latency

- Batch processing has high latency, meaning it takes longer to get the results from the data. It can range from minutes to hours to days, depending on the size and frequency of the batches.
- Stream processing has low latency, meaning it delivers the results from the data quickly. It can range from milliseconds to seconds, depending on the speed and complexity of the processing.

## The scalability

- Batch processing is scalable, meaning it can handle large volumes of data or data sources from legacy systems, where it’s not feasible to deliver data in streams. It can also leverage parallel processing and distributed computing to speed up the processing.
- Stream processing is also scalable, meaning it can handle high velocity and variety of data from modern sources, such as sensors, web logs, social media, etc. It can also leverage stateful processing and fault tolerance to ensure the accuracy and reliability of the processing.

## The use cases

- Batch processing is often used for offline analytics, such as historical reporting, data warehousing, data mining, machine learning, etc. It is suitable for scenarios where the data is static, the accuracy is more important than the timeliness, and the processing is complex.
- Stream processing is often used for real-time analytics, such as dashboarding, alerting, monitoring, streaming ETL, etc. It is suitable for scenarios where the data is dynamic, the timeliness is more important than the accuracy, and the processing is simple.