# Cross-site scripting

Cross-site scripting (XSS) is a type of security vulnerability that can be found in some web applications. XSS attacks enable attackers to inject client-side scripts into web pages viewed by other users. A cross-site scripting vulnerability may be used by attackers to bypass access controls such as the same-origin policy   .

## Types of XSS attacks

There are three main types of XSS attacks: reflected, stored, and DOM-based.

- Reflected XSS: The attacker sends a malicious link to the victim, who clicks on it and executes the script on the web page. The script is not stored on the server, but only reflected back to the victim's browser. For example, the attacker could craft a URL that contains a script in the query string, and send it to the victim via email or social media. When the victim opens the link, the script runs on the web page and performs the attacker's actions  .
- Stored XSS: The attacker injects a malicious script into a web page that is stored on the server, such as a comment, a forum post, or a profile. The script is then executed by any user who visits that web page. For example, the attacker could post a comment on a blog that contains a script that steals the cookies of other users who view the comment  .
- DOM-based XSS: The attacker injects a malicious script into a web page that modifies the Document Object Model (DOM) of the page. The script is not sent to the server, but only runs on the client-side. For example, the attacker could manipulate the URL fragment (the part after the # symbol) to include a script that changes the content or behavior of the web page  .

## Impacts of XSS attacks

XSS attacks can have various impacts on the web application and its users, depending on the attacker's goals and the type of script injected. Some possible impacts are:

- Stealing sensitive information, such as cookies, session tokens, credentials, or personal data, that can be used to impersonate or compromise the user's account   .
- Redirecting the user to a malicious website, such as a phishing site, that can trick the user into revealing their credentials or installing malware   .
- Performing unauthorized actions on behalf of the user, such as changing their password, posting messages, or transferring funds   .
- Defacing the web page, such as changing its appearance, content, or functionality, to damage the reputation or credibility of the web application   .
- Exploiting the user's browser, such as installing malware, keyloggers, or ransomware, that can harm the user's device or data   .

## Prevention of XSS attacks

XSS attacks can be prevented by applying proper input validation, output encoding, and content security policies on the web application. Some best practices are:

- Input validation: The web application should check and sanitize the user input before processing or storing it, to ensure that it does not contain any malicious scripts or characters. For example, the web application could use a whitelist of allowed input characters, or a blacklist of disallowed input characters, to filter out any scripts or HTML tags  .
- Output encoding: The web application should encode the user output before displaying it on the web page, to ensure that it does not execute as a script or HTML element. For example, the web application could use HTML entities or URL encoding to escape any special characters, such as <, >, ", or &  .
- Content security policy: The web application should specify a content security policy (CSP) that defines the sources and types of content that are allowed to be loaded or executed on the web page, to prevent any unauthorized scripts or resources from running. For example, the web application could use a CSP header or meta tag to restrict the sources of scripts, images, stylesheets, or fonts, or to disable inline