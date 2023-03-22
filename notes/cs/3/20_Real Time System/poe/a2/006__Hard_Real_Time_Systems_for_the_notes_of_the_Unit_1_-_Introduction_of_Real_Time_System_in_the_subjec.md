 Here is the content in Markdown format without any emojis or external links and in a formal tone:

### Hard Real Time Systems

- Hard real-time systems are systems where missing a deadline is absolutely unacceptable. Even missing a deadline by a small amount can be disastrous.
- Examples include systems controlling aircraft flight control, nuclear plant monitoring, industrial robot control, etc. Where even a small delay can lead to loss of life or serious damage.
- These systems need guarantees of timing behaviour and this requires:
    - Known/deterministic worst-case execution times for tasks.
    - Fixed and known task execution sequences.
    - Limited concurrency.
    - Limited preemption.
- Techniques like rate monotonic scheduling are used to provide timing guarantees. The system is carefully designed to ensure all deadlines will always be met, even in worst-case conditions.
- The hardware platforms used need to be very reliable and deterministic in behaviour. General purpose operating systems are not suitable and hard real-time systems often use special real-time operating systems or run directly on the hardware.

The content summarizes key points about hard real-time systems in a formal tone with bullet points and no external links or emojis as instructed. Please let me know if you would like me to modify or expand the content in any way.