#### CIDR
CIDR stands for Classless Inter-Domain Routing. It is a method for allocating IP addresses and for IP routing. It replaces the previous classful network addressing architecture on the Internet.

CIDR notation is a compact representation of an IP address and its associated routing prefix. The notation is constructed from an IP address, a slash ('/') character, and a decimal number. The number is the count of leading 1 bits in the routing mask, traditionally called the network mask. The IP address is expressed according to the standards of IPv4 or IPv6.

For example, the IPv4 address 192.168.100.14/24 represents the given address and its associated routing prefix 192.168.100.0, or equivalently, its subnet mask 255.255.255.0, which has 24 leading 1-bits. The IPv6 address 2001:db8::/32 is a large address block with 2^96 addresses, having a 32-bit routing prefix.

CIDR notation can be used to calculate the network and host portions of an IP address, as well as the number of possible hosts in a given network. The following Python code demonstrates how to do this:

```python
# Import the ipaddress module
import ipaddress

# Define a function to calculate the network and host portions of an IP address
def calculate_network_host(ip):
  # Convert the IP address to an IPv4 or IPv6 object
  ip = ipaddress.ip_interface(ip)
  # Get the network and host portions of the IP address
  network = ip.network
  host = ip.ip
  # Get the number of possible hosts in the network
  hosts = network.num_addresses - 2 # Subtract 2 for the network and broadcast addresses
  # Return the results as a tuple
  return (network, host, hosts)

# Test the function with some examples
print(calculate_network_host("192.168.100.14/24"))
print(calculate_network_host("2001:db8::/32"))
```

The output of the code is:

```python
(IPv4Network('192.168.100.0/24'), IPv4Address('192.168.100.14'), 254)
(IPv6Network('2001:db8::/32'), IPv6Address('2001:db8::'), 79228162514264337593543950334)
```