### 6. To study Operational Amplifier as Adder and Subtractor

- An operational amplifier (op-amp) is a high-gain, direct-coupled electronic circuit that can perform various linear operations such as amplification, filtering, differentiation, integration, etc.
- An op-amp has two input terminals: the inverting input (-) and the non-inverting input (+), and one output terminal. It also has two power supply terminals: the positive supply (V+) and the negative supply (V-).
- The output voltage of an op-amp is proportional to the difference between the input voltages, i.e., Vout = A(V+ - V-), where A is the open-loop gain of the op-amp.
- An op-amp can be used as an adder or a subtractor by connecting resistors to its input and output terminals. The resistors form a feedback network that controls the gain and the polarity of the output voltage.
- An op-amp adder is a circuit that produces an output voltage that is the weighted sum of the input voltages, i.e., Vout = Rf/R1 V1 + Rf/R2 V2 + ... + Rf/Rn Vn, where Rf is the feedback resistor and R1, R2, ..., Rn are the input resistors.
- An op-amp subtractor is a circuit that produces an output voltage that is the weighted difference of the input voltages, i.e., Vout = Rf/R1 (V1 - V2), where Rf is the feedback resistor and R1 and R2 are the input resistors.
- The following diagrams show the schematic of an op-amp adder and an op-amp subtractor:

```
    V1     V2     Vn
    |      |      |
    R1     R2     Rn
    |      |      |
    \      \      \
     \      \      \
      \      \      \
       \      \      \
        \      \      \
         \      \      \
          \      \      \
           \      \      \
            \      \      \
             \      \      \
              \      \      \
               \      \      \
                \      \      \
                 \      \      \
                  \      \      \
                   \      \      \
                    \      \      \
                     \      \      \
                      \      \      \
                       \      \      \
                        \      \      \
                         \      \      \
                          \      \      \
                           \      \      \
                            \      \      \
                             \      \      \
                              \      \      \
                               \      \      \
                                \      \      \
                                 \      \      \
                                  \      \      \
                                   \      \      \
                                    \      \      \
                                     \      \      \
                                      \      \      \
                                       \      \      \
                                        \      \      \
                                         \      \      \
                                          \      \      \
                                           \      \      \
                                            \      \      \
                                             \      \      \
                                              \      \      \
                                               \      \      \
                                                \      \      \
                                                 \      \      \
                                                  \      \      \
                                                   \      \      \
                                                    \      \      \
                                                     \      \      \
                                                      \      \      \
                                                       \      \      \
                                                        \      \      \
                                                         \      \      \
                                                          \      \      \
                                                           \      \      \
                                                            \      \      \
                                                             \      \      \
                                                              \      \      \
                                                               \      \      \
                                                                \      \      \
                                                                 \      \      \
                                                                  \      \      \
                                                                   \      \      \
                                                                    \      \      \
                                                                     \      \      \
                                                                      \      \      \
                                                                       \      \      \
                                                                        \      \      \
                                                                         \      \      \
                                                                          \      \      \
                                                                           \      \      \
                                                                            \      \      \
                                                                             \      \      \
                                                                              \      \      \
                                                                               \      \      \
                                                                                \      \      \
                                                                                 \      \      \
                                                                                  \      \      \
                                                                                   \      \      \
                                                                                    \      \      \
                                                                                     \      \      \
                                                                                      \      \      \
                                                                                       \      \      \
                                                                                        \      \      \
                                                                                         \      \      \
                                                                                          \      \      \
                                                                                           \      \      \
                                                                                            \      \      \
                                                                                             \      \      \
                                                                                              \      \      \
                                                                                               \      \      \
                                                                                                \      \      \
                                                                                                 \      \      \
                                                                                                  \      \      \