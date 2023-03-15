#### CIDR
CIDR (Classless Inter-Domain Routing) is a way to represent IP addresses and their associated network masks. Here is an example of CIDR notation in Python:

```python
import ipaddress

# Define the IP address and network mask in CIDR notation
cidr = '192.168.1.0/24'

# Create an IPv4 network object
network = ipaddress.ip_network(cidr)

# Print the network address and network mask
print(f'Network address: {network.network_address}')
print(f'Network mask: {network.netmask}')
```
