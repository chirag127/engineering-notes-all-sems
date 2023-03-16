### Soft Real Time Systems

- A soft real-time system is a system that can tolerate some degree of latency or jitter in the execution of its tasks, without causing catastrophic failure or unacceptable degradation of performance  .
- A soft real-time system has a deadline for each task, but missing the deadline occasionally does not have disastrous consequences. The usefulness of the results produced by a soft real-time system decreases gradually with an increase in tardiness.
- Examples of soft real-time systems include:
  - Software that maintains and updates the flight plans for commercial airliners. The flight plans must be kept reasonably current, but they can operate with the latency of a few seconds.
  - Live audio-video systems, such as video conferencing, streaming, or gaming. These systems require low latency and high quality, but can tolerate some occasional glitches or delays .
  - Telephone switches, which handle the routing and switching of voice calls. These systems must provide fast and reliable service, but can cope with some dropped or delayed calls.
- Characteristics of soft real-time systems include:
  - They can run on multiple cores and impose fewer restrictions on applications than hard real-time systems.
  - They can use dynamic memory allocation, virtual memory, and preemptive scheduling, which are not feasible for hard real-time systems .
  - They can handle non-deterministic events and inputs, such as user interactions, network traffic, or sensor data .
  - They can trade off between timeliness and quality of service, depending on the system requirements and the available resources .