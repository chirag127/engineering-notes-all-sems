#### URL in Networking

- A URL (Uniform Resource Locator) is a string that identifies a resource on the Internet and how to access it.
- A URL consists of several components, such as the scheme, the authority, the path, the query, and the fragment.
- The scheme specifies the protocol used to communicate with the resource, such as http, https, ftp, mailto, etc.
- The authority identifies the host that provides the resource, and may include a username, a password, a hostname, and a port number.
- The path specifies the location of the resource on the host, and may consist of one or more segments separated by slashes (/).
- The query contains additional information that may be used by the resource, such as parameters, filters, options, etc. The query starts with a question mark (?) and consists of one or more name-value pairs separated by ampersands (&).
- The fragment identifies a specific part of the resource, such as a section, a paragraph, or an element. The fragment starts with a hash (#) and follows the rules of the resource's media type.
- A URL can be absolute or relative. An absolute URL contains all the components, while a relative URL omits some of them and is resolved based on the context of a base URL.
- A URL can be encoded or decoded to handle special characters that may not be allowed or may have special meanings in the URL components. The encoding and decoding process uses percent-encoding, which replaces a character with a percent sign (%) followed by its hexadecimal code.
- A URL can be normalized or canonicalized to remove or standardize some variations that may not affect the identification of the resource, such as case, punctuation, encoding, etc. The normalization process may improve the usability, readability, and comparability of URLs.

Some examples of URLs are:

- `https://www.example.com/index.html` : an absolute URL that uses the https scheme, the authority www.example.com, and the path /index.html.
- `../images/logo.png` : a relative URL that uses the path ../images/logo.png, and is resolved based on the base URL of the current document.
- `mailto:alice@example.com?subject=Hello&body=Hi%20Alice` : an absolute URL that uses the mailto scheme, the authority alice@example.com, and the query subject=Hello&body=Hi%20Alice. The query is encoded to replace the space character with %20.
- `https://en.wikipedia.org/wiki/URL#Syntax` : an absolute URL that uses the https scheme, the authority en.wikipedia.org, the path /wiki/URL, and the fragment Syntax. The fragment identifies a specific section of the Wikipedia article on URL.

Some mnemonics and learning tricks for URL in Networking are:

- To remember the components of a URL, use the acronym SAP QF: Scheme, Authority, Path, Query, Fragment.
- To remember the order of the components of a URL, use the phrase "Some Angry People Question Facts".
- To remember the syntax of a URL, use the formula `scheme://authority/path?query#fragment`.
- To remember the encoding and decoding process of a URL, use the phrase "Percent-encode to prevent problems".