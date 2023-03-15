### Experiment 8.3 - File Transfer

- File transfer is the process of copying or moving a file from one computer to another over a network or the Internet.
- File transfer can be done using different protocols, such as FTP, HTTP, SCP, SFTP, etc.
- File transfer can be done in different modes, such as binary, ASCII, or auto.
- File transfer can be done using different tools, such as command-line utilities, graphical user interfaces, or web browsers.
- File transfer can be done for different purposes, such as backup, synchronization, sharing, or distribution.

#### Objectives

- To learn how to use FTP to transfer files between two computers.
- To learn how to use SCP and SFTP to securely transfer files between two computers.
- To learn how to use HTTP to transfer files using a web browser.

#### Requirements

- Two computers connected to the same network or the Internet.
- FTP server and client software installed on both computers.
- SSH server and client software installed on both computers.
- Web server and browser software installed on both computers.
- A text editor and a binary file (such as an image or a video) to transfer.

#### Procedure

- FTP
  - On the computer that will act as the FTP server, create a folder named ftp and copy the text and binary files into it.
  - On the same computer, start the FTP server software and configure it to allow anonymous access to the ftp folder.
  - On the computer that will act as the FTP client, start the FTP client software and connect to the FTP server using the IP address and the anonymous username and password.
  - On the FTP client, use the ls or dir command to list the files in the ftp folder on the FTP server.
  - On the FTP client, use the get or mget command to download the text and binary files from the FTP server to the local folder.
  - On the FTP client, use the put or mput command to upload the text and binary files from the local folder to the FTP server.
  - On the FTP client, use the quit or bye command to disconnect from the FTP server.
  - On the FTP server, verify that the files have been transferred correctly by comparing the file sizes and contents.
- SCP and SFTP
  - On the computer that will act as the SSH server, create a folder named ssh and copy the text and binary files into it.
  - On the same computer, start the SSH server software and configure it to allow password authentication and public key authentication.
  - On the computer that will act as the SSH client, start the SSH client software and generate a public and private key pair using the ssh-keygen command.
  - On the SSH client, use the ssh-copy-id command to copy the public key to the SSH server.
  - On the SSH client, use the scp command to securely copy the text and binary files from the SSH server to the local folder using the IP address and the username and password or the public key.
  - On the SSH client, use the scp command to securely copy the text and binary files from the local folder to the SSH server using the IP address and the username and password or the public key.
  - On the SSH client, use the sftp command to securely connect to the SSH server using the IP address and the username and password or the public key.
  - On the SFTP client, use the ls or dir command to list the files in the ssh folder on the SSH server.
  - On the SFTP client, use the get or mget command to download the text and binary files from the SSH server to the local folder.
  - On the SFTP client, use the put or mput command to upload the text and binary files from the local folder to the SSH server.
  - On the SFTP client, use the quit or bye command to disconnect from the SSH server.
  - On the SSH server, verify that the files have been transferred correctly by comparing the file sizes and contents.
- HTTP
  - On the computer that will act as the web server, create a folder named www and copy the text and binary files into it.
  - On the same computer, start the web server software and configure it to allow access to the www folder.
  - On the computer that will act as the web client, start the web browser software and enter the URL of the web server using the IP address and the www folder name.
  - On the web browser, view the text and binary files by clicking on the links or the icons.
  - On the web browser, download the text and binary files by right-clicking on the links or the icons and choosing the save option.
  - On the web browser, upload the text and binary