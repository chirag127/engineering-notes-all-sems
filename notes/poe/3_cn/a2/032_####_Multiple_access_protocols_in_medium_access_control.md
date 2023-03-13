 Here is the content in markdown format on the topic #### Multiple access protocols in medium access control:

#### Multiple access protocols in medium access control

The multiple access protocols determine how multiple terminals or nodes share the common communication channel in a network. The main types of multiple access protocols are:

1. Frequency-division multiple access (FDMA): The available bandwidth of the channel is divided into several frequency bands or channels and each terminal is allocated a different frequency band. This is analogous to radio stations transmitting on different frequencies. FDMA prevents interference between the terminals but the bandwidth efficiency may not be very high if the traffic pattern results in some frequency bands being unused at times.

2. Time-division multiple access (TDMA): The time axis is divided into slots of time and each terminal is allocated a different time slot in the frame. This is analogous to different people taking turns speaking in a meeting. TDMA prevents interference and can achieve high bandwidth efficiency but it requires careful synchronization between the terminals and the base station.

3. Code-division multiple access (CDMA): Each terminal is allocated a code word and data signals are spread over the available bandwidth using these code words. As long as the code words are nearly orthogonal, the data signals can be separated even though they occupy the same time interval and frequency band. CDMA achieves very high bandwidth efficiency but it may be more complex to implement than FDMA and TDMA. It is used in 2G and 3G cellular systems.

4. Carrier-sense multiple access (CSMA): With CSMA, the terminals detect the state of the channel before transmitting. If the channel is sensed to be clear, the terminals may transmit. However, there is a possibility of collisions if two or more terminals sense the channel to be clear and transmit simultaneously. CSMA is relatively simple but the throughput efficiency depends on the traffic pattern and how well collisions are handled. CSMA with collision detection (CSMA/CD) is used in Ethernet.

[Detailed diagrams, examples, advantages, disadvantages, applications, etc. can be added here if helpful for learning.]