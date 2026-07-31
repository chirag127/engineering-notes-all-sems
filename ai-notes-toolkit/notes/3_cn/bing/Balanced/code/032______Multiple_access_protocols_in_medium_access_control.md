#### Multiple access protocols in medium access control

Multiple access protocols are a set of protocols operating in the Medium Access Control sublayer (MAC sublayer) of the Open Systems Interconnection (OSI) model  . These protocols allow a number of nodes or users to access a shared network channel.

There are different types of multiple access protocols, such as:

- Random access protocols: In these protocols, all stations have the same priority and can send data depending on the medium's state (idle or busy). Examples of random access protocols are ALOHA, Carrier Sense Multiple Access (CSMA), CSMA with Collision Avoidance (CSMA/CA) and CSMA with Collision Detection (CSMA/CD) .
- Controlled access protocols: In these protocols, the access to the medium is controlled by a central station or a distributed algorithm. Examples of controlled access protocols are Reservation, Polling and Token Passing.
- Channelization protocols: In these protocols, the available bandwidth of the channel is divided into smaller sub-channels that are assigned to different stations. Examples of channelization protocols are Frequency Division Multiple Access (FDMA), Time Division Multiple Access (TDMA) and Code Division Multiple Access (CDMA).

The choice of a multiple access protocol depends on various factors, such as the network topology, the traffic characteristics, the channel conditions and the performance requirements.

Here is a pseudocode example of a random access protocol, CSMA/CD:

```
# CSMA/CD protocol
# Assume that each station has a variable called state that can be either idle, transmitting or waiting
# Assume that each station can sense the channel state (busy or idle) and detect collisions
# Assume that each station has a backoff timer that is initialized randomly

# When a station has a frame to send
if state == idle and channel == idle:
  state = transmitting
  send frame
  start timer
else:
  state = waiting
  wait until channel is idle

# When a station is transmitting a frame
if timer expires:
  state = idle
  reset timer
elif collision is detected:
  state = waiting
  abort transmission
  increase backoff time
  start timer

# When a station is waiting to send a frame
if timer expires:
  state = idle
  reset timer
elif channel is idle:
  state = transmitting
  send frame
  start timer
```