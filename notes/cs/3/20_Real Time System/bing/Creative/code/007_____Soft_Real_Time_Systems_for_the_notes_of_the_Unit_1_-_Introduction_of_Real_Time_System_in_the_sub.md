### Soft Real Time Systems

- A soft real-time system is a system that can tolerate some degree of deadline misses or timing jitter without causing critical failures or unacceptable degradation of performance   .
- A soft real-time system is typically used to handle concurrent access and update of multiple connected systems in changing situations, where the quality of service may vary depending on the timeliness of the response.
- Some examples of soft real-time systems are:
  - Software that maintains and updates the flight plans for commercial airliners.
  - Streaming audio and video applications that can tolerate some glitches or delays in the playback.
  - Online gaming platforms that can adjust the level of detail and resolution based on the network latency.
- Some characteristics of soft real-time systems are:
  - They can run on multiple cores and impose fewer restrictions on applications than hard real-time systems.
  - They can use dynamic memory allocation and garbage collection techniques that may introduce unpredictable delays in the execution.
  - They can employ adaptive algorithms and feedback mechanisms that can adjust the system parameters and behavior based on the observed performance.
  - They can use probabilistic analysis and statistical methods to estimate the worst-case execution time and the deadline miss ratio.