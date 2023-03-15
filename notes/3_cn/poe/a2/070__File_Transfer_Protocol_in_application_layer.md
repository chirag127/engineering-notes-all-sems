 Here is the content in markdown format with formal tone and without external links or emojis:

### File Transfer Protocol in application layer

1. FTP or File Transfer Protocol is a standard network protocol used to transfer computer files between a client and server on a computer network.
2. FTP is built on a client-server model architecture and uses separate control and data connections between the client and the server.
3. The FTP client initiates both the control and data connections. The control commands are sent over the control connection, and the data is transferred over the data connection.
4. FTP provides authentication, uses TCP for its transport layer, and allows data to be transferred in two modes:
- ASCII mode: Used for text files. Converts the end-of-line characters as needed for the receiving system.
- Binary mode: Used for image, audio, and video files etc. Preserves the exact bit-sequence of transmitted data and avoids conversion of newlines.
5. FTP servers often provide an anonymous login mechanism, allowing users to access files without providing authentication. Some FTP servers let the administrator limit anonymous users to certain directories.
6. FTP has been largely replaced by more secure, firewall-friendly file transfer alternatives such as Secure File Transfer Protocol (SFTP) and SSH File Transfer Protocol (SFTP). However, FTP is still commonly used to transfer large media files given its simplicity and low overhead.