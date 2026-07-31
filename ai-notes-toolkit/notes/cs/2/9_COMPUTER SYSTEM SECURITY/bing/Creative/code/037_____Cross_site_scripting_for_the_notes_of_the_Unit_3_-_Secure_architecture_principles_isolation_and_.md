### Cross site scripting

- Cross site scripting (XSS) is a type of security vulnerability that can be found in some web applications  .
- XSS attacks enable attackers to inject client-side scripts into web pages viewed by other users  .
- A cross site scripting vulnerability may be used by attackers to bypass access controls such as the same-origin policy .
- The malicious scripts can perform various actions, such as stealing cookies, session tokens, or other sensitive information, redirecting the user to malicious websites, displaying fake or misleading content, or executing arbitrary code on the user's browser.
- There are three main types of XSS attacks: reflected, stored, and DOM-based.
  - Reflected XSS occurs when the attacker sends a malicious link to the victim, and the web application echoes the user input in the response without proper validation or encoding.
  - Stored XSS occurs when the attacker stores the malicious script on the web application, such as in a database, a comment field, or a forum post, and the web application displays the script to the user without proper validation or encoding.
  - DOM-based XSS occurs when the attacker modifies the DOM (Document Object Model) of the web page using a client-side script, and the web application does not sanitize the user input before writing it to the DOM.
- To prevent XSS attacks, web applications should implement proper input validation, output encoding, and content security policies.
  - Input validation means checking the user input for any malicious characters or scripts, and rejecting or sanitizing them before processing.
  - Output encoding means converting the user input into a safe format, such as HTML entities, before displaying it on the web page.
  - Content security policies mean setting rules for the web browser to control what sources of content are allowed or blocked on the web page.