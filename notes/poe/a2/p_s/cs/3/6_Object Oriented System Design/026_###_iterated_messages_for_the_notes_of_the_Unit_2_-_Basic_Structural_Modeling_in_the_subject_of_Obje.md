 Here is the content in markdown format for the topic ### iterated messages for the notes of the Unit 2 - Basic Structural Modeling in the subject of Object Oriented System Design:

### Iterated Messages

- Iterated messages refer to messages that are sent repeatedly over a period of time or continuously.
- These messages are sent in a loop until a certain condition is met or to keep performing an action continuously.
- For example, a timer sending ticks at regular intervals, a server sending heartbeat messages periodically to check if a client is alive, etc.
- The sender and receiver objects need to be designed to handle such iterated messages efficiently without any performance issues.
- Some key points to keep in mind for iterated messages are:

1. Do not put the message sending logic directly in the loop. Instead, create a separate thread or use timer based scheduling to send the messages. This avoids blocking the main flow of execution.
2. The receiver should be ready to receive and process multiple such messages and not just one. Proper queuing and dequeueing mechanisms may be required based on the use case.
3. Proper validations and exits from the loop should be present to not continue sending messages endlessly in unwanted scenarios.
4. The rate at which messages are sent and processed should be optimized based on the application requirements and hardware capabilities. Too fast rates may lead to congestion while too slow rates may not serve the actual purpose.

- Iterated messages are commonly used in event-driven systems and streaming data applications.
- Examples include stock price ticks, GPS location updates, server monitoring heartbeats, etc.