 Here is the content in markdown format without any emojis or external links and in a formal tone:

## Unit 2 - Real Time Scheduling

1. Real-time systems - Systems where correct performance depends not only on logical correctness of computations but also on timeliness of results. Missing a deadline can have catastrophic consequences.
2. Hard real-time systems - Missing a deadline is unacceptable. Examples - Emergency shutdown systems in nuclear plants, Flight control systems, etc.
3. Soft real-time systems - Missing a deadline occasionally is acceptable, but lateness must be bounded. Examples - Multimedia systems where some frames can be skipped occasionally as long as the video/audio quality is acceptable.
4. Real-time task - A piece of functionality that must be executed within a given deadline. Can be characterized by:
 - worst-case execution time (wcet) - upper bound on execution time.
 - deadline - latest time by which task must complete.
 - period - minimum inter-arrival time between task invocations. Aperiodic tasks have no period.
5. Real-time scheduling - The problem of assigning priorities/resources to real-time tasks such that all deadlines are met. Criteria for evaluation -
 - Meeting all deadlines (hard guarantee)
 - Maximizing number of deadlines met (soft guarantee)
 - Maximizing throughput/resource utilization

Does this sound okay? Let me know if you would like me to modify or expand the content in any way.