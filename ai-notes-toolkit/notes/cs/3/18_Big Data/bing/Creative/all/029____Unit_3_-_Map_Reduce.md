## Unit 3 - Map Reduce

- Map Reduce is a programming model and an associated implementation for processing and generating large data sets with a parallel, distributed algorithm on a cluster.
- The model is inspired by the map and reduce functions commonly used in functional programming, although their purpose in the Map Reduce framework is not the same as in their original forms.
- The key idea is to split the input data into independent chunks that are processed by the map functions in a completely parallel manner. The framework sorts the outputs of the maps, which are then input to the reduce functions. Typically both the input and the output of the job are stored in a file-system. The framework takes care of scheduling the tasks, monitoring them and re-executes the failed tasks.
- The Map Reduce model can be applied to many real-world problems, such as web indexing, data mining, machine learning, image processing, etc.
- The main advantages of the Map Reduce model are:
  - It abstracts the details of parallelization, fault-tolerance, data distribution and load balancing from the programmers.
  - It allows the programmers to write simple and scalable code using a high-level language of their choice.
  - It can handle very large data sets efficiently and reliably.
  - It can exploit the locality of data by processing it on or near the nodes where it is stored, reducing the network traffic and improving the performance.
- The main components of the Map Reduce framework are:
  - The Map Reduce library, which provides the interface for the programmers to define the map and reduce functions, and the configuration parameters for the job.
  - The Map Reduce master, which is responsible for splitting the input data, assigning the tasks to the workers, monitoring their progress and collecting the results.
  - The Map Reduce workers, which run the map or reduce tasks assigned by the master, and report their status and output to the master.
  - The distributed file system, which stores the input and output data of the job, and provides high availability and fault tolerance.