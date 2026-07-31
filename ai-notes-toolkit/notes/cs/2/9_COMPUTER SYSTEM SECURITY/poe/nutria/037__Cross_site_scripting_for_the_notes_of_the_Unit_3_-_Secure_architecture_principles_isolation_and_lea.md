
### Cross Site Scripting

Cross Site Scripting (XSS) is a type of attack that allows an attacker to inject malicious code into a web page. This code can be used to steal data, hijack user sessions, or redirect users to malicious sites.

XSS attacks can be divided into two categories:

1. **Stored XSS**: Stored XSS attacks occur when malicious code is stored in a database or other persistent storage. When a user visits the page, the malicious code is executed.

2. **Reflected XSS**: Reflected XSS attacks occur when malicious code is sent to a web server, which then reflects the code back to the user's browser.

To prevent XSS attacks, web developers should:

1. Validate user input to ensure that it is valid and does not contain malicious code.
2. Escape HTML characters in user input to prevent malicious code from being executed.
3. Use a Content Security Policy (CSP) to restrict which domains can access the website.
4. Use a web application firewall (WAF) to detect and block malicious requests.
5. Implement a secure architecture, such as the principles of isolation and least privilege.