### 10. Construct a recursive descent parser for an expression.

- A recursive descent parser is a top-down parser that uses a set of recursive procedures to process the input.
- Each procedure implements one of the nonterminals of the grammar, and the parser starts with the procedure for the start symbol.
- The parser consumes one token of input at a time, and decides which procedure to call based on the current token and the grammar rules.
- The parser can use a lookahead token to predict which alternative to choose in a production with multiple options.
- The parser can also use backtracking to try different alternatives if the current one fails, but this may be inefficient or ambiguous.
- A recursive descent parser can be constructed for an expression grammar by following these steps:

  - Define the grammar rules for the expression, such as:

    ```
    E -> T + E | T
    T -> F * T | F
    F -> (E) | id
    ```

  - Write a procedure for each nonterminal, such as:

    ```
    def parse_E():
      parse_T()
      if lookahead == '+':
        match('+')
        parse_E()

    def parse_T():
      parse_F()
      if lookahead == '*':
        match('*')
        parse_T()

    def parse_F():
      if lookahead == '(':
        match('(')
        parse_E()
        match(')')
      elif lookahead == 'id':
        match('id')
      else:
        error()
    ```

  - Write a procedure to match the current token and advance the lookahead, such as:

    ```
    def match(token):
      if lookahead == token:
        lookahead = next_token()
      else:
        error()
    ```

  - Write a procedure to handle errors, such as:

    ```
    def error():
      print("Syntax error")
      exit()
    ```

  - Initialize the lookahead token and call the procedure for the start symbol, such as:

    ```
    lookahead = next_token()
    parse_E()
    ```