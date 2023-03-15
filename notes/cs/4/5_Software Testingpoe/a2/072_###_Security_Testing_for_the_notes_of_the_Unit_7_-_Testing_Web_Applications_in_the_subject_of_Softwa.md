 Here is the content in markdown format for the given topic:

### Security Testing for the notes of the Unit 7 - Testing Web Applications in the subject of Software Testing

Following are the key points to cover under Security Testing for Web Applications:

1. SQL Injection:
- It is a web security vulnerability that allows an attacker to influence the queries that an application makes to its database.
- Mnemonic: Little Bobby Tables - to remember that improper use of user input in SQL queries can lead to SQL Injection vulnerability.
- How to test: Include ' or 1=1;-- in the input fields to check if the application is vulnerable to SQL Injection.
- How to prevent: Use prepared statements or parameterized queries and sanitize the user input.

2. Cross-Site Scripting (XSS):
- It is a type of injection attack where malicious scripts are injected into otherwise benign and trusted web sites.
- How to test: Include <script>alert('xss')</script> in the input fields to check if the application is vulnerable to XSS.
- How to prevent: Sanitize the user input and escape untrusted HTTP parameters and attributes.

3. Broken Access Control:
- It is a vulnerability where access restrictions on the server are not properly enforced.
- How to test: Try accessing other user's data or perform functions which you are not authorized to do to check for broken access control.
- How to prevent: Implement access control mechanisms and verify the user privileges before allowing any access.

[Similar detailed points can be included for other security vulnerabilities like CSRF, insecure direct object references, etc. with examples and prevention methods.]

Advantages of security testing:
- Identifies vulnerabilities in the application which can be fixed early.
- Prevents data breaches and leakage of sensitive information.
- Builds secure software and maintains customer trust.

Disadvantages of security testing:
- Requires highly skilled testers with knowledge of penetration testing and security domains.
- Difficult to automate security testing.
- Discovering and exploiting vulnerabilities can be time-consuming.

[Include diagrams or codes if required to explain any of the points]