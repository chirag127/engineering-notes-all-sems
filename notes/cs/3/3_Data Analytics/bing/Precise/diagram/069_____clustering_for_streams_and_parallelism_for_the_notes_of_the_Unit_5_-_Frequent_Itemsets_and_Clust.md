# Clustering for Streams and Parallelism

Clustering for streams and parallelism refers to the process of grouping multiple streams with similar behavior and trend together, instead of clustering the data records within one data stream . This is different from some previous studies on clustering stream data.

A data stream can be thought of as a transient, continuously increasing sequence of time-stamped data . The goal is to cluster parallel streams of real-valued data, that is to say, continuously evolving time series .

In the literature of data stream clustering methods, a large number of algorithms use a two-phase scheme which consists of an online component that processes data stream points and produces summary statistics, and an offline component that uses the summary data to generate the clusters .

One proposed algorithm for clustering multiple data streams is based on correlation analysis. Performing correlation analysis on data streams under the one-scan requirement poses significant technical challenges since the raw data cannot be stored .