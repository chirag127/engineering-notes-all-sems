### Soft and Hard Real-Time Communication Systems

- Real-time communication systems are systems that exchange information between two or more entities within a specified time bound.
- Real-time communication systems are generally understood as one of two types: **Hard Real-Time (HRT)** and **Soft Real-Time (SRT)**.
- The difference between a hard and soft real-time communication system is the consequences of incorrect operation.
- In hard real-time communication systems, missing a deadline can be very costly or catastrophic; process control, nuclear reactor control, and air traffic control are some examples.
- In soft real-time communication systems, on the other hand, missed deadlines may lower the quality of service provided, but are not fatal; video streaming, voice over IP, and online gaming are some examples.
- Hard real-time communication systems require strict guarantees on the timeliness and reliability of the data transmission, and often use dedicated networks or protocols that can provide deterministic behavior and fault tolerance.
- Soft real-time communication systems can tolerate some degree of uncertainty and variability in the data transmission, and often use consumer networks or protocols that can provide best-effort service and adapt to changing network conditions.
- A large amount of soft real-time systems are telecommunications products such as VOIP systems and certain video calling platforms such as Discord and Google Meet.
- Some of the challenges and trade-offs involved in designing real-time communication systems are:
  - **Bandwidth**: the amount of data that can be transmitted per unit time; higher bandwidth means higher data rate and lower latency, but also higher cost and power consumption.
  - **Latency**: the delay between the source and the destination of the data; lower latency means faster response and higher accuracy, but also higher complexity and overhead.
  - **Jitter**: the variation in the latency of the data; higher jitter means lower predictability and stability, but also lower resource utilization and congestion.
  - **Reliability**: the probability that the data is transmitted without errors or losses; higher reliability means higher quality and robustness, but also higher redundancy and overhead.
  - **Security**: the protection of the data from unauthorized access or modification; higher security means higher privacy and integrity, but also higher encryption and overhead.

Some possible mnemonics and learning tricks for the topic are:

- To remember the difference between hard and soft real-time systems, you can use the acronym **HARD**:
  - **H**igh cost or catastrophic consequences of missing deadlines
  - **A**bsolute guarantees on timeliness and reliability
  - **R**igid and dedicated networks or protocols
  - **D**eterministic and fault-tolerant behavior
- To remember the challenges and trade-offs involved in designing real-time communication systems, you can use the acronym **BLJRS**:
  - **B**andwidth: data rate and latency
  - **L**atency: response and accuracy
  - **J**itter: predictability and stability
  - **R**eliability: quality and robustness
  - **S**ecurity: privacy and integrity
- To remember the examples of hard and soft real-time communication systems, you can use the following associations:
  - Hard real-time systems are often related to **safety** and **control**, such as process control, nuclear reactor control, and air traffic control.
  - Soft real-time systems are often related to **entertainment** and **communication**, such as video streaming, voice over IP, and online gaming.