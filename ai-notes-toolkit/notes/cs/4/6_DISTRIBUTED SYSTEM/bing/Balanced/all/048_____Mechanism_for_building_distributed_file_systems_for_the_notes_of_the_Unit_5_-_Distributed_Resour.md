# Mechanism for building distributed file systems

A distributed file system (DFS) is a file system that is distributed on multiple file servers or locations. It allows programs to access or store isolated files as they do with the local ones, allowing programmers to access files from any network or computer.

The mechanism for building a DFS involves the following aspects:

- Use of file models: The DFS uses different conceptual models of a file. The following are the two basic criteria for file modeling, which include file structure and modifiability. The files can be unstructured or structured based on the applications used in file systems. The files can also be immutable or mutable depending on whether they can be modified or not.
- Use of file accessing models: A DFS may use one of the following models to service a client’s file request:
  - Upload/download model: The client downloads the entire file from the server, modifies it locally, and uploads it back to the server.
  - Remote access model: The client accesses the file on the server through remote procedure calls (RPCs) or remote method invocations (RMIs).
  - Remote service model: The client sends a request to the server, which performs the file operation and returns the result to the client.
- Use of file replication: File replication is the primary mechanism for improving file availability and performance in a DFS. A replicated file is a file that has multiple copies with each copy located on a separate file server. The challenges of file replication include:
  - Consistency: The replicated copies of a file should be consistent with each other, meaning that they should reflect the same state of the file.
  - Location: The location of the replicated copies of a file should be transparent to the client, meaning that the client should not need to know where the copies are stored.
  - Update: The update of a replicated file should be propagated to all the copies, meaning that any change made to one copy should be reflected on the others.
- Use of file caching: File caching is another mechanism for improving file performance and reducing network traffic in a DFS. File caching is the process of storing a copy of a file or a part of a file in a local memory or disk for faster access. The challenges of file caching include:
  - Coherency: The cached copy of a file should be coherent with the original file, meaning that they should have the same content and metadata.
  - Consistency: The cached copy of a file should be consistent with the other cached copies, meaning that they should reflect the same state of the file.
  - Replacement: The replacement of a cached copy of a file should be done according to some policy, meaning that the system should decide which copy to evict when the cache is full.
- Use of file naming: File naming is the mechanism for identifying and locating files in a DFS. File naming involves the following components:
  - File name: A file name is a string of characters that uniquely identifies a file within a namespace.
  - Namespace: A namespace is a collection of file names that are organized in a hierarchical or flat structure.
  - Name resolution: Name resolution is the process of mapping a file name to a file location or a file identifier.
  - Name service: A name service is a component that provides name resolution and name management functions for a DFS.

: Mechanism for building Distributed file system - GeeksforGeeks. Retrieved from https://www.geeksforgeeks.org/mechanism-for-building-distributed-file-system/