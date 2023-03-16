# MAC protocol survey for IoT

- MAC protocol stands for medium access control protocol, which is the first protocol layer above the physical layer in wireless networks.
- MAC protocol is responsible for controlling the access of the nodes to the shared medium, such as radio frequency or optical fiber.
- MAC protocol is essential for the performance and efficiency of wireless networks, especially for the Internet of Things (IoT), which is a network of interconnected devices that can communicate and exchange data without human intervention.
- IoT devices have diverse characteristics and requirements, such as low power consumption, high scalability, long range, high reliability, and low latency.
- Therefore, different MAC protocols have been proposed and developed for IoT applications, based on various criteria and techniques, such as coverage, reservation, scheduling, and coordination.
- In this survey, we will review some of the MAC protocols that are suitable for IoT, focusing on the IEEE 802.11ah standard, also known as WiFi HaLow, which is a scalable solution for medium-range communication in IoT.
- We will also discuss some of the challenges and open issues that need to be addressed for the future development and deployment of MAC protocols for IoT.

## IEEE 802.11ah WiFi HaLow

- IEEE 802.11ah is a sub-gigahertz (SGHz) WiFi standard that operates in the frequency bands below 1 GHz, such as 900 MHz, 868 MHz, and 433 MHz.
- IEEE 802.11ah aims to provide a low-power, long-range, and high-density wireless solution for IoT and machine-to-machine (M2M) communication, with a target range of up to 1 km and a maximum number of 8192 stations per access point (AP).
- IEEE 802.11ah leverages various innovative medium access control (MAC) techniques to achieve these goals, such as:

  - Restricted access window (RAW): A mechanism that divides the stations into groups and assigns each group a time window to access the channel, reducing the contention and collision among the stations.
  - Target wake time (TWT): A mechanism that allows the stations to negotiate with the AP their wake-up and sleep schedules, reducing the energy consumption and increasing the battery life of the stations.
  - Short MAC header: A mechanism that reduces the overhead and latency of the MAC frames by using a shorter MAC header, which is only 2 bytes long, compared to the 34 bytes of the legacy MAC header.
  - Relay: A mechanism that enables the stations to relay the frames of other stations that are out of the range of the AP, extending the coverage and improving the reliability of the network.

## Classification of MAC protocols for IoT

- MAC protocols for IoT can be classified into different categories, based on various criteria, such as:

  - Coverage: The range of the wireless communication, which can be short (up to 10 meters), medium (up to 100 meters), or long (up to 1 km or more).
  - Reservation: The technique of allocating the channel resources to the stations, which can be contention-based (without reservation or scheduling), where the stations compete for the channel access, or contention-free (with reservation or scheduling), where the stations reserve the channel access in advance.
  - Scheduling: The technique of organizing the channel access of the stations, which can be centralized, where the AP coordinates the channel access of the stations, or distributed, where the stations coordinate the channel access among themselves.
  - Coordination: The technique of managing the interference and collision among the stations, which can be synchronous, where the stations synchronize their clocks and transmissions, or asynchronous, where the stations transmit independently without synchronization.

- Some examples of MAC protocols for IoT based on these criteria are:

  - Short-range, contention-based, distributed, and asynchronous: IEEE 802.15.4 ZigBee, which is a low-power, low-data-rate, and low-cost wireless protocol for sensor networks and smart home applications.
  - Medium-range, contention-based, centralized, and synchronous: IEEE 802.11ah WiFi HaLow, which is a low-power, long-range, and high-density wireless protocol for IoT and M2M communication.
  - Long-range, contention-free, distributed, and asynchronous: LoRaWAN, which is a low-power, wide-area network (LPWAN) protocol that uses a chirp spread spectrum (CSS) modulation technique to enable long-range and low-data-rate communication for IoT devices.

## Challenges and open issues for MAC protocols for IoT

- MAC protocols for IoT face several challenges and open issues that need to be addressed for the future development and deployment