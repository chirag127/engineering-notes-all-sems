## Experiment 4 - Write a code simulating PING and TRACEROUTE commands

1. **PING** is a computer network administration software utility used to test the reachability of a host on an Internet Protocol (IP) network. It measures the round-trip time for messages sent from the originating host to a destination computer that are echoed back to the source.

2. **TRACEROUTE** is a computer network diagnostic tool for displaying the route (path) and measuring transit delays of packets across an Internet Protocol (IP) network.

3. To simulate these commands, we can write a code in a programming language such as Python.

4. For the PING command, we can use the `ping` module in Python. Here is an example code:

```python
import ping

def ping_host(host):
    try:
        delay = ping.Ping(host).do()
    except ping.socket.error as e:
        print("Ping Error:", e)
    else:
        print(host, delay)
```

5. For the TRACEROUTE command, we can use the `scapy` module in Python. Here is an example code:

```python
from scapy.all import *

def traceroute_host(host):
    res, unans = traceroute(host, maxttl=30)
    res.show()
```

6. These codes can be modified and expanded to include additional features and functionalities as per the requirements of the simulation.