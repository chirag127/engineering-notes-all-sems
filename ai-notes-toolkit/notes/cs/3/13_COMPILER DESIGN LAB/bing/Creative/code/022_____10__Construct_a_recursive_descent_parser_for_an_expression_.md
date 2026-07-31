### 10. Construct a recursive descent parser for an expression.

A recursive descent parser is a type of top-down parser that uses a set of recursive procedures to process the input. Each procedure corresponds to a nonterminal symbol in the grammar, and tries to match the input with one of the productions for that nonterminal. A recursive descent parser can be constructed for any LL(1) grammar, which is a grammar that can be parsed by looking at the next input symbol (left-to-right) and the leftmost nonterminal (leftmost derivation).

To construct a recursive descent parser for an expression, we need to define the grammar of the expression language, and then write a procedure for each nonterminal symbol. For example, suppose we have the following grammar for arithmetic expressions:

```
E -> T + E | T
T -> F * T | F
F -> ( E ) | id
```

This grammar can be simplified by eliminating the left recursion, which is a source of infinite recursion in a recursive descent parser. We can use the following transformation rule to eliminate the left recursion:

```
A -> A α | β
```

becomes

```
A -> β A'
A' -> α A' | ε
```

where ε is the empty string. Applying this rule to our grammar, we get:

```
E -> T E'
E' -> + T E' | ε
T -> F T'
T' -> * F T' | ε
F -> ( E ) | id
```

Now we can write a recursive procedure for each nonterminal symbol, using the following pseudocode conventions:

- `match(token)` consumes the next input symbol if it matches the given token, otherwise reports an error.
- `next()` returns the next input symbol without consuming it.
- `error(msg)` reports an error with the given message and terminates the parsing.

The procedures are:

```
parse_E():
  parse_T()
  parse_E'()

parse_E'():
  if next() == '+':
    match('+')
    parse_T()
    parse_E'()
  else:
    return // do nothing for ε

parse_T():
  parse_F()
  parse_T'()

parse_T'():
  if next() == '*':
    match('*')
    parse_F()
    parse_T'()
  else:
    return // do nothing for ε

parse_F():
  if next() == '(':
    match('(')
    parse_E()
    match(')')
  elif next() == 'id':
    match('id')
  else:
    error('Expected ( or id')
```

To parse an input expression, we call `parse_E()` and check if the input is exhausted. If not, we report an error. For example, to parse the input `id + id * id`, we get the following sequence of calls:

```
parse_E()
  parse_T()
    parse_F()
      match('id')
    parse_T'()
      return
  parse_E'()
    match('+')
    parse_T()
      parse_F()
        match('id')
      parse_T'()
        match('*')
        parse_F()
          match('id')
        parse_T'()
          return
    parse_E'()
      return
```

The input is exhausted and no error is reported, so the parsing is successful.