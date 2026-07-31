
### Inter Process Communication – Semaphore 

* Semaphore is a synchronization primitive used to control access to a shared resource. It is a signaling mechanism used between processes or threads to communicate.
* Semaphores are of two types: counting semaphores and binary semaphores. 
* Counting semaphores are used to control access to a resource that can be used multiple times, such as a buffer or a queue. They are initialized with a count indicating the number of resources that can be used. 
* Binary semaphores are used to control access to a resource that can only be used once. They are initialized with a value of one and decremented to zero when the resource is used. 
* Semaphores are used to ensure that only one process or thread can access a resource at a time. This is done by having the process or thread wait until the semaphore is signaled. 
* Semaphores are also used to synchronize processes or threads. This is done by having the process or thread wait until the semaphore is signaled. 
* Semaphores can also be used to implement mutual exclusion, which ensures that only one process or thread can access a shared resource at a time. 
* Semaphores are an important part of any real-time operating system, as they are used to control access to shared resources and to synchronize processes and threads.