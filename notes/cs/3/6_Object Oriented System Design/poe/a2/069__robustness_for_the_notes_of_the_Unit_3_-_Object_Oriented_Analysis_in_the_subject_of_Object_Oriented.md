 Here are the notes on Robustness for Unit 3 - Object Oriented Analysis in Object Oriented System Design:

### Robustness

1. Robustness refers to the ability of a system to handle errors, abnormalities, or unexpected inputs gracefully and continue operating.
2. A robust system should not crash or produce incorrect outputs when provided with invalid inputs or in the presence of hardware/software faults. It should have mechanisms to handle exceptions and continue operating.
3. Some techniques to achieve robustness:
 - Error handling - Check for errors and handle them appropriately instead of crashing. Use try/catch blocks, exceptions, etc.
 - Defensive programming - Validate inputs and assume things can go wrong. Check for null values, invalid states, etc. and handle them.
 - Graceful degradation - If certain components fail, the system should degrade gracefully by providing reduced functionality instead of failing completely.
 - Fault tolerance - Employ strategies like redundancy to avoid single points of failure and continue operating even in the presence of faults.
 - Loose coupling - Minimize dependencies between components so that a fault in one component does not affect others and the system can continue operating.

4. Robust systems lead to higher availability, reliability and fault tolerance which are important qualities for real-world software and systems. Being robust prepares a system to handle unforeseen circumstances and continue functioning.

The above notes cover the key points about robustness and techniques to achieve it in object oriented systems. The points are written in a formal tone with markdown formatting and no emojis as specified. Let me know if you would like me to elaborate on any of the points or modify the notes.