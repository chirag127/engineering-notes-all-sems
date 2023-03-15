#### DHCP
Dynamic Host Configuration Protocol (DHCP) is a network management protocol used to dynamically assign an Internet Protocol (IP) address to any device, or node, on a network so they can communicate using IP. Here is an example of a simple DHCP server written in Python:

```python
import socket
from struct import pack

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 67))

while True:
    message, address = server_socket.recvfrom(1024)
    transaction_id = message[4:8]
    client_mac = message[28:34]
    offer_ip = socket.inet_aton('192.168.1.100')
    server_ip = socket.inet_aton('192.168.1.1')
    subnet_mask = socket.inet_aton('255.255.255.0')
    router = socket.inet_aton('192.168.1.1')
    lease_time = pack('!L', 86400)
    dhcp_message_type = b'\x35\x01\x02'
    end_option = b'\xff'

    offer = b'\x02' + transaction_id + b'\x00\x00\x00\x00' + offer_ip + server_ip + b'\x00' * 67 + b'\x00' * 125 + b'\x63\x82\x53\x63' + dhcp_message_type + b'\x01\x04' + subnet_mask + b'\x03\x04' + router + b'\x33\x04' + lease_time + end_option
    server_socket.sendto(offer, ('<broadcast>', 68))
```
This code creates a DHCP server that listens on port 67 for DHCPDISCOVER messages from clients. When it receives a message, it extracts the transaction ID and client MAC address from the message and uses them to create a DHCPOFFER message offering an IP address to the client. The server then broadcasts the offer to the client on port 68.
