### Cluster Middleware and SSI for the notes of the Unit 3 - Overview of Cluster Computing in the subject of High Performance Computing

- Cluster Middleware is the software layer that provides the necessary services and abstractions for cluster computing. It consists of two sub-layers: SSI Infrastructure and System Availability Infrastructure (SAI)  .
- SSI Infrastructure is the sub-layer that creates a Single System Image (SSI) for the cluster, which is the illusion of a single powerful resource that hides the heterogeneity and distribution of the underlying nodes   .
- SSI can be achieved at different levels, such as hardware, operating system, network, process, file system, and user interface. SSI can provide benefits such as ease of use, scalability, load balancing, and fault tolerance   .
- SAI is the sub-layer that provides cluster services such as check pointing, automatic failover, recovery from failure, and fault tolerance. SAI can enhance the reliability and availability of the cluster by detecting and handling node or network failures  .
- An example of a cluster middleware that supports SSI and SAI is OpenSSI, which is an open source project that extends the Linux kernel to create a single system image cluster. OpenSSI allows processes on different nodes to communicate using inter-process communication mechanisms as if they were running on the same machine, and also supports file system mirroring and process migration .

Some possible mnemonics and learning tricks for cluster middleware and SSI are:

- Cluster Middleware = SSI + SAI
- SSI = Single System Illusion
- SAI = Services for Availability and Integrity
- OpenSSI = Open Source SSI