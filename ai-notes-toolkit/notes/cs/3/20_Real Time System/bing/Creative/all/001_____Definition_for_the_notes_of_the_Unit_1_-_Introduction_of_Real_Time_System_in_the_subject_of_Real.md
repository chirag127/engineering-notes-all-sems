# Definition for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A real time system is a system that must respond to events or inputs within a specified time interval, called a deadline.
- A real time system can be classified into two types: hard real time system and soft real time system.
- A hard real time system is a system that must meet all its deadlines, otherwise it may cause catastrophic consequences or failure. For example, a nuclear reactor control system, a flight control system, or a pacemaker.
- A soft real time system is a system that can tolerate some missed deadlines, but the quality of service or performance may degrade. For example, a video streaming system, a voice recognition system, or a web server.
- A real time system can also be classified into two types based on the predictability of the events or inputs: periodic and aperiodic.
- A periodic system is a system that has events or inputs that occur at regular intervals, such as a sensor reading, a clock tick, or a task execution. The interval between two consecutive occurrences of the same event or input is called the period.
- An aperiodic system is a system that has events or inputs that occur at irregular or unpredictable intervals, such as a user request, a network packet, or a fault. The interval between two consecutive occurrences of the same event or input is called the interarrival time.
- A real time system can also be classified into two types based on the number of processors or cores: uniprocessor and multiprocessor.
- A uniprocessor system is a system that has only one processor or core that executes all the tasks or processes of the system. The processor or core may switch between different tasks or processes using a scheduling algorithm.
- A multiprocessor system is a system that has more than one processor or core that can execute tasks or processes of the system concurrently or in parallel. The processors or cores may communicate with each other using shared memory or message passing.