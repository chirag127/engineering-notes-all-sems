### File Transfer Protocol in application layer

File Transfer Protocol (FTP) is a standard network protocol used to transfer files from one host to another over a TCP-based network, such as the Internet. FTP is built on a client-server architecture and uses separate control and data connections between the client and the server. Here is an example of how FTP can be implemented in Python:

```python
from ftplib import FTP

ftp = FTP('ftp.example.com')
ftp.login(user='username', passwd='password')
ftp.cwd('/path/to/directory')

filename = 'example.txt'
with open(filename, 'rb') as file:
    ftp.storbinary(f'STOR {filename}', file)

ftp.quit()
```
