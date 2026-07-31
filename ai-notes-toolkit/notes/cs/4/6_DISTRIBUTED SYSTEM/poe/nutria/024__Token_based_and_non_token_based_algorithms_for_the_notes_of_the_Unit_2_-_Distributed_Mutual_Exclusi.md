
### Token-Based Algorithms

- Token-based algorithms are used to ensure that only one process at a time can access a critical section. 
- Token-based algorithms use a token, or a special message, to indicate which process is allowed to enter the critical section.
- The token is passed from process to process in a distributed system and is only held by one process at a time. 
- A process must acquire the token before it can enter the critical section.
- The token is released by the process when it exits the critical section, allowing the next process in line to acquire the token and enter the critical section.

### Non-Token-Based Algorithms

- Non-token-based algorithms are used to ensure that only one process at a time can access a critical section. 
- Non-token-based algorithms use a request and reply mechanism to control access to the critical section. 
- A process must request access to the critical section and wait for a reply before it can enter the critical section. 
- The reply is sent by the process that currently holds the critical section and is only sent when the process exits the critical section. 
- This allows the next process in line to enter the critical section.