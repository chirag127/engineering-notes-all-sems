### Experiment 8.3 - File Transfer

In this experiment, we will learn about file transfer between two computers using the Python programming language. The file transfer will be done over a network connection using the socket programming library in Python.

#### Requirements
- Two computers connected to the same network
- Python programming language installed on both computers
- Basic knowledge of socket programming in Python

#### Steps
1. Open two command prompt windows on both computers and navigate to a common directory where the files to be transferred are located.
2. In one command prompt window, run the server program using the following command:
```python server.py```
3. In the other command prompt window, run the client program using the following command:
```python client.py```
4. The client program will prompt for the IP address of the server computer. Enter the IP address of the server computer and press enter.
5. The client program will prompt for the name of the file to be transferred. Enter the name of the file and press enter.
6. The file transfer will start and the progress will be displayed on both the client and server command prompt windows.
7. Once the transfer is complete, the client and server command prompt windows will display a message indicating the success of the transfer.

#### Advantages
- Can be used to transfer files between two computers over a network connection.
- Can be automated using scripts for regular file transfers.

#### Disadvantages
- Requires knowledge of socket programming in Python.
- Can be slow for large files or slow network connections.

#### Example
An example of transferring a file named "example.txt" between two computers with IP addresses 192.168.1.100 (server) and 192.168.1.101 (client) using the above steps.

#### Applications
- Used in backup and synchronization of files between computers.
- Used in transferring files between servers in a network.