The channel structure in GSM is based on the distinction between physical channels and logical channels. Physical channels are defined by the frequency and time slot used for transmission and reception. Logical channels are defined by the type and content of the information carried by the physical channels.

The following diagram illustrates the basic architecture of a GSM network, showing the different types of physical and logical channels:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Mobile Station |       | Base Station    |       | Network         |
|                 |       | Subsystem       |       | Switching       |
|                 |       |                 |       | Subsystem       |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  SIM Card       |       |  BTS            |       |  MSC            |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Radio          |       |  BSC            |       |  VLR            |
|  Transceiver    |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Display        |       |  Transcoder     |       |  HLR            |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  DSP            |       |                 |       |  EIR            |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|                 |       |                 |       |  AUC            |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|                 |       |                 |       |  GMSC           |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|                 |       |                 |       |  PSTN/ISDN      |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|                 |       |                 |       |  Other GSM      |
|                 |       |                 |       |  Networks       |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+

```

The physical channels are divided into two types: traffic channels (TCH) and control channels (CCH). Traffic channels carry voice or data information between the mobile station and the network. Control channels carry signaling and synchronization information between the mobile station and the base station.

The logical channels are divided into two types: traffic channels (TCH) and control channels (CCH). Traffic channels are further divided into full rate (TCH/F) and half rate (TCH/H) channels, depending on the data rate used. Control channels are further divided into broadcast channels (BCH), common control channels (CCCH), dedicated control channels (DCCH), and associated control channels (ACCH), depending on the function and direction of the information.

The following diagram illustrates the mapping of logical channels to physical channels in GSM:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Mobile Station |       | Base Station    |       | Network         |
|                 |       | Subsystem       |       | Switching       |
|                 |       |                 |       | Subsystem       |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  SIM Card       |       |  BTS            |       |  MSC            |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Radio          |       |  BSC            |       |  V