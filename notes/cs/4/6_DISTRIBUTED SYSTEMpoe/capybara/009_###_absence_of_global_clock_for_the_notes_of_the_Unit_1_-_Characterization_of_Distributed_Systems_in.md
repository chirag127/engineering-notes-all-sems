### Absence of Global Clock for the Notes of Unit 1 - Characterization of Distributed Systems in the Subject of Distributed System

In distributed systems, clocks are used to order events that occur on different nodes. However, due to the absence of a global clock, it becomes challenging to order events accurately. In this section, we will discuss the absence of a global clock and its impact on distributed systems.

#### What is a Global Clock?

A global clock is a clock that is synchronized across all nodes in a distributed system. It can be used to order events that occur on different nodes in the system. In other words, it provides a common time reference for all the nodes.

#### Absence of Global Clock

In a distributed system, there is no way to synchronize clocks across all the nodes. This is because the nodes are geographically dispersed and may have different clock speeds. As a result, there is no global clock in the system.

#### Impact of Absence of Global Clock

The absence of a global clock has several implications for distributed systems. Some of these are:

- Ordering of events becomes difficult: Without a global clock, it becomes challenging to order events that occur on different nodes accurately. This can lead to inconsistencies in the system.

- Timing-related issues: In the absence of a global clock, timing-related issues can occur. For example, two events that occur on different nodes may appear to occur at the same time, leading to confusion.

- Difficulty in debugging: The absence of a global clock can make it challenging to debug issues in a distributed system. This is because it becomes difficult to trace the sequence of events that led to the issue.

#### Learning Trick

To remember the impact of the absence of a global clock, you can use the mnemonic "OTD" which stands for Ordering, Timing, and Debugging. This will help you remember the three main implications of the absence of a global clock in a distributed system.

In conclusion, the absence of a global clock in a distributed system can lead to several issues related to ordering, timing, and debugging. It is essential to understand these implications to design and develop robust distributed systems.