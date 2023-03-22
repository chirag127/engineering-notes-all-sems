 Here is the content in Markdown format without any emojis or external links, in a formal tone with points:

### Offline Versus Online Scheduling

#### Offline Scheduling
- The schedule is computed before runtime.
- All tasks and their characteristics like period, deadline, execution time are known beforehand.
- The schedule is computed at design time.
- It is suitable for systems with static task set.
- Allows optimal resource utilization.
- Not suitable for dynamic real-time systems where tasks may get created and deleted at runtime.

#### Online Scheduling
- The schedule is computed at runtime based on the tasks that are present.
- Task characteristics may not be known beforehand. They may get changed at runtime.
- It is suitable for dynamic real-time systems where tasks and their characteristics may change at runtime.
- Does not always guarantee optimal resource utilization.
- Incurs runtime overhead for schedule computation.

The choice between offline and online scheduling depends on whether the task set is static or dynamic. Both approaches are used in practice for real-time systems depending on the system requirements.