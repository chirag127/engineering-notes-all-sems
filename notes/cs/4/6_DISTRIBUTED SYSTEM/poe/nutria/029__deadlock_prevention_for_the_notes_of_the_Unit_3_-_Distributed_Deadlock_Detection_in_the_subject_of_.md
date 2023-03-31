
### Deadlock Prevention

* Deadlock prevention is a technique used to avoid the occurrence of deadlock in a distributed system. 
* Deadlock can occur when resources are not properly managed and deadlock prevention techniques can be used to ensure that resources are managed in an efficient manner.
* Deadlock prevention techniques include: 
  * Mutual Exclusion: Resources are not shared between processes and each process is allocated exclusive access to the resources it needs. 
  * Hold and Wait: A process that requests a resource must wait until it has been released by the process that currently holds it. 
  * No Preemption: A process can only release a resource when it is finished with it. 
  * Circular Wait: A process must wait for a resource that is held by another process which is in turn waiting for a resource held by another process and so on. 
  * Resource Ordering: Resources are ordered and processes can only request resources in the order they are listed. 
  * Timeout: A process will wait for a certain amount of time before it is allowed to request a resource. 
  * Deadlock Avoidance: A process will not be allowed to request a resource if it will cause a deadlock.