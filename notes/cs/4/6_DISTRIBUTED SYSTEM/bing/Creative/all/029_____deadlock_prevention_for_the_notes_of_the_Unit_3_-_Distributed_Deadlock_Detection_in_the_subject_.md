# Deadlock Prevention for the Notes of the Unit 3 - Distributed Deadlock Detection in the Subject of Distributed System

A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process. In a distributed system, deadlocks are more difficult to detect and resolve because the processes and resources may be physically dispersed across different nodes.

Deadlock prevention is a technique to avoid the occurrence of deadlocks by ensuring that at least one of the four necessary conditions for deadlock (mutual exclusion, hold and wait, no preemption, and circular wait) is never satisfied.

There are two main methods of deadlock prevention in a distributed system:

- Ordered request
- Collective request

## Ordered Request

In this method, each resource type is assigned a certain level to maintain a resource request policy for a process. This is known as the resource allocation policy. The policy states that a process can request resources only in an increasing order of levels. For example, if there are three resource types A, B, and C with levels 1, 2, and 3 respectively, then a process can request A before B, and B before C, but not C before A or B.

This method prevents circular wait condition, as there is no cycle in the resource allocation graph. However, this method may be inefficient and impractical, as it may force a process to request resources that it does not need or to release resources that it still needs.

## Collective Request

In this method, a process must request all the resources it needs at the same time before starting execution. This is known as the atomic allocation policy. The policy states that a process can either get all the resources it requests or none of them. For example, if a process needs resources A, B, and C, then it must request them together and wait until they are all available.

This method prevents hold and wait condition, as a process does not hold any resources while waiting for others. However, this method may also be inefficient and impractical, as it may cause a lot of resource wastage and starvation.