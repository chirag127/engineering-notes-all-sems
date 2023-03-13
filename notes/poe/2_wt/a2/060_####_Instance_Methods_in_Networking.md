 Here is the content in markdown format for Instance Methods in Networking:

#### Instance Methods in Networking

- **.gethostname()**: Returns the hostname of the machine. Mnemonic: Get the Host Name.
- **.gethostbyname(hostname)**: Translates a hostname to IPv4 address. Mnemonic: Get IP by Host Name.
- **.gethostbyname_ex(hostname)**: Translates a hostname to a tuple containing (hostname, aliaslist, IP address list). Provides more details than gethostbyname().
- **.gethostbyaddr(ip_address)**: Translates an IPv4 address to a hostname. Reverse of gethostbyname().
- **.getservbyname(servicename, protocolname)**: Returns a port number for a given service and protocol. Mnemonic: Get port by Service Name.
- **.getprotobyname(protocolname)**: Returns a protocol number for the given protocol name.

Advantages: Provide mapping between hostnames, IP addresses and port numbers which are required for networking and connecting to remote hosts.
Disadvantages: May return outdated information or fail to resolve in case the DNS is not updated.
Examples:
```
import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print(ip)
```

Applications: Used to get host information, verify DNS records, used in client-server programming to get port numbers, etc.

The above content summarizes some key Instance Methods in the socket module of Python related to networking and provides some Mnemonics to remember them easily along with advantages, disadvantages and examples. The points are written in a formal way with headings for a study material. Please let me know if you would like me to elaborate on any part or add more details.