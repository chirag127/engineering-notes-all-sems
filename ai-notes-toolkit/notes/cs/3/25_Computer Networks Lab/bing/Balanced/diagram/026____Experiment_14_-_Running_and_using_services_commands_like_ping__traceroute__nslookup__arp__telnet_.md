## Experiment 14 - Running and using services/commands like ping, traceroute, nslookup, arp, telnet, ftp, etc

- In this experiment, you will learn how to use some common network services and commands that can help you troubleshoot, test, and communicate with other devices on a network.
- These services and commands are:
  - ping: a tool that sends packets of data to a specified destination and measures the round-trip time and packet loss rate.
  - traceroute: a tool that traces the path of packets from the source to the destination and displays the routers and hosts along the way.
  - nslookup: a tool that queries the Domain Name System (DNS) and resolves hostnames to IP addresses or vice versa.
  - arp: a tool that displays and manipulates the Address Resolution Protocol (ARP) cache, which maps IP addresses to MAC addresses on a local network.
  - telnet: a protocol that allows remote login and command execution on a host using a text-based interface.
  - ftp: a protocol that allows file transfer between hosts using a client-server model.
- To run these services and commands, you will need a terminal or command prompt application on your device, and access to a network with other devices that support these protocols.
- The syntax and output of these commands may vary depending on the operating system and network configuration of your device and the destination device.
- The following are some examples of how to use these services and commands on a Windows device. You can replace the IP addresses or hostnames with the ones that are relevant to your network.

### ping
- To ping a destination, type `ping <destination>` in the terminal, where `<destination>` can be an IP address or a hostname.
- For example, to ping the IP address 8.8.8.8, which is a public DNS server provided by Google, type `ping 8.8.8.8` and press Enter.
- You should see something like this:

```
Pinging 8.8.8.8 with 32 bytes of data:
Reply from 8.8.8.8: bytes=32 time=14ms TTL=117
Reply from 8.8.8.8: bytes=32 time=13ms TTL=117
Reply from 8.8.8.8: bytes=32 time=13ms TTL=117
Reply from 8.8.8.8: bytes=32 time=13ms TTL=117

Ping statistics for 8.8.8.8:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 13ms, Maximum = 14ms, Average = 13ms
```
- This output shows that four packets of 32 bytes each were sent to 8.8.8.8, and all of them were received back with a time of 13 or 14 milliseconds and a Time To Live (TTL) of 117. The TTL is a value that indicates how many hops (routers) the packet can pass through before it expires. The ping statistics show the number of packets sent, received, and lost, and the minimum, maximum, and average round-trip times.
- To ping a hostname, such as www.google.com, type `ping www.google.com` and press Enter. You should see something like this:

```
Pinging www.google.com [142.250.74.196] with 32 bytes of data:
Reply from 142.250.74.196: bytes=32 time=14ms TTL=117
Reply from 142.250.74.196: bytes=32 time=13ms TTL=117
Reply from 142.250.74.196: bytes=32 time=13ms TTL=117
Reply from 142.250.74.196: bytes=32 time=13ms TTL=117

Ping statistics for 142.250.74.196:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 13ms, Maximum = 14ms, Average = 13ms
```
- This output shows that the hostname www.google.com was resolved to the IP address 142.250.74.196, and the rest of the output is similar to the previous example.
- To stop the ping command, press Ctrl+C. You can also use some options to modify the ping behavior, such as `-n` to specify the number of packets to send, `-l` to specify the