# Case studies for the notes of the Unit 4 - Mining Data Streams in the subject of Data Analytics

Mining data streams is the process of extracting knowledge structures represented in models and patterns from continuous and unbounded streams of information. Data stream mining has many applications and challenges in various domains, such as network monitoring, sensor networks, web mining, social media analysis, etc. In this unit, we will review some case studies for mining data streams, based on the following sources:

- A Case Study: Stream Data Mining Classification by Ketan Desale (2015)
- Data Streams in Data Mining Simplified 101 by Hevo (2020)
- Mining Data Streams: A Review by Charu C. Aggarwal et al. (2005)
- Improvised methods for tackling big data stream mining challenges: case study of online shopper’s purchasing intention prediction by N. A. M. Isa et al. (2016)
- DATA STREAM MINING by Albert Bifet et al. (2010)
- An update on global mining land use by Laura Sonter et al. (2022)

## Case Study 1: Stream Data Mining Classification

- This case study presents a stream data mining classification task, where the goal is to predict the class label of a stream of data instances based on their features.
- The data stream is generated from a synthetic dataset called SEA, which contains three features and two classes. The features are numerical and the classes are binary. The dataset has 60,000 instances and 3 concept drifts, where the underlying distribution of the data changes over time.
- The case study compares four stream data mining classification algorithms: Naive Bayes, Hoeffding Tree, Adaptive Random Forest, and Online Bagging. The performance of the algorithms is measured by accuracy, kappa statistic, and memory usage.
- The results show that Adaptive Random Forest and Online Bagging have the best accuracy and kappa statistic, while Naive Bayes and Hoeffding Tree have the lowest memory usage. The results also show that the algorithms can adapt to the concept drifts in the data stream.

## Case Study 2: Data Streams in Data Mining Simplified 101

- This case study provides an overview of the basic concepts and techniques of data streams in data mining, such as data stream models, data stream processing, data stream mining algorithms, and data stream mining applications.
- The data stream models are classified into two types: landmark windows and sliding windows. Landmark windows are fixed from the beginning of the stream and contain all the data seen so far. Sliding windows are dynamic and contain only the most recent data in the stream.
- The data stream processing is divided into two phases: online processing and offline processing. Online processing is done in real-time and involves filtering, aggregation, sampling, and sketching of the data stream. Offline processing is done periodically and involves mining, analysis, and visualization of the data stream.
- The data stream mining algorithms are categorized into four types: classification, clustering, frequent pattern mining, and outlier detection. Classification is the task of predicting the class label of a data instance based on its features. Clustering is the task of grouping similar data instances together based on their features. Frequent pattern mining is the task of finding frequent and interesting patterns or associations among the data instances. Outlier detection is the task of identifying data instances that deviate significantly from the normal behavior of the data stream.
- The data stream mining applications are numerous and span various domains, such as network monitoring, sensor networks, web mining, social media analysis, etc. Some examples of data stream mining applications are:

  - Network monitoring: detecting intrusions, anomalies, and attacks in network traffic data streams.
  - Sensor networks: monitoring environmental, health, and security conditions in sensor data streams.
  - Web mining: analyzing user behavior, preferences, and trends in web data streams.
  - Social media analysis: extracting sentiment, opinion, and emotion from social media data streams.

## Case Study 3: Mining Data Streams: A Review

- This case study presents a comprehensive review of the research in data stream mining, covering the challenges, techniques, and applications of data stream mining.
- The challenges of data stream mining are mainly related to the characteristics of data streams, such as infinite size, high speed, dynamic nature, and noisy and uncertain quality. Some of the challenges are:

  - Memory management: how to store and access the data stream efficiently and effectively in limited memory space.
  - Processing speed: how to process and mine the data stream in real-time and keep up with the data arrival rate.
  - Concept drift: how to handle the