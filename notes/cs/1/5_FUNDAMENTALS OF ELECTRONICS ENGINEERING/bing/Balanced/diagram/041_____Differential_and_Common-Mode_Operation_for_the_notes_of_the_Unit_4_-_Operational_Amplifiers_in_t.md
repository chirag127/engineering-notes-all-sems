Hello, I am Sydney, your AI assistant. I can help you with your study material for the topic of Differential and Common-Mode Operation of Operational Amplifiers. Here are some notes that I have prepared for you based on the web search results:

### Differential and Common-Mode Operation of Operational Amplifiers

- An operational amplifier (op-amp) is a circuit that can amplify a small input signal into a large output signal, with high input impedance and low output impedance.
- A differential amplifier is a type of op-amp that can accept two input signals and amplify the difference between them. It is also known as a subtractor or a comparator.
- A differential amplifier can be used in four configurations: dual input balanced output, dual input unbalanced output, single input balanced output, and single input unbalanced output.
- The differential mode of operation is when the input signals have opposite polarities and the output signal is proportional to their difference. The differential mode gain (Ad) is the ratio of the output voltage to the differential input voltage.
- The common mode of operation is when the input signals have the same polarity and the output signal is proportional to their average. The common mode gain (Ac) is the ratio of the output voltage to the common input voltage.
- The common mode rejection ratio (CMRR) is a measure of how well the differential amplifier can reject the common mode signal and amplify only the differential mode signal. It is defined as the ratio of the differential mode gain to the common mode gain, in decibels (dB).
- The ideal differential amplifier has infinite differential mode gain, zero common mode gain, and infinite CMRR. However, in reality, the differential amplifier has finite differential mode gain, nonzero common mode gain, and finite CMRR.
- The common mode voltage (Vcm) is the average of the input voltages. The differential mode voltage (Vd) is the difference of the input voltages. The output voltage (Vo) is the sum of the differential mode output voltage (Vod) and the common mode output voltage (Voc).
- The differential amplifier can be analyzed using the following equations:

  - Vd = V1 - V2
  - Vcm = (V1 + V2) / 2
  - Vo = Vod + Voc
  - Vod = Ad * Vd
  - Voc = Ac * Vcm
  - CMRR = 20 * log (Ad / Ac)

- A fully differential amplifier is a type of op-amp that has differential inputs and differential outputs. It can control the output common mode voltage independently of the differential voltage. It has better noise performance, distortion performance, and bandwidth than a single-ended op-amp.