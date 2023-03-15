## Experiment 4 - Write a code simulating PING and TRACEROUTE commands

1. **PING** is a computer network administration software utility used to test the reachability of a host on an Internet Protocol (IP) network. It measures the round-trip time for messages sent from the originating host to a destination computer that are echoed back to the source.

2. **TRACEROUTE** is a computer network diagnostic tool for displaying the route (path) and measuring transit delays of packets across an Internet Protocol (IP) network.

3. To simulate the PING command, you can write a program that sends an Internet Control Message Protocol (ICMP) echo request to a specified host and waits for a response. The program can measure the time it takes for the response to arrive and display it to the user.

4. To simulate the TRACEROUTE command, you can write a program that sends a series of ICMP echo requests with increasing Time to Live (TTL) values. The program can record the IP addresses of the routers that respond with ICMP Time Exceeded messages and display the route to the user.

5. Here is an example of a Python program that simulates the PING command:

```python
import os
hostname = "google.com"
response = os.system("ping -c 1 " + hostname)
if response == 0:
    print(hostname + ' is up!')
else:
    print(hostname + ' is down!')
```

6. Here is an example of a Python program that simulates the TRACEROUTE command:

```python
import os
hostname = "google.com"
for i in range(1, 30):
    response = os.system("traceroute -m " + str(i) + " " + hostname)
    if response == 0:
        break
```

7. These programs can be modified and expanded to include additional features and functionality, such as displaying the round-trip time for each hop in the route or allowing the user to specify the maximum number of hops to trace.