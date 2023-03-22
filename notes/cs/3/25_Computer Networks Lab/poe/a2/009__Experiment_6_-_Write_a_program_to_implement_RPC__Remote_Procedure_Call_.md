 Here is the content in markdown format without any emojis or external links:

## Experiment 6 - Write a program to implement RPC (Remote Procedure Call)

1. RPC is a client-server communication model where a program on a client machine sends a message to a server to initiate a procedure call and wait for a response.
2. The client's stub procedure marshals the procedure call, sends it to the server, and waits for the reply.
3. The server's stub procedure unmarshals the parameters and calls the actual server procedure with the parameters. After execution, it returns the result to the client.
4. The client's stub receives the reply and returns the result to the caller.
5. This makes it appear as if a procedure is executed locally, whereas it is actually executed on the server.
6. Steps to implement RPC:

- Define the interface (specification) of procedures to be called.
- Implement client and server stubs.
- Implement server procedure(s).
- Compile stubs and procedures into client and server applications.
- Run the server process.
- Run the client process and invoke RPC.

The key advantages of RPC are:

- Location transparency - Client is unaware of where the procedure is executed.
- Portability - Can be used across networks and heterogeneous systems.
- Efficiency - Lightweight and efficient client-server communication.

The main disadvantages are:

- Tight coupling - Client and server are tightly coupled.
- Security - Vulnerable to various threats and attacks.
- Version management - Difficult to manage interface changes and version compatibility.