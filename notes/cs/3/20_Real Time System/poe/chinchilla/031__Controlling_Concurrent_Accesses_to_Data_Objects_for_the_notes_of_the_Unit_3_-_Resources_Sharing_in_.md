### Controlling Concurrent Accesses to Data Objects

In Real Time Systems, it is common for multiple tasks to access the same data objects concurrently. This can lead to data inconsistency and race conditions, which can cause serious problems in the system. Therefore, it is important to control concurrent accesses to data objects. In this unit, we will discuss various techniques for controlling concurrent accesses to data objects.

#### Mutual Exclusion

Mutual exclusion is a technique that ensures that only one task can access a data object at a time. There are several ways to implement mutual exclusion:

- **Locking:** A lock is a mechanism that prevents other tasks from accessing a data object while it is being used by a task. When a task needs to access a data object, it must first acquire the lock. Other tasks that try to access the same data object while it is locked will be blocked until the lock is released.

- **Semaphore:** A semaphore is a variable that is used to control access to a shared resource. It is similar to a lock, but it can be used to allow multiple tasks to access the same resource concurrently. A semaphore has a count that is initially set to the number of available resources. When a task needs to access the resource, it must first decrement the count. If the count becomes zero, the task will be blocked until the resource becomes available again.

#### Priority Inversion

Priority inversion is a problem that can occur when a low-priority task holds a lock or a semaphore that a high-priority task needs to access. This can cause the high-priority task to be blocked, which can lead to a decrease in system performance. There are several ways to prevent priority inversion:

- **Priority Inheritance:** Priority inheritance is a technique that ensures that a task that holds a lock or a semaphore will inherit the priority of the highest-priority task that is blocked waiting for the lock or semaphore. This prevents priority inversion by temporarily raising the priority of the low-priority task.

- **Priority Ceiling:** Priority ceiling is a technique that assigns a priority ceiling to each lock or semaphore. The priority ceiling is the highest priority of any task that can access the lock or semaphore. When a task acquires a lock or semaphore, its priority is raised to the priority ceiling of the lock or semaphore. This prevents priority inversion by ensuring that a task cannot be blocked by a lower-priority task that holds a lock or semaphore.

#### Deadlocks

Deadlocks are situations where two or more tasks are blocked waiting for each other to release resources. Deadlocks can be prevented by using the following techniques:

- **Resource Ordering:** Resource ordering is a technique that requires tasks to acquire resources in a specific order. This prevents deadlocks by ensuring that tasks cannot be blocked waiting for resources that are held by other tasks that are waiting for resources that they hold.

- **Timeouts:** Timeouts are a technique that allows tasks to give up waiting for resources after a certain amount of time has passed. This prevents deadlocks by ensuring that tasks cannot be blocked indefinitely waiting for resources that may never become available.

In conclusion, controlling concurrent accesses to data objects is an important aspect of Real Time Systems. Techniques such as mutual exclusion, priority inheritance, priority ceiling, resource ordering, and timeouts can be used to prevent data inconsistency, race conditions, priority inversion, and deadlocks. It is important to choose the appropriate technique based on the specific requirements of the system.