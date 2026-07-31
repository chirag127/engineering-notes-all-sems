### Soft Real Time Systems

- A soft real-time system is a system that can tolerate some degree of deadline misses or timing jitter without causing critical failures or unacceptable degradation of performance  .
- A soft real-time system can run on multiple cores and impose fewer restrictions on applications than a hard real-time system .
- A soft real-time system is typically used to solve issues of concurrent access and the need to keep a number of connected systems up-to-date through changing situations.
- Some examples of soft real-time systems are:
  - Software that maintains and updates the flight plans for commercial airliners.
  - Streaming audio-video applications that can tolerate some packet loss or delay .
  - Online gaming platforms that can adjust the level of graphics quality or network latency according to the available resources.
- Some characteristics of soft real-time systems are:
  - They have flexible deadlines that can be missed occasionally with low probability .
  - They have variable response times that depend on the system load and the priority of the tasks.
  - They have graceful degradation of quality or performance when the system is overloaded or the resources are insufficient .
  - They have high throughput and high availability requirements .