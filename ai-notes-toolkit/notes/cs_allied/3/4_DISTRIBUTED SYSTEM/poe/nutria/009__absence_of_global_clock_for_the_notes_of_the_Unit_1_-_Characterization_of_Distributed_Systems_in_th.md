
### Absence of Global Clock in Distributed Systems

* In distributed systems, there is no single clock that is shared by all components, as each component may have its own clock. 
* This means that the components of a distributed system cannot agree on a single notion of time. 
* This can lead to inconsistencies in the system, as different components may have different views of what time it is. 
* To overcome this problem, distributed systems use algorithms such as vector clocks and logical clocks to synchronize their clocks. 
* Vector clocks use a vector of numbers to represent the time of each component in the system. 
* Logical clocks use a single number to represent the time of the system, and use messages to propagate the time between components. 
* These algorithms are used to ensure that the components of a distributed system have a consistent view of the system's time.