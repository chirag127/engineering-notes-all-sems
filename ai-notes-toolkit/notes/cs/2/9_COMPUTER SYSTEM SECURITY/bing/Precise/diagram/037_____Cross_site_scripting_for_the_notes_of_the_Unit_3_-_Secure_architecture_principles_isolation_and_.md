### Cross Site Scripting

Cross Site Scripting (XSS) is a type of vulnerability that exists in web applications. It allows attackers to inject malicious scripts into web pages viewed by other users. This can result in a range of attacks, such as stealing user data, defacing websites, and redirecting users to malicious sites.

There are three main types of XSS attacks:

1. **Stored XSS**: This type of attack occurs when the malicious script is permanently stored on the server, such as in a database or a comment field. When the user views the affected page, the script is executed.

2. **Reflected XSS**: This type of attack occurs when the malicious script is reflected back to the user through a search result or error message. The script is not permanently stored on the server.

3. **DOM-based XSS**: This type of attack occurs when the malicious script is executed as a result of modifying the Document Object Model (DOM) of the page in the user's browser.

To prevent XSS attacks, it is important to follow secure coding practices, such as validating and sanitizing user input, encoding output, and using security-focused browser extensions. Additionally, implementing a Content Security Policy (CSP) can help mitigate the risk of XSS attacks.