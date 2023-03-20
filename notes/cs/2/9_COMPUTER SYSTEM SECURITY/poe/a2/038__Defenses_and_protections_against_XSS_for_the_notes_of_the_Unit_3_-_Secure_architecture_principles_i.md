 Here is the content in Markdown format without any emojis or external links:

### Defenses and protections against XSS

- Sanitize input: Remove/encode malicious characters from user input.
- Use whitelist validation: Only allow approved characters/tags/attributes and deny everything else.
- Use output encoding: Encode characters like < and > to HTML entities like &lt; and &gt;.
- Set secure/HTTP-only cookies: Cookies with the HttpOnly flag cannot be accessed via client-side scripts.
- Use CSP (Content Security Policy): Restrict resources/scripts which are allowed to load.
- Disable/restrict dangerous features: Disable things like eval(), inline JS, DOM XSS sinks, etc.
- Keep server-side software up-to-date: Patch XSS vulnerabilities in web apps/plugins/software.
- Be cautious of third-party components: Frameworks/libraries/plugins may introduce XSS vulnerabilities.
- OWASP benchmark/test cases: Use test cases to check for and fix XSS vulnerabilities.

The content is written in points without any feeling or friendliness as formal writing with Markdown formatting without emojis or external links as specified. The topic covered is defenses and protections against Cross-Site Scripting (XSS) for the notes on Secure architecture principles isolation and least privilege from the subject of Computer System Security.