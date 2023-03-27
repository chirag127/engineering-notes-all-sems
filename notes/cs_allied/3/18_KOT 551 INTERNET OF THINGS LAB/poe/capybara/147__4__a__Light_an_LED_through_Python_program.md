#### 4. a) Light an LED through Python program

To light an LED through a Python program, follow the below steps:

1. Import the necessary libraries: 
    ```
    import RPi.GPIO as GPIO
    import time
    ```

2. Set the mode and pin number: 
   ```
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin_number, GPIO.OUT)
   ```
   
   Note: Replace `pin_number` with the actual pin number connected to the LED.
   
3. Turn on the LED: 
    ```
    GPIO.output(pin_number, GPIO.HIGH)
    ```
    
4. Wait for a few seconds:
    ```
    time.sleep(5)
    ```
    
5. Turn off the LED: 
    ```
    GPIO.output(pin_number, GPIO.LOW)
    ```

6. Clean up the GPIO pins:
    ```
    GPIO.cleanup()
    ```
    
   Note: This step is necessary to release the resources used by the GPIO pins.
   
By following these steps, you can light an LED through a Python program. However, make sure to double-check the pin number and connections before running the program to avoid any hardware damage.