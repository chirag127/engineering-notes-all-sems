#### Map Reduce framework and basics

- Map Reduce is a programming model or pattern within the Hadoop framework that is used to access big data stored in the Hadoop File System (HDFS) .
- Map Reduce is a core component, integral to the functioning of the Hadoop framework .
- Map Reduce facilitates concurrent processing by splitting petabytes of data into smaller chunks, and processing them in parallel on Hadoop commodity servers .
- Map Reduce consists of two distinct tasks – Map and Reduce .
- The Map task takes input data, and maps it to <key, value> pairs according to the user specifications .
- The Reduce task takes a collection of <key, value> pairs and “reduces” them according to the user-specified reduce function .
- The Map Reduce framework consists of a single master ResourceManager, one worker NodeManager per cluster-node, and MRAppMaster per application .
- The Map Reduce framework handles the input/output locations and the distribution of data and tasks across the cluster .
- Map Reduce can be used for various applications, such as log analysis, full-text indexing, web-link graph traversal, machine learning, etc. .