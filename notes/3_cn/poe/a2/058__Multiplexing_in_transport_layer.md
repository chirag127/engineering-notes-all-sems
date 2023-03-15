 Here is the formal content on Multiplexing in transport layer in markdown format with points:

### Multiplexing in transport layer

1. Multiplexing is the process of combining multiple data streams over a single transmission medium. In the transport layer, multiplexing is used to combine multiple application layer data streams over a single port number. This allows multiple applications to share a single port, conserving system resources.
2. Two types of multiplexing used in the transport layer are:
 - Port number multiplexing: Each application is assigned a port number, allowing the transport layer to direct incoming data to the correct application.
 - Session multiplexing: A session ID is used to associate segments of data with a particular application.
3. Multiplexing is handled differently in TCP and UDP:
 - In TCP, port numbers are used to multiplex. Each application must have its own port.
 - In UDP, port numbers are also used but optional. Multiple applications can reuse the same port number if their data can be uniquely identified another way.
4. The benefits of multiplexing include:
 - Efficient use of system resources like port numbers and network bandwidth.
 - Allowing multiple applications to run concurrently and share transport layer services.
 - Simplified network architecture. Without multiplexing, each application would require its own transport mechanism.

Does this sound okay? Let me know if you would like me to modify or expand the content in any way.