#### Channel allocation in medium access control

- Channel allocation is the process of assigning a portion of the available bandwidth to different users or devices in a communication network.
- Channel allocation can be classified into three types: fixed, dynamic, and hybrid.
- Fixed channel allocation (FCA) assigns a fixed number of channels to each user or device, regardless of their traffic demand or activity. FCA is simple and efficient, but it may result in underutilization or overutilization of the channels.
- Dynamic channel allocation (DCA) assigns channels to users or devices on demand, based on their traffic demand or activity. DCA is flexible and adaptive, but it may incur higher overhead and complexity.
- Hybrid channel allocation (HCA) combines the advantages of FCA and DCA by using both fixed and dynamic channels. HCA can achieve better performance and efficiency, but it may require more coordination and synchronization.

- A mnemonic to remember the types of channel allocation is: **F**ix **D**ynamic **H**ybrid (FDH).
- An example of FCA is frequency division multiple access (FDMA), which divides the frequency spectrum into fixed channels and assigns them to different users or devices.
- An example of DCA is carrier sense multiple access (CSMA), which allows users or devices to sense the channel before transmitting and avoid collisions with other users or devices.
- An example of HCA is time division multiple access (TDMA), which divides the time into fixed slots and assigns them to different users or devices, but also allows dynamic allocation of slots within a frame.

- A diagram to illustrate the types of channel allocation is:

```
|<----------------- Frequency spectrum ----------------->|
|<----- FCA ----->|<----- DCA ----->|<----- HCA ----->|
|                 |                 |                 |
|  |----|----|----|                 |  |----|----|----|
|  | A  | B  | C  |                 |  | A  | B  | C  |
|  |----|----|----|                 |  |----|----|----|
|                 |                 |                 |
|  |----|----|----|                 |  |----|----|----|
|  | D  | E  | F  |                 |  | D  | E  | F  |
|  |----|----|----|                 |  |----|----|----|
|                 |                 |                 |
|  |----|----|----|                 |  |----|----|----|
|  | G  | H  | I  |                 |  | G  | H  | I  |
|  |----|----|----|                 |  |----|----|----|
|                 |                 |                 |
|                 |  |----|----|----|                 |
|                 |  | A  | B  | C  |                 |
|                 |  |----|----|----|                 |
|                 |                 |                 |
|                 |  |----|----|----|                 |
|                 |  | D  | E  | F  |                 |
|                 |  |----|----|----|                 |
|                 |                 |                 |
|                 |  |----|----|----|                 |
|                 |  | G  | H  | I  |                 |
|                 |  |----|----|----|                 |
|                 |                 |                 |
|                 |                 |  |----|----|----|
|                 |                 |  | A  | B  | C  |
|                 |                 |  |----|----|----|
|                 |                 |                 |
|                 |                 |  |----|----|----|
|                 |                 |  | D  | E  | F  |
|                 |                 |  |----|----|----|
|                 |                 |                 |
|                 |                 |  |----|----|----|
|                 |                 |  | G  | H  | I  |
|                 |                 |  |----|----|----|
|                 |                 |                 |
|                 |                 |  |----|----|----|
|                 |                 |  | A  | B  | C  |
|                 |                 |  |----|----|----|
|                 |                 |                 |
|                 |                 |  |----|----|----|
|                 |                 |  | D  | E  | F  |
|                 |                 |  |----|----|----|
|                 |                 |                 |
|