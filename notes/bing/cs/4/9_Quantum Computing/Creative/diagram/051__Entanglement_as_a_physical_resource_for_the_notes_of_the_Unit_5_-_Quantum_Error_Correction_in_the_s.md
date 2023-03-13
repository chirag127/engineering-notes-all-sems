Entanglement is a quantum phenomenon that allows two or more particles to share quantum states, even when they are spatially separated. Entanglement can be used as a physical resource for quantum error correction, which is a technique to protect quantum information from noise and decoherence.

One way to use entanglement for quantum error correction is to employ entanglement-assisted quantum error-correcting codes (EAQECCs) . These codes make use of preexisting entanglement between the sender and receiver to boost the rate of transmission. It is possible to construct an EAQECC from any classical linear code, unlike standard QECCs, which can only be constructed from dual-containing codes.

The following diagram illustrates the basic architecture of an EAQECC:

```
Sender                          Receiver
+------------------+            +------------------+
|                  |            |                  |
| Classical linear |            | Classical linear |
| code encoder     |            | code decoder     |
|                  |            |                  |
+--------+---------+            +---------+--------+
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
+--------+---------+            +---------+--------+
|                  |            |                  |
| Quantum channel  |            | Quantum channel  |
| encoder          |            | decoder          |
|                  |            |                  |
+--------+---------+            +---------+--------+
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
+--------+---------+            +---------+--------+
|                  |            |                  |
| Quantum channel  |            | Quantum channel  |
|                  |            |                  |
+--------+---------+            +---------+--------+
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
         |                              |
+--------+---------+            +---------+--------+
|                  |            |                  |
| Preexisting      |            | Preexisting      |
| entanglement     |            | entanglement     |
|                  |            |                  |
+------------------+            +------------------+
```

The sender encodes the classical information using a classical linear code, then encodes the resulting quantum state using a quantum channel encoder. The encoded state is sent through a noisy quantum channel to the receiver, who decodes it using a quantum channel decoder and a classical linear code decoder. The preexisting entanglement between the sender and receiver helps to correct the errors introduced by the quantum channel. 

: General entanglement-assisted quantum error-correcting codes, Phys. Rev. A 76, 062313 (2007)