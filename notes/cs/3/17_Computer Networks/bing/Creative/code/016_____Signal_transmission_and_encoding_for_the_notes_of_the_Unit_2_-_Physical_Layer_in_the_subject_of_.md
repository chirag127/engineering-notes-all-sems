### Signal transmission and encoding

- Signal transmission is the process of sending data over a physical medium, such as a cable or the airwaves, using electric or electromagnetic impulses .
- Encoding is the process of converting data into a format that can be transmitted by a signal, such as binary digits (0s and 1s) or voltage levels  .
- Encoding can be classified into two types: digital-to-digital encoding and analog-to-digital encoding.
- Digital-to-digital encoding is the representation of digital information by a digital signal, such as a series of voltage pulses. This process is also known as line coding.
- Analog-to-digital encoding is the representation of analog information by a digital signal, such as a sequence of binary digits. This process is also known as sampling and quantization.
- Encoding techniques can have different properties, such as bandwidth, bit rate, bit error rate, synchronization, and complexity  .
- Some common encoding techniques are:
  - Non-return-to-zero (NRZ): A binary encoding scheme that uses two voltage levels to represent 0s and 1s, without returning to a zero level between bits .
  - Return-to-zero (RZ): A binary encoding scheme that uses three voltage levels to represent 0s and 1s, and returns to a zero level between bits .
  - Manchester: A binary encoding scheme that uses a transition from high to low voltage to represent a 0, and a transition from low to high voltage to represent a 1 .
  - Differential Manchester: A binary encoding scheme that uses a transition at the beginning of each bit period to represent a 0, and no transition to represent a 1 .
  - 4B/5B: A block encoding scheme that maps every 4-bit group to a 5-bit code, and uses the extra bit to ensure that there are no more than three consecutive 0s or 1s in the encoded signal .
  - Pulse code modulation (PCM): An analog-to-digital encoding scheme that samples the analog signal at regular intervals, and assigns a binary code to each sample based on its amplitude .
  - Delta modulation (DM): An analog-to-digital encoding scheme that samples the analog signal at regular intervals, and assigns a binary code to each sample based on the difference between its amplitude and the previous sample .