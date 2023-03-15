### Time Services

- Time services are the mechanisms that provide the notion of time and timing in real-time systems .
- Time services are essential for ensuring the timeliness and synchronization of real-time tasks and events .
- Time services can be classified into two categories: clock services and timer services.

#### Clock Services

- Clock services are the functions that provide the current time value and the resolution of the time unit.
- Clock services can be implemented by using hardware clocks or software clocks.
- Hardware clocks are physical devices that generate periodic signals based on a quartz crystal oscillator or an atomic clock.
- Software clocks are logical entities that maintain a time value based on the hardware clock signals or other external sources.
- Clock services can support different time domains, such as absolute time, relative time, or logical time.
- Absolute time is the time measured from a fixed reference point, such as the Unix epoch or the GPS time.
- Relative time is the time measured from a variable reference point, such as the system start or the task activation.
- Logical time is the time based on the order of events or messages in a distributed system, such as Lamport's timestamps or vector clocks.

#### Timer Services

- Timer services are the functions that provide the ability to schedule actions or events based on time values.
- Timer services can be implemented by using hardware timers or software timers.
- Hardware timers are physical devices that generate interrupts or signals when a predefined time value is reached.
- Software timers are logical entities that use the clock services or the hardware timers to trigger actions or events.
- Timer services can support different types of timers, such as one-shot timers, periodic timers, or deadline timers.
- One-shot timers are timers that expire only once after a specified time interval.
- Periodic timers are timers that expire repeatedly at regular time intervals.
- Deadline timers are timers that expire at a specific absolute time value.