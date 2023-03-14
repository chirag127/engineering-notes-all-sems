### Regular Expressions

- Regular expressions are a way of specifying patterns of text using a concise syntax.
- Regular expressions can be used to search, extract, replace, or validate text data.
- Regular expressions are composed of literals and metacharacters.
- Literals are characters that match themselves, such as `a`, `b`, `1`, or `.`.
- Metacharacters are characters that have special meanings, such as `*`, `+`, `?`, `|`, `^`, `$`, `[`, `]`, `(`, `)`, `{`, `}`, `\`, or `/`.
- Some common metacharacters and their meanings are:

  - `*` matches zero or more occurrences of the preceding expression.
  - `+` matches one or more occurrences of the preceding expression.
  - `?` matches zero or one occurrence of the preceding expression.
  - `|` matches either the expression before or the expression after it.
  - `^` matches the beginning of a line or string.
  - `$` matches the end of a line or string.
  - `[...]` matches any one of the characters inside the brackets.
  - `[^...]` matches any one of the characters not inside the brackets.
  - `(...)` groups a subexpression and captures its match.
  - `{n}` matches exactly n occurrences of the preceding expression.
  - `{n,m}` matches at least n and at most m occurrences of the preceding expression.
  - `\` escapes the following character or introduces a special sequence.
  - `/` delimits the regular expression.

- Some examples of regular expressions and their meanings are:

  - `/a*b/` matches any number of `a`s followed by a `b`, such as `b`, `ab`, `aab`, or `aaaaab`.
  - `/[a-z]+/` matches one or more lowercase letters, such as `apple`, `cat`, or `zoo`.
  - `/[0-9]{3}-[0-9]{4}/` matches a phone number of the form `###-####`, such as `123-4567` or `987-6543`.
  - `/^https?:\/\/(www\.)?example\.com\/?$/` matches a URL of the form `http://example.com`, `https://example.com`, `http://www.example.com`, or `https://www.example.com`, with or without a trailing slash.
  - `/[A-Z][a-z]*( [A-Z][a-z]*)*/` matches a proper name consisting of one or more capitalized words separated by spaces, such as `Alice`, `Bob Smith`, or `Charles Darwin`.