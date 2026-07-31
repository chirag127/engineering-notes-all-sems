### Fundamentals of amplitude modulation and demodulation techniques

- Amplitude modulation (AM) is a technique to transmit information via radio carrier waveform by varying the amplitude of the carrier signal in proportion to the amplitude of the modulation signal that is to be transmitted .
- The modulation signal can be an audio signal, a video signal, or any other type of signal that carries information.
- The carrier signal is usually a high-frequency sinusoidal wave that can propagate efficiently through the transmission medium, such as air, cable, or optical fiber.
- The modulated signal has the same frequency as the carrier signal, but its amplitude varies according to the modulation signal.
- The modulated signal can be represented as:

$$
s(t) = A_c[1 + k_a m(t)]\cos(2\pi f_c t)
$$

where $s(t)$ is the modulated signal, $A_c$ is the amplitude of the carrier signal, $k_a$ is the amplitude modulation index, $m(t)$ is the modulation signal, and $f_c$ is the frequency of the carrier signal .

- The modulation index $k_a$ determines the degree of modulation and the bandwidth of the modulated signal. It can vary from 0 to 1, where 0 means no modulation and 1 means 100% modulation.
- The bandwidth of the modulated signal is twice the bandwidth of the modulation signal, and it is centered at the carrier frequency .
- The modulated signal can be demodulated at the receiver's end using various techniques, such as envelope detection, synchronous detection, or coherent detection  .
- Envelope detection is the simplest and most common technique for demodulating AM signals. It uses a diode and a capacitor to extract the envelope of the modulated signal, which is proportional to the modulation signal  .
- Synchronous detection or coherent detection is a more complex and accurate technique for demodulating AM signals. It uses a local oscillator that is synchronized with the carrier signal to multiply the modulated signal with a cosine wave of the same frequency and phase as the carrier signal. This produces a signal that is proportional to the modulation signal, but with a DC offset that can be removed by a low-pass filter  .
- Amplitude modulation and demodulation techniques are widely used in radio broadcasting, television, and telecommunications. They have advantages such as simplicity, low cost, and compatibility with existing systems, but they also have disadvantages such as low efficiency, high noise susceptibility, and limited bandwidth .