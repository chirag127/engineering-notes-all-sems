### Dynamic Versus Static Systems

- A **static system** is one where the tasks and their attributes (such as arrival time, execution time, deadline, priority, etc.) are known in advance and do not change during the system execution. A static system can be scheduled offline using a **static scheduling algorithm** that assigns a fixed priority or a fixed order to each task. Static scheduling algorithms are usually simpler and faster than dynamic ones, and can guarantee the feasibility of the schedule if the system is schedulable. Static scheduling algorithms are suitable for **hard real-time systems** where the tasks have strict deadlines and deterministic behavior. Static scheduling algorithms can also be used to validate the system performance and detect any potential deadline violations. Examples of static scheduling algorithms are **rate-monotonic scheduling (RMS)** and **earliest deadline first (EDF)** with fixed task parameters .

- A **dynamic system** is one where the tasks and their attributes can change during the system execution due to unpredictable events or workload variations. A dynamic system requires a **dynamic scheduling algorithm** that assigns a variable priority or a variable order to each task based on the current system state. Dynamic scheduling algorithms are usually more complex and slower than static ones, but can adapt to the changing system conditions and optimize the system performance. Dynamic scheduling algorithms are suitable for **soft real-time systems** where the tasks have flexible deadlines and stochastic behavior. Dynamic scheduling algorithms can also handle sporadic or aperiodic tasks that arrive at random times. Examples of dynamic scheduling algorithms are **least laxity first (LLF)** and **earliest deadline first (EDF)** with variable task parameters .

- The main advantages and disadvantages of static and dynamic systems are summarized below   :

| Static System | Dynamic System |
|---------------|----------------|
| + Simpler and faster scheduling algorithm | - More complex and slower scheduling algorithm |
| + Guaranteed feasibility of the schedule if the system is schedulable | - No guarantee of feasibility of the schedule |
| + Possible to validate the system performance offline | - Not possible to validate the system performance offline |
| + Suitable for hard real-time systems with strict deadlines and deterministic behavior | + Suitable for soft real-time systems with flexible deadlines and stochastic behavior |
| - Poor performance in terms of overall response time of tasks | + Better performance in terms of overall response time of tasks |
| - Cannot handle sporadic or aperiodic tasks | + Can handle sporadic or aperiodic tasks |
| - Cannot adapt to changing system conditions | + Can adapt to changing system conditions |