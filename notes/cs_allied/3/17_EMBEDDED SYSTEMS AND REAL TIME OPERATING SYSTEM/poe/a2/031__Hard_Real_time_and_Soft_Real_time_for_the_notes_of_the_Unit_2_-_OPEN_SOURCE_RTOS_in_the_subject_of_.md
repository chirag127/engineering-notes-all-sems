 Here is the content in Markdown format without any emojis or external links and in formal tone:

### Hard Real time and Soft Real-time

- Hard Real-time system: In hard real-time systems, meeting the deadline is absolutely critical, even if it requires dropping or skipping some tasks. Missing a deadline will result in system failure. Example: Flight control system, industrial robot controllers.
- Soft Real-time system: In soft real-time systems, most deadlines need to be met, but occasional missed deadlines are tolerable. The usefulness of the results degrades after deadline, but system failure does not occur. Example: Video conferencing, voice recognition systems.
- RTOS (Real Time Operating System) is an OS designed to serve real-time applications that must process data reliably within strict time constraints. It reduces latency and increases predictability. It provides capabilities such as priority scheduling, interrupt management, and semaphores.
- Differences between general-purpose OS and RTOS:
-- RTOS provides more predictability and deterministic behavior. It has fast and prioritized responses to events.
-- RTOS has a smaller footprint and faster response times. It has fewer abstractions and overlays.
-- RTOS does not have a general interface for a range of devices. It interfaces directly with the hardware.

The notes cover the key differences between hard real-time and soft real-time systems along with the characteristics of a Real-Time Operating System which is essential for real-time applications. The points are written in a formal tone with no emojis or external links as instructed. Please let me know if you would like me to modify or expand the notes.