### Timing Constraints for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- Timing constraints are a vital attribute in real-time systems. They decide the total correctness of the result in real-time systems.
- The correctness of results in real-time systems does not depend only on logical correctness but also the result should be obtained within the time constraint.
- For a real-time system to be capable of real-time computing, it must satisfy two requirements:
  - Timeliness: The ability to produce the expected result by a specific deadline.
  - Time synchronization: The capability of agents to coordinate independent clocks and operate together in unison.
- Timing constraints associated with the real-time system are classified to identify the different types of timing constraints in a real-time system. Timing constraints are broadly classified into two categories:
  - Performance Constraints: The constraints enforced on the response of the system are known as Performance Constraints. They are further divided into three types:
    - Delay Constraint: A delay constraint describes the minimum time interval between the occurrence of two consecutive events. For example, the minimum time interval between a sensor detecting an obstacle and a robot stopping its motion.
    - Deadline Constraint: A deadline constraint describes the maximum time interval between the occurrence of two consecutive events. For example, the maximum time interval between a user pressing a button and a screen displaying the result.
    - Duration Constraint: A duration constraint describes the maximum time interval for which an event can last. For example, the maximum time interval for which a camera can capture an image.
  - Reliability Constraints: The constraints enforced on the probability of failure of the system are known as Reliability Constraints. They are also divided into three types:
    - Failure Rate Constraint: A failure rate constraint describes the maximum acceptable frequency of failure of the system. For example, the maximum acceptable frequency of a network dropping packets.
    - Failure Duration Constraint: A failure duration constraint describes the maximum acceptable time interval for which the system can remain in a failed state. For example, the maximum acceptable time interval for which a power supply can be down.
    - Recovery Time Constraint: A recovery time constraint describes the maximum acceptable time interval for which the system can recover from a failed state. For example, the maximum acceptable time interval for which a backup system can take over from a failed system.
- Types of real-time systems based on timing constraints:
  - Hard real-time system: This type of system can never miss its deadline. Missing the deadline may have disastrous consequences. For example, a nuclear reactor control system, a pacemaker, an air traffic control system, etc.
  - Soft real-time system: This type of system can miss its deadline occasionally with some acceptably low probability. Missing the deadline may degrade the performance or quality of service of the system. For example, a video streaming system, a voice recognition system, a web server, etc.

Mnemonics are memory tricks that can help you remember new information by connecting it to something you already know. There are different types of mnemonics, such as rhymes, acronyms, diagrams, or key words. For example, you can use the acronym HOMES to remember the names of the Great Lakes: Huron, Ontario, Michigan, Erie, and Superior. Or you can use the rhyme "Thirty days hath September, April, June, and November" to remember how many days are in each month.

Some mnemonics are easy to remember, but others may be more difficult. It depends on your personal preference and learning style. The best way to find out which mnemonics work for you is to try them out and practice them. You can also create your own mnemonics based on what makes sense to you. The more meaningful and memorable the mnemonic is, the better it will help you recall the information.