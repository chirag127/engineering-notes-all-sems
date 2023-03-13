### CDMA

CDMA stands for Code Division Multiple Access. It is a technique that allows multiple users to simultaneously transmit data signals over a common channel by assigning unique spreading code to each individual user. This leads to the increasing of bandwidth used by transmitting stations from a few Hz to a few MHz.

The following diagram illustrates the basic architecture of a CDMA system for transmission and reception of the signal:

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
| Data Source    |     | Data Source    |     | Data Source    |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
| Spreading Code |     | Spreading Code |     | Spreading Code |
| Generator      |     | Generator      |     | Generator      |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
| Modulator      |     | Modulator      |     | Modulator      |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       +---------------------+---------------------+
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
| Demodulator    |     | Demodulator    |     | Demodulator    |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
| Spreading Code |     | Spreading Code |     | Spreading Code |
| Generator      |     | Generator      |     | Generator      |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
| Data Sink      |     | Data Sink      |     | Data Sink      |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
```

In this diagram, each data source represents a user who wants to transmit data over the channel. Each