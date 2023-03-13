
### Map Reduce Types in Map Reduce

Map Reduce is a programming model used for processing large data sets. It is based on the divide-and-conquer approach, where a large problem is divided into smaller sub-problems, which are then solved independently. Map Reduce consists of two phases: the Map phase and the Reduce phase. 

#### Map Phase

The Map phase takes an input data set and processes it in parallel to produce a set of intermediate key-value pairs. The intermediate key-value pairs are then sorted and grouped by the same key. 

#### Reduce Phase

The Reduce phase takes the intermediate key-value pairs and processes them in parallel to produce a set of final output values. The output values are then written to the output data set. 

#### Mnemonics and Learning Tricks

- **M**ap **R**educe: **M**ap **R**educe divides the problem into smaller sub-problems and solves them independently. 
- **M**ap **P**hase: **M**ap **P**hase takes an input data set and produces a set of intermediate key-value pairs. 
- **R**educe **P**hase: **R**educe **P**hase takes the intermediate key-value pairs and produces a set of final output values. 

#### Advantages

- Map Reduce is a highly scalable model, as it can be easily distributed across multiple computers. 
- The Map Reduce model is highly fault tolerant, as it can easily handle node failures. 
- Map Reduce is highly efficient, as it can process large data sets in parallel. 

#### Disadvantages

- Map Reduce can be difficult to debug, as it is a distributed system. 
- Map Reduce is not suitable for iterative and interactive computations. 
- Map Reduce is not suitable for real-time applications.