### Domain Name System

The Domain Name System (DNS) is a hierarchical and decentralized naming system for computers, services, or other resources connected to the Internet or a private network. It associates various information with domain names assigned to each of the participating entities. Most prominently, it translates more readily memorized domain names to the numerical IP addresses needed for locating and identifying computer services and devices with the underlying network protocols. By providing a worldwide, distributed directory service, the Domain Name System is an essential component of the functionality of the Internet.

Here is an example of a simple DNS resolution in Python:

```python
import socket
addr1 = socket.gethostbyname('google.com')
addr2 = socket.gethostbyname('microsoft.com')
print(addr1)
print(addr2)
```
