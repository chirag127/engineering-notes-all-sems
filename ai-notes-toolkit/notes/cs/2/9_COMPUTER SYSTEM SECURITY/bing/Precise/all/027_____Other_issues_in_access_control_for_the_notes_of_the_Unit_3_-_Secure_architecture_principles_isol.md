# Other issues in access control

1. **Covert channels**: A covert channel is a communication channel that allows two cooperating processes to transfer information in a way that violates the system's security policy. Covert channels can be used to bypass access controls and can be difficult to detect and prevent.

2. **Confused deputy problem**: The confused deputy problem occurs when a program is tricked into misusing its authority. This can happen when a program is given a capability that it should not have, or when it is given a capability with the wrong parameters.

3. **Time-of-check to time-of-use (TOCTTOU) attacks**: TOCTTOU attacks exploit the time window between when a system checks a condition and when it uses the result of that check. An attacker can change the condition during this window, causing the system to take an unintended action.

4. **Race conditions**: A race condition occurs when the behavior of a system depends on the timing of events, and the events do not always occur in the same order. Race conditions can be exploited to bypass access controls or to cause other security problems.

5. **Object reuse**: Object reuse refers to the reuse of storage media, such as disks or memory, that previously contained sensitive information. If the storage media is not properly sanitized before reuse, the sensitive information may be accessible to unauthorized users.

6. **Polyinstantiation**: Polyinstantiation is the creation of multiple instances of the same object with different security levels. This can be used to prevent unauthorized users from inferring the existence of information that they are not authorized to access.

7. **Incomplete mediation**: Incomplete mediation occurs when a system does not check all of the relevant security conditions before granting access to a resource. This can allow unauthorized users to access the resource.
