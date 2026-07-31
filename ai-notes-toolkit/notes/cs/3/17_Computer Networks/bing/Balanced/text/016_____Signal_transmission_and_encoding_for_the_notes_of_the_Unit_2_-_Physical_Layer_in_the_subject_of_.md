### Signal transmission and encoding

- Signal transmission is the process of sending data over a physical medium, such as a cable or the airwaves, using electric or electromagnetic impulses.
- Encoding is the process of converting data into a format that can be represented by signals and understood by the sender and receiver nodes.
- Data encoding can be classified into two types: digital-to-digital encoding and analog-to-digital encoding.
- Digital-to-digital encoding is the representation of digital information (binary 1s and 0s) by a digital signal (voltage pulses). This process is also known as line coding.
- Analog-to-digital encoding is the representation of analog information (continuous waveforms) by a digital signal (voltage pulses). This process is also known as modulation.
- Different techniques of encoding data for transmission have different advantages and disadvantages, such as bandwidth efficiency, error detection, synchronization, and complexity.
- Some common techniques of digital-to-digital encoding are:
  - Non-return-to-zero (NRZ): A binary 1 is represented by a high voltage and a binary 0 is represented by a low voltage. There is no transition in the signal for consecutive bits of the same value.
  - Return-to-zero (RZ): A binary 1 is represented by a high voltage for half of the bit duration and a low voltage for the other half. A binary 0 is represented by a low voltage for the entire bit duration. There is a transition in the signal for every bit.
  - Manchester: A binary 1 is represented by a low-to-high transition in the middle of the bit duration. A binary 0 is represented by a high-to-low transition in the middle of the bit duration. There is a transition in the signal for every bit.
  - Differential Manchester: A binary 1 is represented by the absence of a transition in the middle of the bit duration. A binary 0 is represented by the presence of a transition in the middle of the bit duration. There is a transition in the signal at the beginning of every bit.
- Some common techniques of analog-to-digital encoding are:
  - Amplitude shift keying (ASK): A binary 1 is represented by a high amplitude of a carrier wave and a binary 0 is represented by a low amplitude of a carrier wave. The frequency and phase of the carrier wave remain constant.
  - Frequency shift keying (FSK): A binary 1 is represented by a high frequency of a carrier wave and a binary 0 is represented by a low frequency of a carrier wave. The amplitude and phase of the carrier wave remain constant.
  - Phase shift keying (PSK): A binary 1 is represented by a phase shift of 180 degrees in a carrier wave and a binary 0 is represented by no phase shift in a carrier wave. The amplitude and frequency of the carrier wave remain constant.