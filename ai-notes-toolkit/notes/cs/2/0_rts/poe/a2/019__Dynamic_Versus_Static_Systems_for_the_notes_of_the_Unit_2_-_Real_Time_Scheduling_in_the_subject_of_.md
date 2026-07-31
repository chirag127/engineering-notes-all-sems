 Here are the notes on the topic "Dynamic Versus Static Systems" for Unit 2 - Real Time Scheduling:

### Dynamic Versus Static Systems

- In static systems, all tasks are known a priori, i.e. before runtime. The schedule can be computed offline. In dynamic systems, new tasks arrive during runtime and the schedule must be recomputed to accommodate them.
- Static systems have the advantage of predictable and analyzable worst-case performance. However, they cannot handle unexpected tasks or events. Dynamic systems can accommodate unforeseen tasks but may suffer from unpredictability and unanalyzability.
- Hybrid systems use static scheduling for predictable tasks and dynamic scheduling for unexpected tasks. This combines the advantages of both pure approaches.
- Whether a system should be static or dynamic depends on the application and its requirements. Systems with primarily periodic and predictable tasks are good candidates for static scheduling. Systems with aperiodic or sporadic tasks benefit from dynamic scheduling.

- The key points to note are:
-- Static systems have tasks known before runtime while dynamic systems have tasks arriving during runtime.
-- Static systems enable analysis of worst-case performance while dynamic systems handle unforeseen tasks.
-- Hybrid systems use both static and dynamic scheduling to combine advantages.
-- The choice of static vs dynamic depends on application requirements like predictability of tasks.

Does this summary look okay? Let me know if you would like me to modify or expand the notes in any way.