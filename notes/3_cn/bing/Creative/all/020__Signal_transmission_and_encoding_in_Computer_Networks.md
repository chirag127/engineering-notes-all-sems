#### Signal transmission and encoding in Computer Networks

- Signal transmission is the process of sending data in the form of electrical, optical, or wireless signals over a physical medium such as a cable, a fiber, or the air.
- Encoding is the process of converting a stream of data bits into a predefined code that can be represented by the signals on the medium.
- Encoding is necessary to ensure reliable and efficient transmission of data over the network.
- Encoding schemes can be classified into two categories: digital data to digital signals and digital data to analog signals.

##### Digital data to digital signals

- This category involves encoding binary data (0s and 1s) into discrete signals (high and low) that can be transmitted over a digital medium such as a twisted pair or a coaxial cable.
- The main challenge of this category is to deal with the problems of baseline wander and clock recovery.
- Baseline wander is the phenomenon of the average signal level drifting away from the ideal value due to long sequences of 0s or 1s, making it difficult to distinguish between the signal levels.
- Clock recovery is the process of synchronizing the sender and the receiver clocks to ensure correct interpretation of the signal timing and duration.
- Some of the common encoding schemes in this category are:

###### Non-Return to Zero (NRZ)

- In NRZ encoding, a 1 bit is represented by a high signal and a 0 bit is represented by a low signal.
- NRZ encoding is simple and efficient, but it suffers from baseline wander and clock recovery problems, especially when there are long sequences of 0s or 1s.
- NRZ encoding has two variations: NRZ-Level (NRZ-L) and NRZ-Inverted (NRZ-I).
- In NRZ-L, the signal level is determined by the bit value: high for 1 and low for 0.
- In NRZ-I, the signal level is determined by the bit transition: a change for 1 and no change for 0.
- NRZ-I has an advantage over NRZ-L in that it has more transitions, which helps in clock recovery.
- However, NRZ-I still suffers from baseline wander and clock recovery problems when there are long sequences of 0s or 1s.

###### Bi-phase encoding

- Bi-phase encoding is a technique that introduces more transitions in the signal to overcome the baseline wander and clock recovery problems of NRZ encoding.
- Bi-phase encoding has two variations: Manchester encoding and Differential Manchester encoding.
- In Manchester encoding, a 1 bit is represented by a low-to-high transition in the middle of the bit duration, and a 0 bit is represented by a high-to-low transition in the middle of the bit duration.
- In Differential Manchester encoding, a 1 bit is represented by the absence of a transition in the middle of the bit duration, and a 0 bit is represented by the presence of a transition in the middle of the bit duration.
- Additionally, Differential Manchester encoding uses the transition at the beginning of the bit duration to indicate the bit value: a change for 1 and no change for 0.
- Bi-phase encoding has an advantage over NRZ encoding in that it has at least one transition per bit, which helps in clock recovery and avoids baseline wander.
- However, bi-phase encoding has a disadvantage in that it requires twice the bandwidth of NRZ encoding, since it uses two signal levels per bit.

###### Block encoding

- Block encoding is a technique that transforms a block of data bits into a longer block of code bits that can be transmitted over the medium.
- Block encoding has two objectives: to ensure DC balance and to provide error detection.
- DC balance means that the number of 0s and 1s in the code block are equal or nearly equal, which avoids baseline wander and reduces the power consumption of the signal.
- Error detection means that the code block has some redundancy that allows the receiver to detect and correct some errors in the transmission.
- Some of the common block encoding schemes are:

####### 4B/5B encoding

- In 4B/5B encoding, a block of 4 data bits is mapped to a block of 5 code bits, using a predefined table of 16 possible mappings.
- The 5 code bits are chosen such that they have no more than one leading 0 and no more than two trailing 0s, which ensures DC balance and avoids long sequences of 0s.
- The 5 code bits are also chosen such that they have at least two transitions, which helps in clock recovery.
- The 4B/5B encoding has an