### Wireless Networks

Wireless networks are networks that use radio waves or other wireless technologies to connect devices without cables. Wireless networks can be classified into different types based on their architecture, such as autonomous, cloud-based, split-MAC, and 6G architectures.

#### Autonomous AP Architecture

Autonomous AP architecture is a wireless network architecture where each access point (AP) is responsible for everything, such as authentication, encryption, channel selection, and radio frequency management. Autonomous APs do not depend on a central controller or server, and they can operate independently or in a group. Autonomous APs are suitable for small or simple wireless networks, but they have some drawbacks, such as scalability, security, and management issues.

An example of an autonomous AP architecture is shown below:

```
+--------+         +--------+         +--------+
| Device |         | Device |         | Device |
+--------+         +--------+         +--------+
    |                  |                  |
    |                  |                  |
    |                  |                  |
+--------+         +--------+         +--------+
|  AP 1  |---------|  AP 2  |---------|  AP 3  |
+--------+         +--------+         +--------+
    |                  |                  |
    |                  |                  |
    |                  |                  |
+--------+         +--------+         +--------+
| Router |---------| Switch |---------| Server |
+--------+         +--------+         +--------+
```

#### Cloud-based Architecture

Cloud-based architecture is a wireless network architecture where the APs are managed by a cloud service provider, such as Cisco Meraki or Google Wifi. The APs connect to the cloud via the internet, and the cloud provides centralized configuration, monitoring, security, and analytics for the wireless network. Cloud-based architecture is suitable for large or distributed wireless networks, but it has some drawbacks, such as dependency on the internet, privacy, and cost.

An example of a cloud-based architecture is shown below:

```
+--------+         +--------+         +--------+
| Device |         | Device |         | Device |
+--------+         +--------+         +--------+
    |                  |                  |
    |                  |                  |
    |                  |                  |
+--------+         +--------+         +--------+
|  AP 1  |         |  AP 2  |         |  AP 3  |
+--------+         +--------+         +--------+
    |                  |                  |
    |                  |                  |
    |                  |                  |
+--------+         +--------+         +--------+
| Router |---------| Switch |---------| Router |
+--------+         +--------+         +--------+
    |                  |                  |
    |                  |                  |
    |                  |                  |
    +------------------+------------------+
                  |
                  |
                  |
              +--------+
              | Cloud  |
              +--------+
```

#### Split-MAC Architecture

Split-MAC architecture is a wireless network architecture where the APs are controlled by a wireless LAN controller (WLC), which is a dedicated device or software that manages the wireless network. The APs perform the real-time functions of the MAC layer, such as encryption, decryption, and frame transmission, while the WLC performs the non-real-time functions, such as authentication, roaming, and load balancing. Split-MAC architecture is suitable for medium or large wireless networks, but it has some drawbacks, such as complexity, single point of failure, and scalability.

An example of a split-MAC architecture is shown below:

```
+--------+         +--------+         +--------+
| Device |         | Device |         | Device |
+--------+         +--------+         +--------+
    |                  |                  |
    |                  |                  |
    |                  |                  |
+--------+         +--------+         +--------+
|  AP 1  |         |  AP 2  |         |  AP 3  |
+--------+         +--------+         +--------+
    |                  |                  |
    |                  |                  |
    |                  |                  |
    +------------------+------------------+
                  |
                  |
                  |
              +--------+
              |  WLC   |
              +--------+
                  |
                  |
                  |
+--------+         +--------+         +--------+
| Router |---------| Switch |---------| Server |
+--------+         +--------+         +--------+
```

#### 6G Architecture

6G architecture is a wireless network architecture that is still in the early stages of development, but it aims