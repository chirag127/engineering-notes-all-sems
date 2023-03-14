Transmission impairments are the factors that degrade the quality of a signal during its transmission from the sender to the receiver. There are three main types of transmission impairments: noise, distortion, and attenuation.

Noise is the unwanted signal that gets added to the transmitted signal and causes errors in the received signal. There are different sources of noise, such as thermal noise, shot noise, impulse noise, crosstalk, and intermodulation noise.

Distortion is the change in the shape or amplitude of the signal due to the delay or frequency-dependent attenuation of different frequency components of the signal. Distortion can affect both analog and digital signals, but it is more severe for composite signals that have multiple frequency components.

Attenuation is the decrease in signal strength or power as the signal travels through the transmission medium. Attenuation can be caused by the resistance, capacitance, and inductance of the medium, as well as by the absorption, scattering, and reflection of the signal by the environment.

The following diagram illustrates the basic architecture of a network and the effects of transmission impairments on the signal:

```
+--------+    +--------+    +--------+    +--------+
| Sender |----| Switch |----| Switch |----|Receiver|
+--------+    +--------+    +--------+    +--------+
  |           /  |   \         |   \         |
  |          /   |    \        |    \        |
  |         /    |     \       |     \       |
  |        /     |      \      |      \      |
  |       /      |       \     |       \     |
  |      /       |        \    |        \    |
  |     /        |         \   |         \   |
  |    /         |          \  |          \  |
  |   /          |           \ |           \ |
  |  /           |            \|            \|
  | /            |             |             |
  |/             |             |             |
+--------+    +--------+    +--------+    +--------+
| Sender |----| Switch |----| Switch |----|Receiver|
+--------+    +--------+    +--------+    +--------+

  |<------------------------ Signal Path ------------------------>|

  |<-- Attenuation -->|<-- Noise -->|<-- Distortion -->|<-- Noise -->|
```

The diagram shows two senders and two receivers connected by two switches. The signal path is the route that the signal takes from the sender to the receiver. Along the signal path, the signal may encounter different types of transmission impairments, such as attenuation, noise, and distortion. The impairments may affect the signal differently depending on the distance, frequency, and medium of the transmission. The impairments may also accumulate and worsen as the signal passes through multiple switches and links. The result is that the signal received at the receiver may be different from the signal sent by the sender, and may contain errors or distortions that affect the network performance and reliability.