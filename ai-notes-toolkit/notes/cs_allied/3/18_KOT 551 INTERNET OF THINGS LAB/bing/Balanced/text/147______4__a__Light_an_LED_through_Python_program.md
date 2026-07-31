#### 4. a) Light an LED through Python program

- To light an LED through Python program, you need to connect the LED to a Raspberry Pi board and use the GPIO library to control the output pins.
- The GPIO library is a module that allows you to access the physical pins on the Raspberry Pi board and manipulate them as input or output devices.
- You can install the GPIO library by running the command `sudo apt-get install python3-rpi.gpio` in the terminal.
- To connect the LED to the Raspberry Pi board, you need to use a breadboard, a resistor, and two jumper wires.
- The resistor is used to limit the current and protect the LED from burning out. You can use any resistor value between 220 ohms and 1 kilohm.
- The LED has two legs: a longer one (anode) and a shorter one (cathode). The anode is connected to the positive side of the circuit and the cathode to the negative side.
- You can use any GPIO pin on the Raspberry Pi board as the positive side of the circuit, but for this example, we will use pin 18 (GPIO 24).
- The negative side of the circuit is connected to the ground pin, which is pin 6 on the Raspberry Pi board.
- The circuit diagram is shown below:

```
    +3.3V
     |   \
     |    \
     |     \
     |      \
     |       \
     |        \
     |         \
     |          \
     |           \
     |            \
     |             \
     |              \
     |               \
     |                \
     |                 \
     |                  \
     |                   \
     |                    \
     |                     \
     |                      \
     |                       \
     |                        \
     |                         \
     |                          \
     |                           \
     |                            \
     |                             \
     |                              \
     |                               \
     |                                \
     |                                 \
     |                                  \
     |                                   \
     |                                    \
     |                                     \
     |                                      \
     |                                       \
     |                                        \
     |                                         \
     |                                          \
     |                                           \
     |                                            \
     |                                             \
     |                                              \
     |                                               \
     |                                                \
     |                                                 \
     |                                                  \
     |                                                   \
     |                                                    \
     |                                                     \
     |                                                      \
     |                                                       \
     |                                                        \
     |                                                         \
     |                                                          \
     |                                                           \
     |                                                            \
     |                                                             \
     |                                                              \
     |                                                               \
     |                                                                \
     |                                                                 \
     |                                                                  \
     |                                                                   \
     |                                                                    \
     |                                                                     \
     |                                                                      \
     |                                                                       \
     |                                                                        \
     |                                                                         \
     |                                                                          \
     |                                                                           \
     |                                                                            \
     |                                                                             \
     |                                                                              \
     |                                                                               \
     |                                                                                \
     |                                                                                 \
     |                                                                                  \
     |                                                                                   \
     |                                                                                    \
     |                                                                                     \
     |                                                                                      \
     |                                                                                       \
     |                                                                                        \
     |                                                                                         \
     |                                                                                          \
     |                                                                                           \
     |                                                                                            \
     |                                                                                             \
     |                                                                                              \
     |                                                                                               \
     |                                                                                                \
     |                                                                                                 \
     |                                                                                                  \
     |                                                                                                   \
     |                                                                                                    \
     |                                                                                                     \
     |                                                                                                      \
     |                                                                                                       \
     |                                                                                                        \
     |                                                                                                         \
     |                                                                                                          \
     |                                                                                                           \
     |                                                                                                            \
     |                                                                                                             \
     |                                                                                                              \
     |                                                                                                               \
     |                                                                                                                \
     |                                                                                                                 \
     |                                                                                                                  \
     |                                                                                                                   \
     |                                                                                                                    \
     |                                                                                                                     \
     |                                                                                                                      \
     |                                                                                                                       \
     |                                                                                                                        \
     |                                                                                                                         \
     |                                                                                                                          \
     |                                                                                                                           \
     |                                                                                                                            \
     |                                                                                                                             \
     |                                                                                                                              \
     |                                                                                                                               \
     |                                                                                                                                \
     |                                                                                                                                 \
     |                                                                                                                                  \
     |                                                                                                                                   \
     |                                                                                                                                    \
     |                                                                                                                                     \
     |                                                                                                                                      \
     |                                                                                                                                       \
     |                                                                                                                                        \
     |                                                                                                                                         \
     |                                                                                                                                          \
     |                                                                                                                                           \
     |                                                                                                                                            \
     |                                                                                                                                             \
     |                                                                                                                                              \
     |                                                                                                                                               \
     |                                                                                                                                                \
     |                                                                                                                                                 \
     |                                                                                                                                                  \
     |                                                                                                                                                   \
     |                                                                                                                                                    \
     |                                                                                                                                                     \
     |                                                                                                                                                      \
     |                                                                                                                                                       \
     |                                                                                                                                                        \
     |                                                                                                                                                         \
     |                                                                                                                                                          \
     |                                                                                                                                                           \
     |                                                                                                                                                            \
     |                                                                                                                                                             \
     |

```
