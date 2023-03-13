#### Signal transmission and encoding in Computer Networks

- Signal transmission is the process of sending digital or analog data over a physical medium such as copper wire, optical fiber, or wireless channel.
- Encoding is the process of converting data into a specific format that can be recognized and interpreted by the receiver.
- Encoding can be classified into two types: digital-to-digital encoding and analog-to-digital encoding.

- Digital-to-digital encoding is the representation of digital information by a digital signal. It is also known as line coding. It involves converting a stream of bits into a series of voltage pulses, light pulses, or electromagnetic waves that can be transmitted over a wire or a wireless channel.
- There are different techniques of digital-to-digital encoding, such as:
  - Non-return-to-zero (NRZ): In this technique, a high voltage represents a 1 bit and a low voltage represents a 0 bit. There is no change in the signal level for consecutive bits of the same value. This technique is simple but suffers from synchronization problems and DC component issues.
  - Return-to-zero (RZ): In this technique, a high voltage represents a 1 bit and a low voltage represents a 0 bit. However, the signal level returns to zero halfway through each bit duration. This technique reduces the DC component problem but increases the bandwidth requirement and the synchronization problem.
  - Manchester: In this technique, a transition from low to high voltage represents a 1 bit and a transition from high to low voltage represents a 0 bit. There is always a transition at the middle of each bit duration. This technique eliminates the DC component problem and the synchronization problem but doubles the bandwidth requirement.
  - Differential Manchester: In this technique, a transition at the beginning of a bit duration represents a 0 bit and no transition at the beginning of a bit duration represents a 1 bit. There is always a transition at the middle of each bit duration. This technique is similar to Manchester but uses differential encoding, which means that the signal is encoded based on the previous bit rather than the current bit.
  - 4B/5B: In this technique, every 4 bits of data are encoded into 5 bits of signal, using a predefined mapping table. The 5-bit signal has at least one transition and no more than two consecutive 0s or 1s. This technique reduces the DC component problem and the synchronization problem but increases the overhead by 25%.

- Analog-to-digital encoding is the representation of analog information by a digital signal. It is also known as digitization or sampling. It involves converting a continuous analog signal into a discrete sequence of bits that can be transmitted over a digital channel.
- There are three steps involved in analog-to-digital encoding, such as:
  - Sampling: In this step, the analog signal is measured at regular intervals, called the sampling rate or sampling frequency. The sampling rate should be at least twice the highest frequency component of the analog signal, according to the Nyquist theorem. The result of sampling is a sequence of samples, each representing the amplitude of the analog signal at a specific point in time.
  - Quantization: In this step, each sample is assigned a discrete value, called a quantization level, from a finite set of possible values. The number of quantization levels depends on the number of bits per sample, which determines the resolution or accuracy of the digitization. The difference between the actual sample value and the quantization level is called the quantization error or noise.
  - Encoding: In this step, each quantization level is encoded into a binary code, using a predefined mapping scheme. The binary code can be transmitted over a digital channel as a digital signal.

- A mnemonic to remember the steps of analog-to-digital encoding is SQE: Sampling, Quantization, Encoding.