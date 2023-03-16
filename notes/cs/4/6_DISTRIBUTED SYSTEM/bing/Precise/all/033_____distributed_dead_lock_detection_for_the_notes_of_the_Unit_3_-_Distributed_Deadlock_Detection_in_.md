# Distributed Deadlock Detection

Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems. Deadlock detection in distributed systems seems to be the best approach to handle deadlocks in distributed systems .

## Issues in Deadlock Detection

Deadlock handling using the approach of deadlock detection entails addressing two basic issues: First, detection of existing deadlocks and second resolution of detected deadlocks .

## Techniques for Deadlock Detection

Deadlock detection requires examination of the status of process-resource interactions for presence of cyclic wait. It may be identified via a distributed technique like edge chasing or by creating a global wait-for graph (WFG) from local wait-for graphs at a deadlock detector .

The techniques of deadlock detection in the distributed system require the following: Progress – The method should be able to detect all the deadlocks in the system. Safety – The method should not detect false or phantom deadlocks .

There are three approaches to detect deadlocks in distributed systems. They are as follows: deadlock prevention, deadlock avoidance, and deadlock detection .

In the deadlock avoidance approach to distributed systems, a resource is granted to a process if the resulting global system is safe. To resolve the deadlock, we have to abort a deadlocked process .

## Conclusion

Distributed deadlock detection is an important aspect of distributed systems. It involves detecting and resolving deadlocks in a distributed environment. Various techniques and approaches are available for detecting and resolving deadlocks in distributed systems. It is important to choose the right approach for the specific system and its requirements.