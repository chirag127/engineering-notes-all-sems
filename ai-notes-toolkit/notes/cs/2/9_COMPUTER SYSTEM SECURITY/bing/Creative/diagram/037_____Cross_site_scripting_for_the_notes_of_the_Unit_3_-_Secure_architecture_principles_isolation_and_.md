Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is some information on cross site scripting for the notes of the Unit 3 - Secure architecture principles isolation and leas in the subject of COMPUTER SYSTEM SECURITY.

### Cross site scripting

- Cross site scripting (XSS) is a type of security vulnerability that can be found in some web applications   .
- XSS attacks enable attackers to inject client-side scripts into web pages viewed by other users  .
- A cross site scripting vulnerability may be used by attackers to bypass access controls such as the same-origin policy .
- XSS attacks can compromise the confidentiality, integrity, and availability of the web application and its users.
- There are three main types of XSS attacks: reflected, stored, and DOM-based.
  - Reflected XSS occurs when the attacker sends a malicious link to the victim, and the web application reflects the injected script back to the victim's browser.
  - Stored XSS occurs when the attacker stores the malicious script in a persistent data source, such as a database or a comment field, and the web application displays the script to the victim's browser.
  - DOM-based XSS occurs when the attacker manipulates the Document Object Model (DOM) of the web page, and the web application executes the script in the victim's browser.
- XSS attacks can have various impacts, such as stealing cookies, session tokens, or other sensitive information, redirecting the victim to malicious websites, performing actions on behalf of the victim, or installing malware on the victim's device.
- XSS attacks can be prevented by applying secure coding practices, such as validating and sanitizing user input, encoding and escaping output, using Content Security Policy (CSP), and implementing HTTP-only and secure cookies.