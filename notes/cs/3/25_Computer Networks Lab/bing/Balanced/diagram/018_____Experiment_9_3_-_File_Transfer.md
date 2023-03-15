### Experiment 9.3 - File Transfer

- File transfer is the process of copying or moving a file from one computer to another over a network or the Internet.
- File transfer can be done using different protocols, such as FTP, HTTP, SCP, SFTP, etc.
- File transfer can be done for different purposes, such as backup, synchronization, sharing, distribution, etc.
- File transfer can be done in different modes, such as binary, ASCII, or auto.
- File transfer can be done using different tools, such as command-line utilities, graphical user interfaces, web browsers, etc.

#### Objectives

- To learn how to use FTP and SCP commands to transfer files between computers.
- To compare the advantages and disadvantages of FTP and SCP protocols.
- To understand the difference between binary and ASCII modes of file transfer.
- To learn how to use SFTP and a graphical user interface to transfer files securely and conveniently.

#### Procedure

1. Connect to a remote computer using SSH or Telnet.
2. Use the FTP command to start an FTP session with another remote computer.
3. Use the `help` command to see the list of available FTP commands.
4. Use the `ls` command to list the files and directories on the remote computer.
5. Use the `cd` command to change the current directory on the remote computer.
6. Use the `lcd` command to change the current directory on the local computer.
7. Use the `get` command to download a file from the remote computer to the local computer.
8. Use the `put` command to upload a file from the local computer to the remote computer.
9. Use the `mget` and `mput` commands to download and upload multiple files at once.
10. Use the `type` command to change the mode of file transfer between binary and ASCII.
11. Use the `quit` command to end the FTP session.
12. Use the SCP command to copy a file from the local computer to the remote computer using SSH.
13. Use the SCP command to copy a file from the remote computer to the local computer using SSH.
14. Use the `-r` option to copy a directory and its contents recursively using SCP.
15. Use the `-p` option to preserve the file attributes such as permissions, timestamps, etc. using SCP.
16. Use the SFTP command to start an SFTP session with another remote computer using SSH.
17. Use the same commands as FTP to list, change, and transfer files and directories using SFTP.
18. Use the `quit` command to end the SFTP session.
19. Use a graphical user interface such as FileZilla or WinSCP to connect to a remote computer using FTP or SFTP.
20. Use the drag-and-drop feature to transfer files and directories between the local and remote computers using the graphical user interface.

#### Observations

- FTP is a simple and widely used protocol for file transfer, but it is not secure as it sends the data and credentials in plain text over the network.
- SCP is a secure protocol for file transfer, as it encrypts the data and credentials using SSH, but it is not as flexible as FTP as it does not support interactive commands or multiple file transfers.
- SFTP is a secure and flexible protocol for file transfer, as it combines the features of FTP and SCP using SSH, but it may not be supported by all servers or clients.
- Binary mode is used to transfer files that are not text-based, such as images, audio, video, etc. ASCII mode is used to transfer files that are text-based, such as documents, scripts, etc. Auto mode is used to detect the file type and choose the appropriate mode automatically.
- Graphical user interfaces are user-friendly and convenient tools for file transfer, but they may not be as fast or reliable as command-line utilities.