### Cross site request forgery

- Cross site request forgery (CSRF) is a type of web attack that exploits the trust between a web application and a user's browser .
- In a CSRF attack, an attacker tricks a user into performing an action on a web application that the user is already logged into, such as transferring money, changing password, or deleting an account .
- The attacker does not need to know the user's credentials or session details, but only needs to craft a malicious link or form that sends a forged request to the web application .
- The web application cannot distinguish between a legitimate request and a forged request, and executes the action as if it was initiated by the user .
- CSRF attacks can cause serious damage to the user and the web application, such as financial loss, identity theft, or data breach .

### Secure architecture principles: isolation and least privilege

- Isolation and least privilege are two important principles for designing secure architectures for web applications.
- Isolation means separating different components or layers of the web application, such as the presentation, business logic, and data access layers, so that they can only communicate through well-defined interfaces.
- Isolation reduces the attack surface and the impact of a compromise, as an attacker who gains access to one component cannot easily access other components.
- Least privilege means granting the minimum amount of permissions or access rights to each component or user of the web application, such as the web server, the database, or the administrator.
- Least privilege limits the damage and the potential for abuse, as an attacker who exploits a vulnerability or steals a credential cannot perform actions beyond the scope of the assigned privilege.