 Here are the notes on Cross Site Scripting (XSS) for Unit 3 - Secure architecture principles isolation and least privilege in the subject of Computer System Security:

### Cross Site Scripting (XSS)

- XSS is a type of injection attack where malicious scripts are injected into otherwise benign and trusted web sites.
- The injected scripts are then executed by the browser when a user visits the compromised web site.
- The malicious scripts can steal cookies, login credentials, or other sensitive data, or redirect the user to malicious sites.
- XSS attacks generally target web sites that accept input from users, and fail to properly validate and sanitize the input.
- There are three main types of XSS attacks:

1. Reflected XSS - Inputs are sent to the server in a request, and the malicious script is reflected in the response and executed by the browser.
2. Stored XSS - Malicious inputs are stored on the server, and the malicious script is sent to users when the data is displayed.
3. DOM-based XSS - Malicious scripts are executed client-side by manipulating the DOM environment.

- To prevent XSS attacks:

- Sanitize and validate all user input on the server side.
- Encode output using appropriate contexts to avoid interpretation of characters with special meaning.
- Ensure that DOM data is sanitized/escaped before use.
- Keep server-side and client-side scripts separate and do not pass unencoded user data to scripts.
- Update server software and web frameworks regularly to patch vulnerabilities.

- The notes are written in Markdown format with headings and points as requested. No emojis or external links have been included and a formal tone has been maintained. Please let me know if you would like me to modify or expand the notes.