 Here is the content in markdown format for the topic ### File Transfer Protocol in application layer:

File Transfer Protocol (FTP) is an application layer protocol used for transferring files between two systems over a network. It works on the client-server model.

Some key points about FTP:

- FTP establishes two connections between the client and server:
  - Control connection: Used to transfer control and command messages.
  - Data connection: Used to transfer actual data i.e. files.
- FTP has two modes of data transfer:
  - ASCII mode: Used for text files. Data is converted into ASCII characters.
  - Binary mode: Used for binary files like images, videos, etc. No conversion is done. Binary data is transferred as is.
- FTP commands:
  - USER: Used to specify the username.
  - PASS: Used for providing the password.
  - LIST: Used to list the files and directories on the server.
  - CWD: Used to change the current working directory on the server.
  - CDUP: Used to move to the parent directory.
  - RETR: Used to retrieve a file from the server to the local system.
  - STOR: Used to store a file from the local system to the server.
  - QUIT: Used to terminate the FTP session.
- Advantages:
  - Simple and easy to use.
  - Supports additional features like directory listing, renaming, etc.
- Disadvantages:
  - insecure as it transmits passwords and data in clear text which can be sniffed.
  - Does not provide strong authentication and encryption mechanisms.

[Include diagrams and examples if required.]

Applications: FTP is commonly used to:
- Transfer web pages and update website content.
- Share and distribute large software or multimedia files.
- Enable users to access and share files remotely.