### Cross site scripting for the notes of the Unit 3 - Secure architecture principles isolation and least privilege in the subject of COMPUTER SYSTEM SECURITY

Cross-Site Scripting (XSS) is a type of vulnerability that can occur in web applications. It allows attackers to inject malicious scripts into web pages viewed by other users. This can result in a range of attacks, such as stealing user data, defacing websites, or redirecting users to malicious sites.

There are three main types of XSS vulnerabilities:

1. Stored XSS: This type of vulnerability occurs when user input is stored on the server and later displayed to other users without proper validation or escaping. For example, an attacker could post a comment on a blog containing a malicious script, which would then be displayed to all users who view the blog post.

2. Reflected XSS: This type of vulnerability occurs when user input is immediately returned by the server in an HTTP response without proper validation or escaping. For example, an attacker could send a link to a victim containing a malicious script as a search query. When the victim clicks on the link, the script would be executed by their browser.

3. DOM-based XSS: This type of vulnerability occurs when a script on a web page manipulates the Document Object Model (DOM) in a way that allows an attacker to inject malicious scripts. For example, an attacker could manipulate the URL of a web page to include a malicious script, which would then be executed by the victim's browser when the page is loaded.

To prevent XSS vulnerabilities, it is important to follow secure coding practices, such as validating and sanitizing user input, using secure methods for handling user input, and encoding data before displaying it to the user. Additionally, using security features such as Content Security Policy (CSP) can help mitigate the risk of XSS attacks.