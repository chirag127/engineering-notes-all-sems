### Cross Site Request Forgery (CSRF)

- CSRF is a type of attack that forces a user to perform unwanted actions on a web application where they are already authenticated .
- CSRF exploits the trust that the web application has in the user's identity and session.
- CSRF can be used to perform malicious actions such as changing passwords, transferring funds, deleting accounts, etc. without the user's consent or knowledge .
- CSRF can be prevented by using anti-CSRF tokens, validating the origin and referer headers, checking the HTTP method, and requiring user confirmation for sensitive actions.
- CSRF is an example of a confused deputy attack, where the web browser is tricked into submitting a forged request by a less privileged attacker.