### MapReduce

- MapReduce is a framework for processing parallelizable problems across large datasets using a large number of computers (nodes), collectively referred to as a cluster or a grid.
- The MapReduce framework consists of a single master ResourceManager, one worker NodeManager per cluster-node, and MRAppMaster per application.
- The MapReduce framework is usually composed of three operations (or steps): Map, Reduce, and Shuffle .
  - Map: each worker node applies the map function to the local data, and writes the output to a temporary storage. A master node ensures that only one copy of the redundant input data is processed.
  - Shuffle: the worker nodes redistribute the data based on the output keys (produced by the map function), such that all data belonging to one key is located on the same worker node.
  - Reduce: the worker nodes now process each group of output data, per key, in parallel. The reduce function is then applied to each group, which in turn produces a collection of values for each key.
- The MapReduce framework orchestrates the processing by marshalling the distributed servers, running the various tasks in parallel, managing all communications and data transfers between the various parts of the system, and providing for redundancy and fault tolerance.
- The MapReduce framework is designed to scale up from single servers to thousands of machines, each offering local computation and storage.
- The MapReduce framework is widely used for data analysis, data mining, machine learning, and other applications that require processing large volumes of data in parallel.