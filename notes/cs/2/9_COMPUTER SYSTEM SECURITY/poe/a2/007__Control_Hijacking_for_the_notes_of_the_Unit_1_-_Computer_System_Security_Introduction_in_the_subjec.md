 Here is the content written in formal tone with points and without emojis or external links in Markdown format:

### Control Hijacking

1. Control hijacking refers to the exploitation of a program's control flow to perform malicious actions.
2. This is achieved by corrupting program control data to redirect execution flow to injected malicious code.
3. Common vulnerabilities that enable control hijacking attacks include:
    - Buffer overflows: Overflowing input data corrupts the call stack, enabling the attacker to overwrite the return address.
    - Format string vulnerabilities: The attacker controls formatting parameters to inject arbitrary addresses and execute code.
    - Integer overflows: Integer values wrap around, corrupting control data.
4. Mitigations include:
    - Enforcing input validation and bounds checking.
    - Employing stack protections like canaries and NX bit.
    - Using safe programming languages and frameworks.
    - Auditing code for control hijacking vulnerabilities.

The above content is written in a formal tone with points and without any emojis or external links. The Markdown formatting is used and the content is written as study material to learn the topic of Control Hijacking for the notes of Unit 1 - Computer System Security Introduction. Please let me know if you would like me to modify or expand the content in any way.