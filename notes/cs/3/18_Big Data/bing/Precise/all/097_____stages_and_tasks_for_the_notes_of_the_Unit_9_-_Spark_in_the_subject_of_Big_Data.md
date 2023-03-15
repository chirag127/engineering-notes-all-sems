# Unit 9 - Spark

## Stages and Tasks

Apache Spark is a distributed computing system that processes large data sets in parallel across a cluster of computers. The processing of data in Spark is divided into stages and tasks.

### Stages

A stage is a collection of tasks that can be executed in parallel. Stages are created based on the dependencies between the transformations in the Spark application. Each stage contains a sequence of transformations that can be executed without any data shuffling.

### Tasks

A task is the smallest unit of work in Spark. Each task processes a partition of the data and applies the transformations defined in the stage. Tasks are executed in parallel across the cluster.

In summary, Spark divides the processing of data into stages and tasks. Stages are collections of tasks that can be executed in parallel, and tasks are the smallest units of work that process a partition of the data. This allows Spark to efficiently process large data sets in parallel across a cluster of computers.