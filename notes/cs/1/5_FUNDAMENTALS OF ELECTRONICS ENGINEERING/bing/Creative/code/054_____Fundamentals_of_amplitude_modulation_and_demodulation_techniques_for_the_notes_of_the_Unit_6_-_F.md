### Fundamentals of amplitude modulation and demodulation techniques

- Amplitude modulation (AM) is a technique to transmit information via radio carrier waveform by varying the amplitude of the carrier signal in proportion to the amplitude of the modulation signal that is to be transmitted .
- The modulation signal can be an audio signal, a video signal, or any other type of signal that carries information.
- The carrier signal is usually a high-frequency sinusoidal wave that can be easily transmitted and received by antennas.
- The modulated signal has the same frequency as the carrier signal, but its amplitude varies according to the modulation signal.
- The modulated signal can be represented by the following equation:

$$
s(t) = A_c[1 + k_a m(t)]\cos(2\pi f_c t)
$$

where $s(t)$ is the modulated signal, $A_c$ is the amplitude of the carrier signal, $k_a$ is the amplitude modulation index, $m(t)$ is the modulation signal, and $f_c$ is the frequency of the carrier signal.

- The amplitude modulation index $k_a$ is a measure of the degree of modulation, and it ranges from 0 to 1. A higher value of $k_a$ means more modulation and more information transmitted, but also more distortion and noise susceptibility.
- The modulated signal can be decomposed into three components: the carrier signal, the upper sideband signal, and the lower sideband signal. The upper and lower sidebands are the result of the non-linear process of modulation, and they contain the same information as the modulation signal, but shifted in frequency by the carrier frequency.
- The frequency spectrum of the modulated signal can be shown by the following figure:

![AM spectrum](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Amplitude-modulation.png/800px-Amplitude-modulation.png)

where $f_c$ is the carrier frequency, $f_m$ is the modulation frequency, and $B$ is the bandwidth of the modulated signal, which is equal to twice the modulation frequency.

- Amplitude demodulation (AM) is the process of recovering the modulation signal from the modulated signal. There are different techniques for amplitude demodulation, such as envelope detection, synchronous detection, and product detection   .
- Envelope detection is the simplest and most common technique for amplitude demodulation. It consists of rectifying the modulated signal and then filtering out the high-frequency components using a low-pass filter. The output of the filter is the envelope of the modulated signal, which is proportional to the modulation signal.
- Synchronous detection is a more accurate and efficient technique for amplitude demodulation. It consists of multiplying the modulated signal by a local oscillator signal that has the same frequency and phase as the carrier signal. The output of the multiplier is then filtered by a low-pass filter to obtain the modulation signal.
- Product detection is a variation of synchronous detection that uses a local oscillator signal that has a slightly different frequency than the carrier signal. The output of the multiplier is then filtered by a band-pass filter to select one of the sidebands and obtain the modulation signal. This technique can be used to demodulate single-sideband signals, which are a form of amplitude modulation that suppresses the carrier and one of the sidebands to reduce the bandwidth and power consumption.