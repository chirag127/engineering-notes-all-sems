# Remote Login

- Remote login is a process in which a user can log on to a remote computer and use the services and applications that are available on that computer.
- Remote login is an example of an application layer function in the OSI model, which is the highest layer that interacts with the user and the presentation layer, which is responsible for data formatting and encryption.
- Remote login requires a protocol that can establish a connection between the local and remote computers, authenticate the user, and transmit the user's keystrokes and the remote computer's output.
- One of the most common protocols for remote login is Telnet, which stands for Terminal Network. Telnet is a client-server protocol that uses TCP as the transport layer protocol and port number 23 as the well-known port.
- The steps involved in a remote login using Telnet are:

  - The user sends the keystrokes to the terminal driver, which converts them into ASCII codes and sends them to the Telnet client.
  - The Telnet client encapsulates the ASCII codes into TCP segments and sends them to the Telnet server on the remote computer using port 23.
  - The Telnet server receives the TCP segments and extracts the ASCII codes, which are then sent to the terminal driver on the remote computer.
  - The terminal driver converts the ASCII codes into keystrokes and passes them to the application program on the remote computer.
  - The application program processes the keystrokes and sends the output to the terminal driver, which converts it into ASCII codes and sends it to the Telnet server.
  - The Telnet server encapsulates the ASCII codes into TCP segments and sends them back to the Telnet client on the local computer using port 23.
  - The Telnet client receives the TCP segments and extracts the ASCII codes, which are then sent to the terminal driver on the local computer.
  - The terminal driver converts the ASCII codes into characters and displays them on the user's screen.

- The advantages of remote login are:

  - It allows the user to access and use the resources and applications on a remote computer without physically being there.
  - It reduces the network traffic and processing load on the local computer, as the data is transferred only between the Telnet client and server, and the processing is done on the remote computer.
  - It provides a uniform interface for the user, as the user can use the same terminal and commands regardless of the operating system or hardware of the remote computer.

- The disadvantages of remote login are:

  - It requires a reliable and secure network connection, as any interruption or tampering can affect the communication and the user's session.
  - It exposes the user's credentials and data to potential eavesdropping and hacking, as the data is transmitted in plain text and the authentication is based on a simple username and password.
  - It has limited functionality and interactivity, as the user can only use the text-based applications and commands that are supported by the remote computer.