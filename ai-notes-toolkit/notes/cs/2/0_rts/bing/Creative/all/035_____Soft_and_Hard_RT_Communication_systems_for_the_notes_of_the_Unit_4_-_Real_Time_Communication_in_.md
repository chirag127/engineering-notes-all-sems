# Soft and Hard Real-Time Communication Systems

- Real-time communication systems are systems that exchange information between two or more entities within a specified time bound.
- Real-time communication systems are generally understood as one of two types: **Hard Real-Time (HRT)** and **Soft Real-Time (SRT)**.
- The difference between a hard and soft real-time communication system is the consequences of incorrect operation.
- A **hard real-time communication system** is a system that must meet its deadlines, otherwise it may cause catastrophic failure or unacceptable loss  . For example, a nuclear reactor control system, a flight control system, or a pacemaker system are hard real-time communication systems .
- A **soft real-time communication system** is a system that can tolerate some deadline misses, but still tries to achieve the best possible performance  . For example, a video conferencing system, a multimedia streaming system, or a web server are soft real-time communication systems .
- Hard real-time communication systems are **deterministic** in nature, meaning they can guarantee the worst-case execution time and response time for each task .
- Soft real-time communication systems are **probabilistic** in nature, meaning they can estimate the average or expected execution time and response time for each task, but not the worst-case .
- Hard real-time communication systems require **strict** scheduling algorithms and protocols that can ensure the timely delivery of messages and the avoidance of conflicts and deadlocks .
- Soft real-time communication systems can use **relaxed** scheduling algorithms and protocols that can adapt to the dynamic changes in the workload and the network conditions .
- Hard real-time communication systems have **higher** priority, reliability, and safety requirements than soft real-time communication systems .
- Soft real-time communication systems have **higher** flexibility, scalability, and efficiency requirements than hard real-time communication systems .