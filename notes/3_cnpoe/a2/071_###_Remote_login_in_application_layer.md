 Here is the content in markdown format for the topic ### Remote login in application layer:

### Remote login in application layer

The application layer protocol used for remote login is typically SSH (Secure Shell). SSH provides encrypted communication between two hosts over an insecure network, allowing a user to login to a remote machine and execute commands.

Some key points about SSH remote login:

- SSH uses port 22 by default to establish a secure connection between the client and server.
- SSH uses public-key cryptography to authenticate the server and establish a shared secret key for symmetric encryption of the data stream.
- SSH provides terminal-based access as well as file transfer capabilities (through SFTP/SCP protocols).
- SSH connections can be tunneled within other network protocols to provide additional encryption/security for those protocols.
- SSH requires the SSH server software to be installed and configured on the remote machine and SSH client software on the local machine. OpenSSH is a common open-source implementation.
- When logging in with SSH, the user typically enters their username and password/passphrase to authenticate to the remote server. However, public key authentication is more secure and convenient if set up.
- Remembering passwords for multiple remote logins can be difficult, so alternatives like SSH keys or password managers help. Mnemonics/tricks are not very applicable here due to sensitive security requirements.

Advantages of SSH include strong encryption, widespread support, and flexibility. Disadvantages include some complexity to set up and the potential for man-in-the-middle attacks if server authentication is not verified.

SSH is commonly used to administer Unix/Linux servers, access cloud resources, and tunnel insecure protocols. It serves as a key building block of secure remote access in the Internet.

[Detailed diagrams and examples could be added here if helpful for learning.]