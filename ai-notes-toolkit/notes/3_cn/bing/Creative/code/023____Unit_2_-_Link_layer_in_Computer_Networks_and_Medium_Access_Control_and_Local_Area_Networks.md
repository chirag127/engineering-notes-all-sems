## Unit 2 - Link layer in Computer Networks and Medium Access Control and Local Area Networks

The link layer is the lowest layer in the Internet protocol suite, the networking architecture of the Internet. The link layer is the group of methods and communications protocols confined to the link that a host is physically connected to. The link layer is responsible for transferring data between nodes on a network segment across the physical layer.

The data link layer is divided into two sublayers: data link control and multiple access resolution/protocol. Data link control handles the framing, addressing, and error control of the data packets. Multiple access resolution/protocol handles the contention and collision issues that arise when multiple nodes try to access the same channel or medium.

Some of the common multiple access protocols are:

- ALOHA: A simple protocol that allows nodes to transmit data whenever they have it, without coordination with other nodes. This leads to high collision probability and low channel utilization.
- CSMA: A protocol that allows nodes to sense the channel before transmitting data, and defer transmission if the channel is busy. This reduces the collision probability but does not eliminate it.
- CSMA/CA: A protocol that uses a random backoff mechanism to avoid collisions. Nodes that sense a busy channel wait for a random amount of time before trying to transmit again. This is used in wireless networks such as IEEE 802.11.
- CSMA/CD: A protocol that detects collisions and aborts transmission when they occur. Nodes that detect a collision wait for a random amount of time before trying to transmit again. This is used in wired networks such as Ethernet.

A local area network (LAN) is a network that connects devices within a limited geographical area, such as a building or a campus. LANs typically use the data link layer protocols to communicate among the devices. Some of the common LAN technologies are:

- Ethernet: A wired LAN technology that uses CSMA/CD as the multiple access protocol. Ethernet operates at 10 Mbps, 100 Mbps, 1 Gbps, or 10 Gbps, depending on the type of cable and hardware used.
- Wi-Fi: A wireless LAN technology that uses CSMA/CA as the multiple access protocol. Wi-Fi operates at 2.4 GHz or 5 GHz frequency bands, and supports data rates up to 600 Mbps, depending on the standard and hardware used.
- Bluetooth: A wireless LAN technology that uses frequency hopping spread spectrum (FHSS) as the multiple access protocol. Bluetooth operates at 2.4 GHz frequency band, and supports data rates up to 3 Mbps, depending on the version and hardware used.

The following is a sample code in Python that implements a simple CSMA/CD protocol for a wired LAN with four nodes:

```python
# Define the parameters
N = 4 # Number of nodes
T = 100 # Time slots
P = 0.1 # Probability of transmission
C = 0.5 # Probability of collision
S = 0.9 # Probability of successful transmission

# Initialize the variables
channel = [0] * T # Channel state
nodes = [0] * N # Node state
backoff = [0] * N # Backoff time
collisions = 0 # Collision count
successes = 0 # Success count

# Simulate the protocol
for t in range(T):
  # Check if any node wants to transmit
  for i in range(N):
    if nodes[i] == 0: # Idle node
      if random.random() < P: # Node decides to transmit
        nodes[i] = 1 # Node becomes active
    elif nodes[i] == 1: # Active node
      if channel[t] == 0: # Channel is free
        channel[t] = i + 1 # Node occupies the channel
      else: # Channel is busy
        nodes[i] = 2 # Node becomes collided
        channel[t] = -1 # Channel becomes collided
  # Check if any collision occurs
  if channel[t] == -1: # Collided channel
    collisions += 1 # Increment collision count
    for i in range(N):
      if nodes[i] == 2: # Collided node
        backoff[i] = random.randint(1, 4) # Node chooses a random backoff time
        nodes[i] = 3 # Node becomes backoff

```
