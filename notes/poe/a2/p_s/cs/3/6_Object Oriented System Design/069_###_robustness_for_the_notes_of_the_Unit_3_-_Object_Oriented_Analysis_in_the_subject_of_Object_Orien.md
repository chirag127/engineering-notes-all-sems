 Here is the content in markdown format for the topic ### Robustness for the notes of Unit 3 - Object Oriented Analysis in the subject of Object Oriented System Design:

### Robustness

- Robustness refers to the ability of a system to handle errors, exceptions, and invalid inputs gracefully instead of crashing or behaving erratically.
- A robust system is fault-tolerant and able to cope with unexpected conditions or inputs.
- Some ways to achieve robustness in software are:
    - Exception handling: Handle errors and exceptions appropriately instead of the system crashing. Proper error handling and messaging can make the system robust.
    - Input validation: Validate all inputs and handle invalid inputs gracefully instead of the system crashing. Validate type, format, range, etc. of inputs.
    - Fail-safe defaults: Have sensible default behavior in case of errors or invalid inputs. This avoids unpredictable behavior or system crash.
    - Retry and recovery logic: For transient errors, have retry logic and recovery mechanisms to handle intermittent faults. This increases robustness.
    - Graceful degradation: If certain components fail or are unavailable, have the system degrade gracefully instead of failing completely. Priority can be assigned to core functions in case of degraded mode.
- Advantages of a robust system:
    - Increased reliability and dependability.
    - Avoidance of unpredictable or erratic behavior in case of errors or faults.
    - Increased user experience due to graceful handling of errors and faults.
- Disadvantages of a robust system:
    - Additional complexity in programming as exception handling and input validation logic needs to be incorporated.
    - May impact performance slightly due to additional validation and error handling steps.
- Examples of robust systems: Databases with ACID properties, aircraft control systems, etc.
- Applications of robust systems: Safety-critical systems, mission-critical systems, etc. where unpredictable behavior cannot be afforded.