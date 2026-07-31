#### b) Get input from two switches and switch on corresponding LEDs

- To get input from two switches and switch on corresponding LEDs, we need to use a microcontroller, such as Arduino, and connect it to two switches and two LEDs using wires and resistors.
- The switches are used to provide digital input signals to the microcontroller, which can be either HIGH (5V) or LOW (0V) depending on whether the switch is pressed or not.
- The LEDs are used to provide digital output signals from the microcontroller, which can be either HIGH (5V) or LOW (0V) depending on whether the LED is turned on or off.
- The microcontroller can read the input signals from the switches using digitalRead() function and write the output signals to the LEDs using digitalWrite() function.
- The logic of the program is to check the state of each switch and turn on the corresponding LED if the switch is pressed, or turn off the LED if the switch is not pressed.
- The circuit diagram and the code for this task are shown below:

```markdown
Circuit diagram:

    +5V
     |
     |
    [ ]  Switch 1
     |
     |----[10k]----GND
     |
     |----[ ]----Pin 2
     |
     |
    [ ]  Switch 2
     |
     |----[10k]----GND
     |
     |----[ ]----Pin 3
     |
     |
    [ ]  LED 1
     |
     |----[220]----GND
     |
     |----[ ]----Pin 4
     |
     |
    [ ]  LED 2
     |
     |----[220]----GND
     |
     |----[ ]----Pin 5
     |
     |
    GND

Code:

    // Define the pin numbers for the switches and LEDs
    #define SWITCH1 2
    #define SWITCH2 3
    #define LED1 4
    #define LED2 5

    // Declare the variables to store the switch states
    int switch1State = 0;
    int switch2State = 0;

    void setup() {
      // Set the switch pins as inputs with pull-up resistors
      pinMode(SWITCH1, INPUT_PULLUP);
      pinMode(SWITCH2, INPUT_PULLUP);
      // Set the LED pins as outputs
      pinMode(LED1, OUTPUT);
      pinMode(LED2, OUTPUT);
    }

    void loop() {
      // Read the switch states
      switch1State = digitalRead(SWITCH1);
      switch2State = digitalRead(SWITCH2);
      // Turn on the corresponding LED if the switch is pressed, or turn off the LED if the switch is not pressed
      if (switch1State == LOW) {
        digitalWrite(LED1, HIGH);
      } else {
        digitalWrite(LED1, LOW);
      }
      if (switch2State == LOW) {
        digitalWrite(LED2, HIGH);
      } else {
        digitalWrite(LED2, LOW);
      }
    }
```