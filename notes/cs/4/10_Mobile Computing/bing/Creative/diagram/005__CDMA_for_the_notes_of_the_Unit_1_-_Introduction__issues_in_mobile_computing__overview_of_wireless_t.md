The following is a detailed ASCII diagram for CDMA for the notes of the Unit 1 - Introduction, issues in mobile computing, overview of wireless telephony: cellular concept, GSM: in the subject of Mobile Computing.

CDMA is a channel access method that allows multiple users to transmit data simultaneously over a single communication channel by using different spreading codes. CDMA uses the principle of spread spectrum, which increases the bandwidth of the signal and reduces the interference level. CDMA is sometimes referred to as spread spectrum multiple access (SSMA).

There are two main types of CDMA: direct sequence CDMA (DS-CDMA) and frequency hopping CDMA (FH-CDMA).

In DS-CDMA, each user's data is multiplied by a unique pseudorandom code sequence, which spreads the signal over a wider bandwidth. The resulting signal is then modulated and transmitted over the channel. At the receiver, the same code sequence is used to despread the signal and recover the original data. The code sequences are designed to be orthogonal, meaning that they have zero cross-correlation. This allows the receiver to separate the signals from different users by using a matched filter.

In FH-CDMA, each user's data is modulated by a carrier frequency that changes according to a predefined hopping pattern. The hopping pattern is determined by a pseudorandom code sequence, which is unique for each user. The resulting signal is then transmitted over the channel. At the receiver, the same code sequence is used to synchronize the frequency hopping and demodulate the signal. The code sequences are designed to have low cross-correlation, meaning that they have minimal interference. This allows the receiver to separate the signals from different users by using a frequency discriminator.

The following diagram illustrates the basic architecture of a DS-CDMA system:

```
+-----------------+     +-----------------+     +-----------------+
| Data source     |     | Data source     |     | Data source     |
+-----------------+     +-----------------+     +-----------------+
        |                       |                       |
        |                       |                       |
        |                       |                       |
        v                       v                       v
+-----------------+     +-----------------+     +-----------------+
| Spreading code  |     | Spreading code  |     | Spreading code  |
| generator       |     | generator       |     | generator       |
+-----------------+     +-----------------+     +-----------------+
        |                       |                       |
        |                       |                       |
        |                       |                       |
        v                       v                       v
+-----------------+     +-----------------+     +-----------------+
| Spreading       |     | Spreading       |     | Spreading       |
| (multiplication)|     | (multiplication)|     | (multiplication)|
+-----------------+     +-----------------+     +-----------------+
        |                       |                       |
        |                       |                       |
        |                       |                       |
        v                       v                       v
+-----------------+     +-----------------+     +-----------------+
| Modulation      |     | Modulation      |     | Modulation      |
+-----------------+     +-----------------+     +-----------------+
        |                       |                       |
        |                       |                       |
        |                       |                       |
        v                       v                       v
+-----------------+     +-----------------+     +-----------------+
| Transmission    |     | Transmission    |     | Transmission    |
+-----------------+     +-----------------+     +-----------------+
        |                       |                       |
        |                       |                       |
        |                       |                       |
        v                       v                       v
+---------------------------------------------------------------+
| Channel                                                      |
+---------------------------------------------------------------+
        |                       |                       |
        |                       |                       |
        |                       |                       |
        v                       v                       v
+-----------------+     +-----------------+     +-----------------+
| Reception       |     | Reception       |     | Reception       |
+-----------------+     +-----------------+     +-----------------+
        |                       |                       |
        |                       |                       |
        |                       |                       |
        v                       v                       v
+-----------------+     +-----------------+     +-----------------+
| Demodulation    |     | Demodulation    |     | Demodulation    |
+-----------------+     +-----------------+     +-----------------+
        |                       |                       |
        |                       |                       |
        |                       |                       |
        v                       v                       v
+-----------------+     +-----------------+     +-----------------+
| Despreading     |