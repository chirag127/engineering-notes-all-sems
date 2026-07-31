### Cross Site Scripting

Cross-Site Scripting (XSS) is a type of vulnerability that exists in web applications. It allows attackers to inject malicious scripts into web pages viewed by other users. This can result in a variety of attacks, such as stealing user data, defacing websites, or redirecting users to malicious sites.

There are three main types of XSS vulnerabilities:

1. **Stored XSS:** This type of vulnerability occurs when an attacker is able to store a malicious script on a web server, which is then served to all users who view the affected page. This can happen, for example, when a web application allows users to submit content that is not properly sanitized before being stored on the server.

2. **Reflected XSS:** This type of vulnerability occurs when an attacker is able to inject a malicious script into a web page by manipulating the URL or other input to the web application. The script is then reflected back to the user and executed by their browser.

3. **DOM-based XSS:** This type of vulnerability occurs when an attacker is able to manipulate the Document Object Model (DOM) of a web page in a way that allows them to inject a malicious script. This can happen, for example, when a web application uses client-side scripts to dynamically update the content of a page.

To prevent XSS vulnerabilities, it is important to properly sanitize all user input and to use secure coding practices when developing web applications. Additionally, using security features such as Content Security Policy (CSP) can help to mitigate the risk of XSS attacks.