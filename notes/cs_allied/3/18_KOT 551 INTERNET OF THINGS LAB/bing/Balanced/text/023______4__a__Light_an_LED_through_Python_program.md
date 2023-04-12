#### 4. a) Light an LED through Python program

- To light an LED through Python program, you need the following components:
  - A Raspberry Pi board with GPIO pins
  - An LED
  - A resistor (220 ohms or similar)
  - Jumper wires
  - A breadboard
- The steps to light an LED through Python program are as follows:
  - Connect the LED to the breadboard. The longer leg (anode) of the LED should be connected to one end of the resistor, and the shorter leg (cathode) should be connected to a free row on the breadboard.
  - Connect the other end of the resistor to a GPIO pin on the Raspberry Pi board. For example, you can use GPIO 18 (pin 12) as the output pin.
  - Connect the free row on the breadboard where the LED cathode is connected to the ground (GND) pin on the Raspberry Pi board. For example, you can use pin 6 as the ground pin.
  - The circuit diagram for the LED connection is shown below:

  ```
  +3.3V  (1) (2)  +5V
        (3) (4)  +5V
        (5) (6)  GND
        (7) (8)  GPIO 14 (TXD)
   GND  (9) (10) GPIO 15 (RXD)
  GPIO 17 (11) (12) GPIO 18
  GPIO 27 (13) (14) GND
  GPIO 22 (15) (16) GPIO 23
  +3.3V (17) (18) GPIO 24
  GPIO 10 (19) (20) GND
   GPIO 9 (21) (22) GPIO 25
  GPIO 11 (23) (24) GPIO 8
   GND  (25) (26) GPIO 7
  GPIO  0 (27) (28) GPIO 1
  GPIO  5 (29) (30) GND
  GPIO  6 (31) (32) GPIO 12
  GPIO 13 (33) (34) GND
  GPIO 19 (35) (36) GPIO 16
  GPIO 26 (37) (38) GPIO 20
   GND  (39) (40) GPIO 21

  +-----+-----+---------+------+---+---Pi 3---+---+------+---------+-----+-----+
  | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
  +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
  |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
  |   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5v      |     |     |
  |   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
  |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 1 | ALT0 | TxD     | 15  | 14  |
  |     |     |      0v |      |   |  9 || 10 | 1 | ALT0 | RxD     | 16  | 15  |
  |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | OUT  | GPIO. 1 | 1   | 18  |
  |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
  |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 0 | IN   | GPIO. 4 | 4   | 23  |
  |     |     |    3.3v |      |   | 17 || 18 | 0 | IN   | GPIO. 5 | 5   | 24  |

```
