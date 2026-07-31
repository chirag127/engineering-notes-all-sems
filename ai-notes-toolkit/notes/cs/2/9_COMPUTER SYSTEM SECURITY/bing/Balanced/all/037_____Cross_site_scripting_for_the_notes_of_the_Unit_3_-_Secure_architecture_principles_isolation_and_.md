# Cross-site scripting

- Cross-site scripting (XSS) is a type of security vulnerability that can be found in some web applications   .
- XSS attacks enable attackers to inject client-side scripts, typically JavaScript, into web pages viewed by other users  .
- A cross-site scripting vulnerability may be used by attackers to bypass access controls such as the same-origin policy, steal sensitive information, impersonate users, deface websites, or execute malicious commands on the user's browser   .
- There are three main types of XSS attacks: reflected, stored, and DOM-based .
  - Reflected XSS occurs when the attacker sends a malicious link to the victim, and the web application echoes the user input in the response without proper validation or encoding .
  - Stored XSS occurs when the attacker stores the malicious script on the web application, such as in a comment, a forum post, or a database, and the web application displays the script to the victim without proper validation or encoding .
  - DOM-based XSS occurs when the attacker modifies the DOM (Document Object Model) of the web page using a client-side script, and the web application executes the script without proper validation or encoding .
- To prevent XSS attacks, web applications should implement input validation, output encoding, content security policy, and other security measures  .