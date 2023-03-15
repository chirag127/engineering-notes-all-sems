### Semaphores

- Semaphore is essentially a non-negative integer that is used to solve the critical section problem by acting as a signal.
- It is a concept in operating systems for the synchronization of concurrent processes.
- In an operating system, semaphores are used to control access to shared resources and to synchronize the actions of multiple tasks or threads.
- Semaphores are two-field data types, one of which is a non-negative type of integer S.V and the other is a set of processes in a queue S.L.
- It is used to address critical section problems by using two atomic operations, wait and signal, to synchronize processes in this.
- There are two main types of semaphores i.e. counting semaphores and binary semaphores.
- Semaphores allow only one process into the critical section. They follow the mutual exclusion.
- In computer science, a semaphore is a variable or abstract data type used to control access to a common resource by multiple threads and avoid critical section problems in a concurrent system such as a multitasking operating system.
- Semaphores are a type of synchronization primitive.
- Logically semaphore S is an integer variable that, apart from initialization can only be accessed through two atomic operations : Wait (S) or P : If the semaphore value is greater than 0, decrement the value. Otherwise, wait until the value is... Signal (S) or V : Increment the value of Semaphore.