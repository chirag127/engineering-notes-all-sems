 Here are the notes on More Control Hijacking attacks format string vulnerabilities for the Unit 1 - Computer System Security Introduction:

### More Control Hijacking attacks format string vulnerabilities

- Format string vulnerabilities occur when user-controlled input is used to format a string printf-style function.
- Attackers can exploit these vulnerabilities to read arbitrary memory and hijack program control flow.
- To exploit a format string vulnerability, an attacker inputs a format string instead of expected input data. The format string contains % formatting directives that affect the behavior of the printf-style function.
- Some ways to exploit format string vulnerabilities:

1. Reading arbitrary memory: Use %x or %s directives with indexes/addresses to leak memory contents.
2. Gaining control of instruction pointer: Use %n directive to write arbitrary values, allowing control to be transferred to attacker-controlled memory.
3. Calling arbitrary functions: On some systems, use %<number>$<directive> to call functions with attacker-controlled arguments.

- Defenses:

1. Avoid using user-controlled input in printf-style functions.
2. If required, validate and sanitize user input to ensure it only contains expected data.
3. Compile with -Wformat -Werror to enable warnings about format string use.
4. Recompile vulnerable programs with enhanced format string protection likeFORTIFY_SOURCE.

- Always be careful when using formatted string functions with user-controlled input to avoid format string vulnerabilities.