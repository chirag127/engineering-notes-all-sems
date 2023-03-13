### Regular Expressions

- Regular expressions are a way of specifying patterns of text using a concise syntax.
- Regular expressions can be used to search, extract, replace, or validate text data.
- Regular expressions are composed of literals and metacharacters.
- Literals are characters that match themselves, such as `a`, `b`, `1`, or `.`.
- Metacharacters are characters that have special meanings, such as `*`, `+`, `?`, `|`, `^`, `$`, `[`, `]`, `(`, `)`, `{`, `}`, `.` or `\`.
- Some common metacharacters and their meanings are:

  - `*` matches zero or more occurrences of the preceding expression.
  - `+` matches one or more occurrences of the preceding expression.
  - `?` matches zero or one occurrence of the preceding expression.
  - `|` matches either the expression before or the expression after it.
  - `^` matches the beginning of a line or string.
  - `$` matches the end of a line or string.
  - `[...]` matches any one of the characters inside the brackets.
  - `[^...]` matches any one of the characters not inside the brackets.
  - `.` matches any single character except newline.
  - `\` escapes the following character or introduces a special sequence.
  - `(...)` groups a subexpression and captures its match.
  - `{m,n}` matches the preceding expression at least m times and at most n times.

- Some examples of regular expressions and their meanings are:

  - `a*b` matches any number of `a`s followed by a `b`, such as `b`, `ab`, `aab`, `aaab`, etc.
  - `a+b` matches one or more `a`s followed by a `b`, such as `ab`, `aab`, `aaab`, etc.
  - `a?b` matches zero or one `a` followed by a `b`, such as `b` or `ab`.
  - `a|b` matches either `a` or `b`.
  - `^a` matches `a` at the beginning of a line or string.
  - `a$` matches `a` at the end of a line or string.
  - `[abc]` matches any one of `a`, `b`, or `c`.
  - `[^abc]` matches any one of not `a`, `b`, or `c`.
  - `.` matches any single character except newline.
  - `\d` matches any digit, equivalent to `[0-9]`.
  - `\w` matches any word character, equivalent to `[a-zA-Z0-9_]`.
  - `\s` matches any whitespace character, equivalent to `[ \t\n\r\f\v]`.
  - `(a|b)c` matches either `ac` or `bc`.
  - `a{3,5}` matches `a` repeated three, four, or five times, such as `aaa`, `aaaa`, or `aaaaa`.