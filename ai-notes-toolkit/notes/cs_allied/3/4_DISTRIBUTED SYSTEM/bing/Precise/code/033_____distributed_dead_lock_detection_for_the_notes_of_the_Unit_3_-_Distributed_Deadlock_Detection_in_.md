### Distributed Deadlock Detection

Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems. Deadlock detection in distributed systems seems to be the best approach to handle deadlocks in distributed systems .

#### Issues in Deadlock Detection
Deadlock handling using the approach of deadlock detection entails addressing two basic issues: First, detection of existing deadlocks and second resolution of detected deadlocks .

#### Techniques for Deadlock Detection
Deadlocks can be dealt with using any one of the following three strategies: deadlock prevention, deadlock avoidance, and deadlock detection . Deadlock detection requires an examination of the status of the process–resources interaction for the presence of a deadlock condition . It may be identified via a distributed technique like edge chasing or by creating a global wait-for graph (WFG) from local wait-for graphs at a deadlock detector .

#### Requirements for Deadlock Detection Techniques
The techniques of deadlock detection in the distributed system require the following: Progress – The method should be able to detect all the deadlocks in the system. Safety – The method should not detect false or phantom deadlocks .

#### Conclusion
In conclusion, distributed deadlock detection is an important aspect of distributed systems and various techniques and approaches can be used to detect and resolve deadlocks. It is important to choose a technique that is both safe and progressive in detecting deadlocks.