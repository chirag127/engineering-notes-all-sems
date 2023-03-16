#### c) Flash an LED at a given on time and off time cycle, where the two times are taken from a file.

- To flash an LED at a given on time and off time cycle, we need to use a microcontroller, an LED, a resistor, a breadboard, some jumper wires, and a text file that contains the on time and off time values in milliseconds.
- The microcontroller is a device that can execute a program that controls the output pins. We can use any microcontroller that has a digital output pin, such as Arduino, Raspberry Pi, or ESP32.
- The LED is a light-emitting diode that can turn on or off depending on the voltage applied to its terminals. We need to connect one terminal of the LED to the output pin of the microcontroller, and the other terminal to the ground through a resistor. The resistor limits the current that flows through the LED and protects it from burning out.
- The breadboard is a board that has rows and columns of holes that are electrically connected. We can use it to make connections between the components without soldering. We need to insert the LED, the resistor, and the jumper wires into the breadboard according to the circuit diagram below.

![Circuit diagram](https://i.imgur.com/9Qx0Q8F.png)

- The text file is a file that contains the on time and off time values in milliseconds, separated by a comma. For example, the file could look like this:

```
500,1000
200,300
1000,500
```

- This means that the LED should turn on for 500 milliseconds, then turn off for 1000 milliseconds, then turn on for 200 milliseconds, then turn off for 300 milliseconds, and so on. The file should be saved in the same folder as the program that we will write for the microcontroller.
- The program is a set of instructions that tells the microcontroller what to do. We can use any programming language that is compatible with the microcontroller, such as C, Python, or Arduino. The program should do the following steps:

  - Initialize the output pin as an output and set it to low (off).
  - Open the text file and read the first line.
  - Split the line by the comma and convert the values to integers.
  - Set a variable called state to high (on).
  - Start a loop that repeats indefinitely.
    - Write the state to the output pin. This will turn the LED on or off depending on the state.
    - If the state is high, delay for the on time value. If the state is low, delay for the off time value. This will create the on-off cycle.
    - Toggle the state. This will switch the state from high to low or vice versa.
    - Read the next line from the file. If the end of the file is reached, go back to the first line. This will create a loop of the on-off cycles.

- The pseudocode for the program is shown below:

```
output_pin = 2 # change this to the pin number of your microcontroller
pinMode(output_pin, OUTPUT) # set the output pin as an output
digitalWrite(output_pin, LOW) # set the output pin to low (off)

file = open("times.txt", "r") # open the text file in read mode
line = file.readline() # read the first line from the file
on_time, off_time = line.split(",") # split the line by the comma
on_time = int(on_time) # convert the on time to an integer
off_time = int(off_time) # convert the off time to an integer

state = HIGH # set the state to high (on)

while True: # start an infinite loop
  digitalWrite(output_pin, state) # write the state to the output pin
  if state == HIGH: # if the state is high
    delay(on_time) # delay for the on time
  else: # if the state is low
    delay(off_time) # delay for the off time
  state = not state # toggle the state
  line = file.readline() # read the next line from the file
  if line == "": # if the end of the file is reached
    file.seek(0) # go back to the beginning of the file
    line = file.readline() # read the first line again
  on_time, off_time = line.split(",") # split the line by the comma
  on_time = int(on_time) # convert the on time to an integer
  off_time = int(off_time) # convert the off time to an integer
```

- The program can be modified to