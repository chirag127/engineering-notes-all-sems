### Cross site scripting

- Cross site scripting (XSS) is a type of security vulnerability that can be found in some web applications   .
- XSS attacks enable attackers to inject client-side scripts, typically JavaScript, into web pages viewed by other users  .
- A cross site scripting vulnerability may be used by attackers to bypass access controls such as the same-origin policy, steal sensitive information, impersonate users, perform actions on their behalf, or deliver malware   .
- There are three main types of XSS attacks: reflected, stored, and DOM-based .
  - Reflected XSS occurs when the attacker sends a malicious link to the victim, and the web application echoes the user input in the response without proper validation or encoding .
  - Stored XSS occurs when the attacker submits a malicious script to the web application, and the web application stores it in a database or other persistent storage, and later displays it to the victim or other users .
  - DOM-based XSS occurs when the attacker manipulates the Document Object Model (DOM) of the web page using client-side code, and the web application does not sanitize the user input before writing it to the DOM .
- To prevent XSS attacks, web applications should validate and encode user input, use secure HTTP headers, implement Content Security Policy (CSP), and use frameworks and libraries that offer built-in protection against XSS  .