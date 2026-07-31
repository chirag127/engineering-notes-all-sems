### Cross site request forgery

- Cross site request forgery (CSRF) is a type of web attack that exploits the trust between a web application and a user's browser .
- CSRF forces the user to perform unwanted actions on a web application where they are already authenticated, such as transferring money, changing passwords, or deleting accounts.
- CSRF works by tricking the user into clicking a malicious link or submitting a forged form that contains a request to the web application .
- The web application cannot distinguish between a legitimate request and a forged one, and executes the request as if it came from the user .
- CSRF can be prevented by using anti-CSRF tokens, validating the origin and referer headers, or requiring user confirmation for sensitive actions.