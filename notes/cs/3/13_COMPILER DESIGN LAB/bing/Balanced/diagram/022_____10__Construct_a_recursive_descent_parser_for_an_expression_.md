Hello, I am Sydney, your AI assistant. I can help you with your topic.

### 10. Construct a recursive descent parser for an expression.

A recursive descent parser is a type of top-down parser that uses a set of recursive procedures to process the input. Each procedure implements one of the production rules of the grammar, with the same name as the non-terminal symbol it represents. The parser can handle left recursion and precedence by transforming the grammar or using auxiliary techniques.

To construct a recursive descent parser for an expression, we need to follow these steps:

- Define the grammar of the expression language, such as:

```
E -> T + E | T
T -> F * T | F
F -> (E) | id
```

- Eliminate any left recursion or common prefixes in the grammar, such as:

```
E -> T E'
E' -> + T E' | ε
T -> F T'
T' -> * F T' | ε
F -> (E) | id
```

- Write a recursive procedure for each non-terminal symbol in the grammar, such as:

```
void E() {
  T();
  E_prime();
}

void E_prime() {
  if (lookahead == '+') {
    match('+');
    T();
    E_prime();
  }
  else {
    // do nothing, epsilon case
  }
}

void T() {
  F();
  T_prime();
}

void T_prime() {
  if (lookahead == '*') {
    match('*');
    F();
    T_prime();
  }
  else {
    // do nothing, epsilon case
  }
}

void F() {
  if (lookahead == '(') {
    match('(');
    E();
    match(')');
  }
  else if (lookahead == 'id') {
    match('id');
  }
  else {
    // error, unexpected token
  }
}

void match(char c) {
  if (lookahead == c) {
    // consume the token and advance the lookahead
  }
  else {
    // error, expected token c
  }
}
```

- Call the procedure corresponding to the start symbol of the grammar, such as:

```
void parse() {
  // initialize the lookahead
  E();
  // check if the input is fully consumed
  if (lookahead == '$') {
    // success, the input is accepted
  }
  else {
    // error, the input is rejected
  }
}
```

- Test the parser with some sample inputs, such as:

```
id + id * id
( id + id ) * id
id + ( id * id )
id * id + id
```

- Draw a parse tree for each input, such as:

```
id + id * id

    E
   / \
  T   E'
 / \ / \
F  T' + E
| / \  / \
id * F T' ε
    | |
    id ε

( id + id ) * id

    E
   / \
  T   E'
 / \ / \
F  T' * E
| / \  / \
( E ) ε F T'
  |    | |
  T    id ε
 / \
F  E'
| / \
id + E
   / \
  T   E'
 / \ / \
F  T' ε
| / \
id ε

id + ( id * id )

    E
   / \
  T   E'
 / \ / \
F  T' + E
| / \  / \
id ε ( E ) T'
     | / \
     T   E'
    / \ / \
   F  T' ε
   | / \
   id * F
      | |
      id ε

id * id + id

    E
   / \
  T   E'
 / \ / \
F  T' + E
| / \  / \
id * F T' ε
    | / \
    id ε F T'
         | / \
         id ε
```