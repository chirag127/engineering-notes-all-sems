# Concurrency Control for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- Concurrency is the tendency for things to happen at the same time in a system.
- Concurrency is a natural phenomenon, of course. In the real world, at any given time, many things are happening simultaneously.
- When we design software to monitor and control real-world systems, we must deal with this natural concurrency.
- Real-time systems (RTS) respond to their environment within specified time constraints.
- RTS are inherently concurrent and typically manage shared data resources, so they require synchronization to ensure both logical and timing correctness.
- Much research in managing shared data has been carried out in the context of database systems.
- Database systems use concurrency control techniques to ensure that concurrent transactions do not interfere with each other and preserve the consistency of the data.
- However, concurrency control techniques can seldom be transferred from database to the real-time domain without change; the performance considerations are too different.
- We discuss common features and differences between the two domains, paying special attention to the assumptions and goals of different classes of real-time systems.
- We also survey the existing correctness criteria and concurrency control algorithms for real-time systems, and classify them according to their characteristics and properties.
- We identify the main challenges and open issues in this area, and suggest some directions for future research.