### Distributed Deadlock Detection

Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems. Deadlock detection in distributed systems seems to be the best approach to handle deadlocks in distributed systems .

Deadlock handling using the approach of deadlock detection entails addressing two basic issues: First, detection of existing deadlocks and second resolution of detected deadlocks .

Deadlock detection requires examination of the status of process-resource interactions for presence of cyclic wait . It may be identified via a distributed technique like edge chasing or by creating a global wait-for graph (WFG) from local wait-for graphs at a deadlock detector .

To resolve the deadlock, we have to abort a deadlocked process . Deadlocks can be dealt with using any one of the following three strategies: deadlock prevention, deadlock avoidance, and deadlock detection .

The techniques of deadlock detection in the distributed system require the following: Progress – The method should be able to detect all the deadlocks in the system. Safety – The method should not detect false or phantom deadlocks . There are three approaches to detect deadlocks in distributed systems .